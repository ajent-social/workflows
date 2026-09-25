# delivery.go-lint

Status: CANDIDATE reusable workflow.

## Workflow

`.github/workflows/go-lint.yml` — `workflow_call` that runs credential-free
`golangci-lint` against a caller module directory.

### Inputs

| Input | Default | Purpose |
| --- | --- | --- |
| `working-directory` | `.` | Module directory |
| `go-version-file` | `go.mod` | Toolchain source |
| `golangci-lint-version` | `v2.11` | golangci-lint release tag |
| `args` | _(empty)_ | Extra `golangci-lint run` args (simple tokens) |
| `timeout-minutes` | `20` | Job bound |

### Non-goals

- Replacing product `.golangci.yml` policy
- Merging lint into go-validation (keep vet/test and lint as separate required checks when callers want that)
- Arbitrary shell hooks or secreted jobs

### Security defaults

- `permissions.contents: read`
- No secrets; no OIDC
- Actions pinned by full SHA
- Input paths and args pattern-validated

### Caller example

```yaml
jobs:
  go-lint:
    uses: ajent-social/workflows/.github/workflows/go-lint.yml@<immutable-sha>
    with:
      working-directory: .
      golangci-lint-version: v2.11
```

## Verification gate

Failed lint must fail the called job. Two real modules must adopt without
dropping existing required checks. Documentation CI alone is not consumer
verification. No real consumer adoption is recorded yet.

## Census evidence (2026-09-25)

Across admin-owned orgs, active repos in the last 18 months showed
`golangci-lint` in **14** workflow files spanning serenity, sire, gist, saka,
mint, blink, wolf, zatiti, ajent, dira, shiftmesh, and others.
