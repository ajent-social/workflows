# AMSL delivery workflows

Carry operational fixes forward with the workflow that needs them.

<<<<<<< HEAD
**Status: CANDIDATE reusable workflows for Go validation, Go release
verification, container artifacts, and infrastructure preview.** This repository
defines:
=======
**Status: CANDIDATE reusable workflows.** Implemented:
>>>>>>> 313c3f9 (Add go-lint reusable workflow from active-repo census.)

| Contract | Workflow |
| --- | --- |
| [Go validation](contracts/go-validation.md) | [go-validation.yml](.github/workflows/go-validation.yml) |
<<<<<<< HEAD
| [Go release](contracts/go-release.md) | [go-release.yml](.github/workflows/go-release.yml) |
| [Container artifact](contracts/container-artifact.md) | [container-artifact.yml](.github/workflows/container-artifact.yml) |
| [Infrastructure preview](contracts/infrastructure-preview.md) | [infrastructure-preview.yml](.github/workflows/infrastructure-preview.yml) |
=======
| [Go lint](contracts/go-lint.md) | [go-lint.yml](.github/workflows/go-lint.yml) |

Documented (implementation may land on sibling branches/PRs):
[go-release](contracts/go-release.md),
[container-artifact](contracts/container-artifact.md),
[infrastructure-preview](contracts/infrastructure-preview.md).
>>>>>>> 313c3f9 (Add go-lint reusable workflow from active-repo census.)

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
<<<<<<< HEAD
[P1 worklog](docs/p1-delivery-workflows-worklog.md) and
=======
[active-repo census](docs/active-repo-census-2026-09.md) and
>>>>>>> 313c3f9 (Add go-lint reusable workflow from active-repo census.)
[canonical RFC](https://github.com/ajent-social/capabilities/blob/main/docs/rfc/0001-amsl-bootstrap.md).
