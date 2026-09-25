# Worklog — delivery.go-release / container-artifact / infrastructure-preview

2026-09-25. Lifecycle: CANDIDATE. Disposition: EXTRACT.

Implemented three `workflow_call` workflows matching the existing contracts:

- `.github/workflows/go-release.yml` — version + asset verification; optional
  GitHub Release publish behind explicit `contents: write`.
- `.github/workflows/container-artifact.yml` — Buildx multi-platform build,
  Trivy CRITICAL fail, optional push + Cosign keyless sign; digest output only
  when pushed.
- `.github/workflows/infrastructure-preview.yml` — Pulumi `preview` only via
  OIDC AWS role + Pulumi token; never apply.

No private workflow text was copied. Action pins are full SHAs. Status remains
CANDIDATE until two real callers adopt each without weakening required checks
and maintainer review lands.

Skipped extract (still product-local / single-consumer): CloudTrail+Flow
Logs+Budgets audit stacks; Svix-shaped provider webhook ingress (use provider
algorithm or SDK; AMSL HMAC receivers use `go/webhookingress`).
