# Proposed workflow security baseline

- Read-only repository permissions by default; job-specific write/OIDC grants.
- Explicit named secrets; no blanket inheritance or arbitrary privileged shell hooks.
- Reviewed full-SHA references for actions and reusable workflows; deliberate updates.
- Bind artifacts to checked-out source and verify digests before promotion.
- No untrusted PR execution with production credentials or on privileged persistent runners.
- Treat previews and downloaded tools as code execution.
- Bound job time and output; keep secrets and internal identifiers out of artifacts.
- Cancel obsolete PR validation; preserve required builds and serialize deployments appropriately.
- Preserve caller events, required-check names and failure aggregation on adoption.

Use actionlint and zizmor as complementary static tools, not proof of safe execution. Organization rules and runner/cloud trust must enforce policy beyond an optional shared workflow. This document is a proposed contract, not evidence those controls are deployed.
