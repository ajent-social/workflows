"""Exercise extracted workflow shell commands; no hosted Actions or PostgreSQL proof."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/go-validation.yml"


def workflow_steps(path):
    """Read only the existing fixed-indentation named steps; fail closed on drift."""
    lines = path.read_text().splitlines()
    steps = {"validate inputs": [], "go vet": [], "go test": []}
    for index, line in enumerate(lines):
        if not line.startswith("      - name: "):
            continue
        name = line.removeprefix("      - name: ")
        if name not in steps:
            continue
        run = index + 1
        while run < len(lines) and not lines[run].startswith("        run: "):
            if lines[run].startswith("      - "):
                raise AssertionError("named step has no shell command")
            run += 1
        if run == len(lines):
            raise AssertionError("named step has no shell command")
        value = lines[run].removeprefix("        run: ")
        if value == "|":
            body = []
            run += 1
            while run < len(lines) and (lines[run].startswith("          ") or not lines[run]):
                body.append(lines[run][10:])
                run += 1
            value = "\n".join(body)
        steps[name].append(value)
    if any(len(value) != 2 for value in steps.values()):
        raise AssertionError("expected two actual guard/vet/test steps")
    return steps


def run_shell(script, directory, **values):
    env = {key: os.environ[key] for key in ("PATH", "HOME", "TMPDIR", "GOCACHE", "GOMODCACHE") if key in os.environ}
    env.update(GOTOOLCHAIN="local", GOPROXY="off", GOSUMDB="off", GOWORK="off", GOFLAGS="-p=1", GOMAXPROCS="2", PACKAGES="./...", WORKDIR=".", RACE="false", FIXTURE_FAIL="0")
    env.update(values)
    return subprocess.run(["bash", "-euo", "pipefail", "-c", script], cwd=directory, env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=90)


class InputGuards(unittest.TestCase):
    def test_actual_guards(self):
        steps = workflow_steps(WORKFLOW)
        with tempfile.TemporaryDirectory(prefix="workflow-input-guard-") as directory:
            for branch, guard in enumerate(steps["validate inputs"]):
                for package in ("./...", "./nested", "example.com/fixture/nested"):
                    with self.subTest(branch=branch, accepted=package):
                        result = run_shell(guard, directory, PACKAGES=package)
                        self.assertEqual(result.returncode, 0, result.stdout)
                for package in ("", "-race", "--help", "-run=Injected", "./...;echo injected", "$(echo injected)", "./...\n./nested", "./... ./nested", "./...&", "./...|cat", "`echo injected`"):
                    with self.subTest(branch=branch, rejected=package):
                        result = run_shell(guard, directory, PACKAGES=package)
                        self.assertNotEqual(result.returncode, 0, "unsafe package input accepted")
                        self.assertIn("packages must", result.stdout)
                for workdir in ("", "../outside", ".;echo injected", "$(echo injected)"):
                    with self.subTest(branch=branch, workdir=workdir):
                        self.assertNotEqual(run_shell(guard, directory, WORKDIR=workdir).returncode, 0)


class ActualGoCommands(unittest.TestCase):
    def test_nested_module_pass_and_failure(self):
        self.assertIsNotNone(shutil.which("go"), "Go is required for actual command qualification")
        steps = workflow_steps(WORKFLOW)
        with tempfile.TemporaryDirectory(prefix="workflow-go-command-") as directory:
            root = Path(directory)
            (root / "go.mod").write_text("module example.com/fixture\n\ngo 1.20\n")
            (root / "nested").mkdir()
            (root / "nested/fixture_test.go").write_text('''package nested
import ("os"; "testing")
func TestFixture(t *testing.T) {
    if os.Getenv("FIXTURE_FAIL") == "1" { t.Fatal("synthetic test failure") }
}
''')
            self.assertEqual(list(root.glob("*.go")), [], "fixture must have no root Go files")
            for branch in range(2):
                for race in ("false", "true"):
                    for fail in ("0", "1"):
                        with self.subTest(branch=branch, race=race, failing=fail):
                            guard = run_shell(steps["validate inputs"][branch], directory)
                            self.assertEqual(guard.returncode, 0, guard.stdout)
                            if fail == "0":
                                vet = run_shell(steps["go vet"][branch], directory)
                                self.assertEqual(vet.returncode, 0, vet.stdout)
                            result = run_shell(steps["go test"][branch], directory, RACE=race, FIXTURE_FAIL=fail)
                            if fail == "0":
                                self.assertEqual(result.returncode, 0, result.stdout)
                                self.assertIn("example.com/fixture/nested", result.stdout)
                            else:
                                self.assertNotEqual(result.returncode, 0, "failing test was masked")
                                self.assertIn("synthetic test failure", result.stdout)
                with self.subTest(branch=branch, missing_package=True):
                    result = run_shell(steps["go test"][branch], directory, PACKAGES="./absent")
                    self.assertNotEqual(result.returncode, 0, "missing package succeeded")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workflow", type=Path, default=WORKFLOW, help="actual workflow source to exercise")
    parser.add_argument("--static-only", action="store_true", help="exercise actual Bash input guards only; no Go command qualification")
    args = parser.parse_args()
    WORKFLOW = args.workflow
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(InputGuards)
    if not args.static_only:
        suite.addTests(loader.loadTestsFromTestCase(ActualGoCommands))
    raise SystemExit(not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful())
