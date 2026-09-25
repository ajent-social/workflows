# AMSL delivery workflows

Carry operational fixes forward with the workflow that needs them.

**Status: CANDIDATE reusable workflows for Go validation, Go lint, Go release
verification, container artifacts, and infrastructure preview.** This repository
defines:

| Contract | Workflow |
| --- | --- |
| [Go validation](contracts/go-validation.md) | [go-validation.yml](.github/workflows/go-validation.yml) |
| [Go lint](contracts/go-lint.md) | [go-lint.yml](.github/workflows/go-lint.yml) |
| [Go release](contracts/go-release.md) | [go-release.yml](.github/workflows/go-release.yml) |
| [Container artifact](contracts/container-artifact.md) | [container-artifact.yml](.github/workflows/container-artifact.yml) |
| [Infrastructure preview](contracts/infrastructure-preview.md) | [infrastructure-preview.yml](.github/workflows/infrastructure-preview.yml) |

Use reusable workflows for complete jobs and composite actions only for proven
repeated steps. Preserve product gates, required-check names, caller events and
trust boundaries. Templates alone do not maintain consumers.

Pin an immutable revision when calling
`ajent-social/workflows/.github/workflows/<name>.yml@<sha>`. Two real modules
must adopt without weakening their existing gates before experimental promotion.
Repository documentation CI is not a consumer test. Privileged workflows
(release publish, container push/sign, infrastructure preview) additionally
require denied-permission and event-trust evidence before promotion.

See the [security baseline](docs/security-baseline.md),
[verification matrix](docs/verification.md),
[P1 worklog](docs/p1-delivery-workflows-worklog.md) and
[canonical RFC](https://github.com/ajent-social/capabilities/blob/main/docs/rfc/0001-amsl-bootstrap.md).
