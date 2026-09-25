# delivery.container-artifact

Status: CANDIDATE reusable workflow.

## Workflow

`.github/workflows/container-artifact.yml` — `workflow_call` that builds
declared platforms with Buildx, optionally scans with Trivy (fail on CRITICAL),
optionally pushes, and optionally Cosign-signs a pushed digest. Mutable tags are
never promotion approval.

### Inputs

| Input | Default | Purpose |
| --- | --- | --- |
| `context` | `.` | Build context |
| `file` | `Dockerfile` | Dockerfile path |
| `image` | _(required)_ | Registry/name without tag or digest |
| `platforms` | `linux/amd64` | Buildx platforms |
| `ref` | _(empty)_ | Checkout ref |
| `push` | `false` | Push multi-platform image |
| `scan` | `true` | Trivy fs (+ image when loadable) |
| `sign` | `false` | Cosign keyless sign (requires `push`) |
| `timeout-minutes` | `45` | Job bound |

### Secrets

| Secret | Required when |
| --- | --- |
| `registry-username` / `registry-password` | `push` to non-`ghcr.io` registries |
| _(none)_ | `ghcr.io` push uses `GITHUB_TOKEN` |

### Outputs

| Output | Meaning |
| --- | --- |
| `digest` | `sha256:…` when `push=true`; empty otherwise |
| `image` | Image name without digest |

### Non-goals

- Universal builder or deployer
- Confusing image existence with promotion approval
- Long-lived registry passwords as the recommended path (prefer OIDC/`ghcr.io`)

### Security defaults

- `contents: read`; `packages: write` + `id-token: write` for push/sign
- Actions pinned by full SHA; bounded timeout
- Input paths and image refs pattern-validated

### Caller example

```yaml
jobs:
  artifact:
    uses: ajent-social/workflows/.github/workflows/container-artifact.yml@<immutable-sha>
    with:
      image: ghcr.io/example/app
      platforms: linux/amd64,linux/arm64
      push: true
      sign: true
```

Consumers must promote by digest, not by mutable tag.

## Verification gate

Test failed scan, substituted digest, incomplete platform matrix, and source
mismatch. Verify consumer promotion consumes the validated digest. No real
consumer adoption is recorded yet.
