# Worklog — delivery.go-validation

2026-09-24. Lifecycle: CANDIDATE. Disposition: EXTRACT.

Added reusable `workflow_call` workflow
`.github/workflows/go-validation.yml` with credential-free vet/test, optional
Postgres service for sqlstore consumers, read-only permissions and full-SHA
action pins. No private workflow text was copied.

Next: adopt from `ajent-social/go` and a second real module without weakening
caller-required checks; record CI runs and keep status CANDIDATE until human
review.

## 2026-09-24 — first consumer adoptions

- `ajent-social/go` adopts the pinned workflow with `enable-postgres: true`
  (PR merge pending/landed as go#5).
- `zerfoo/zerfoo` adds an additional `amsl-go-validation` job without replacing
  its existing required `test` job (PR #1016).
- Catalog record updated in capabilities (PR #6).
