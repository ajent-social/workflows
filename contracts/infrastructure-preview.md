# delivery.infrastructure-preview

Status: CANDIDATE reusable workflow.

## Workflow

`.github/workflows/infrastructure-preview.yml` — `workflow_call` that runs
`pulumi preview` only against a caller stack with GitHub OIDC → AWS role and a
Pulumi access token. Never applies.

### Inputs

| Input | Default | Purpose |
| --- | --- | --- |
| `working-directory` | `.` | Pulumi program directory |
| `stack-name` | _(required)_ | Pulumi stack name |
| `ref` | _(empty)_ | Checkout ref |
| `cloud-region` | `us-west-2` | AWS region for OIDC credentials |
| `go-version-file` | `go.mod` | Toolchain for Go programs |
| `timeout-minutes` | `30` | Job bound |

### Secrets

| Secret | Purpose |
| --- | --- |
| `aws-role-arn` | IAM role assumed via OIDC for preview |
| `pulumi-access-token` | Pulumi Cloud (or equivalent) token |

### Outputs

| Output | Meaning |
| --- | --- |
| `preview-outcome` | `success` / failure from the preview step |

### Non-goals

- Automatic production apply
- Choosing the caller's stack backend or event trust policy
- Redacting all possible secret leakage from program logs (caller must design)

### Security defaults

- `contents: read` + `id-token: write`
- Preview only (`command: preview`, `upsert: false`)
- Actions pinned by full SHA; bounded timeout
- Inputs pattern-validated

Preview still executes checked-out code. Treat it as code execution with a
narrow cloud role, not as a read-only document check.

### Caller example

```yaml
jobs:
  preview:
    uses: ajent-social/workflows/.github/workflows/infrastructure-preview.yml@<immutable-sha>
    with:
      working-directory: deploy/cloud
      stack-name: org/app/staging
    secrets:
      aws-role-arn: ${{ secrets.AWS_PREVIEW_ROLE_ARN }}
      pulumi-access-token: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

## Verification gate

Test untrusted-event exclusion (caller-side), denied write scope on the role,
failed preview propagation, and that apply is impossible via this workflow. Live
trust is separate from YAML validation. No real consumer adoption is recorded yet.
