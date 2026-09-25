# Verification matrix

1. Static syntax and security analysis with existing tools (actionlint, zizmor).
2. Synthetic caller fixtures for input/output and failure behavior.
3. Real caller runs preserving required checks, events and permissions.
4. Privileged workflows (go-release publish, container push/sign, infrastructure
   preview) additionally require denied-event/permission tests and
   artifact/source verification.
5. Explicit maintainer review before promotion.

Go validation has CANDIDATE workflow source and early consumer adoption PRs;
go-release, container-artifact and infrastructure-preview have CANDIDATE
workflow source with no consumer adoption recorded yet. The repository's
documentation-link workflow is only a bootstrap check.
