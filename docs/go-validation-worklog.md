# Worklog — delivery.go-validation

2026-09-24. Lifecycle: CANDIDATE. Disposition: EXTRACT.

Added reusable `workflow_call` workflow
`.github/workflows/go-validation.yml` with credential-free vet/test, optional
Postgres service for sqlstore consumers, read-only permissions and full-SHA
action pins. No private workflow text was copied.

Next: adopt from `ajent-social/go` and a second real module without weakening
caller-required checks; record CI runs and keep status CANDIDATE until human
review.
