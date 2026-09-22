# delivery.infrastructure-preview

Status: candidate; no released workflow.

Preview trusted code with explicitly scoped identity, state access and bounded result artifacts. Preview executes code even with a read-only cloud role. Caller owns stack, backend, event trust, environment and apply approval.

## Verification gate

Test untrusted-event exclusion, denied write scope, redaction of secrets/state, failed preview result propagation and caller permissions. Verify live trust separately from YAML validation.

No execution or real consumer adoption is recorded yet.
