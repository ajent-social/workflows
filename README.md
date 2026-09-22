# AMSL delivery workflows

Carry operational fixes forward with the workflow that needs them.

**Status: contract foundation. No reusable workflow is released for consumption yet.** This repository defines [Go validation](contracts/go-validation.md), [release verification](contracts/go-release.md), [container artifacts](contracts/container-artifact.md) and [infrastructure preview](contracts/infrastructure-preview.md) boundaries.

Use reusable workflows for complete jobs and composite actions only for proven repeated steps. Preserve product gates, required-check names, caller events and trust boundaries. Templates alone do not maintain consumers.

The first experiment is credential-free Go validation. It must run in two real modules without weakening their existing gates before being presented as proven reuse. Repository documentation CI is not a consumer test.

See the [security baseline](docs/security-baseline.md), [verification matrix](docs/verification.md) and [canonical RFC](https://github.com/ajent-social/capabilities/blob/main/docs/rfc/0001-amsl-bootstrap.md).
