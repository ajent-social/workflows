# Worklog — delivery.go-validation

2026-09-24. Lifecycle: CANDIDATE. Disposition: EXTRACT.

Added reusable `workflow_call` workflow
`.github/workflows/go-validation.yml` with credential-free vet/test, optional
Postgres service for sqlstore consumers, read-only permissions and full-SHA
action pins. No private workflow text was copied.

Next: adopt from `ajent-social/go` and a second real module without weakening
caller-required checks; record CI runs and keep status CANDIDATE until human
review.

## 2026-09-24 — first consumer adoptions

- `ajent-social/go` adopts the pinned workflow with `enable-postgres: true`
  (PR merge pending/landed as go#5).
- `zerfoo/zerfoo` adds an additional `amsl-go-validation` job without replacing
  its existing required `test` job (PR #1016).
- Catalog record updated in capabilities (PR #6).

## 2026-10-16 — preserve Go test package arguments

Capability: `delivery.go-validation`; lifecycle remains CANDIDATE.
A public synthetic module with a root `go.mod`, no root Go files and a nested
test package exposes the command defect: `go test -- ./...` treats the separator
and package pattern as test-binary arguments instead of selecting the nested
packages. Both race modes and both optional-Postgres branches used this form.

The correction passes the single validated package pattern directly to `go test`.
Both existing input guards now explicitly reject a leading dash to prevent
package inputs from becoming Go flags. Vet and test quote that single pattern,
which the guards already restrict against whitespace and shell metacharacters;
this also prevents shell filename expansion. Action pins, permissions, services,
caches and caller inputs are unchanged. No new dependency or copied source is
introduced; the small regression driver uses Python's standard library, Bash
and the installed Go toolchain. Original contribution: Apache-2.0.

`tools/test_go_validation_commands.py` extracts the actual guard/vet/test shell
bodies from the workflow. Its default mode exercises nested-module success and
intentional test failure for race/non-race in both branches, plus missing package
failure. Its input cases reject empty patterns, leading flags and shell
metacharacters. `--static-only` runs the actual Bash input guards without claiming
Go command qualification. `--workflow PATH` can exercise the original source for
failing-before evidence. The branches are command fixtures: no PostgreSQL service
or hosted GitHub Actions execution is established.

Observed locally: original input guards fail the leading-dash regression;
corrected input guards pass. Actionlint and local documentation links pass.
The full actual-Go command matrix remains pending a bounded verification runner.
Human maintainer review and merge remain pending; no upstream maturity,
consumer adoption, hosted CI or service qualification is claimed by this patch.
