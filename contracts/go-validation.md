# delivery.go-validation

Status: CANDIDATE reusable workflow. Not a stable delivery API.

## Workflow

`.github/workflows/go-validation.yml` — `workflow_call` job that runs
credential-free `go vet` and `go test` (race by default).

### Inputs

| Input | Default | Purpose |
| --- | --- | --- |
| `working-directory` | `.` | Module directory with `go.mod` |
| `go-version-file` | `go.mod` | Toolchain source for `setup-go` |
| `packages` | `./...` | Package set for vet/test |
| `race` | `true` | Race detector |
| `timeout-minutes` | `15` | Job bound |
| `enable-postgres` | `false` | Optional Postgres 16 service + `AMSL_SQLSTORE_TEST_DSN` |
| `postgres-db` | `amsl_servicecred_test` | DB name when Postgres is enabled |

### Non-goals

- Arbitrary caller shell hooks
- Deployment, release, container build, or secreted jobs
- Replacing product-required check names or merge-queue policy
- Cross-compile matrices (keep those in the caller)

### Security defaults

- `permissions.contents: read`
- No secrets; no OIDC
- Actions pinned by full SHA
- Bounded timeout

### Caller example

```yaml
jobs:
  go-validation:
    uses: ajent-social/workflows/.github/workflows/go-validation.yml@<immutable-sha>
    with:
      enable-postgres: true
```

Pin a reviewed commit SHA. Moving tags are not an adoption record.

## Verification gate

- Failed vet/test must fail the called job.
- Two real modules must adopt without dropping existing required checks.
- Documentation CI alone is not consumer verification.
