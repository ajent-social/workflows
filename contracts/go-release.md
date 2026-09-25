# delivery.go-release

Status: CANDIDATE reusable workflow.

## Workflow

`.github/workflows/go-release.yml` — `workflow_call` that verifies a release
version string against optional native stamp output and a declared asset set
under `dist-directory`. Optional `publish` creates a GitHub Release only when
the caller grants `contents: write`.

### Inputs

| Input | Default | Purpose |
| --- | --- | --- |
| `working-directory` | `.` | Module directory |
| `go-version-file` | `go.mod` | Toolchain source |
| `ref` | _(empty)_ | Checkout ref; empty uses caller SHA |
| `version` | _(required)_ | Expected version (e.g. `v1.2.3`) |
| `version-command` | _(empty)_ | Optional stamp command; empty skips stamp check |
| `dist-directory` | `dist` | Asset directory |
| `expected-assets` | _(required)_ | Newline-separated file names under dist |
| `timeout-minutes` | `20` | Job bound |
| `publish` | `false` | Create GitHub Release after verify |

### Outputs

| Output | Meaning |
| --- | --- |
| `version` | Verified version |
| `assets-ok` | `true` when all assets were present and non-empty |

### Non-goals

- Replacing GoReleaser or inventing a version scheme
- Cross-compile matrices (caller builds assets before calling)
- External registry credentials

### Security defaults

- Verify job: `permissions.contents: read`
- Publish job: `contents: write` only when `publish: true`
- Actions pinned by full SHA; bounded timeout
- Asset names reject path separators and shell metacharacters

### Caller example

```yaml
jobs:
  release:
    uses: ajent-social/workflows/.github/workflows/go-release.yml@<immutable-sha>
    with:
      version: v1.2.3
      expected-assets: |
        app_linux_amd64
        app_darwin_arm64
      publish: false
```

## Verification gate

Test wrong version stamp, missing asset, empty asset, denied publication
permission, and checkout of an unintended revision. Synthetic assets do not
establish real release compatibility. No real consumer adoption is recorded yet.
