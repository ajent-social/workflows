# delivery.go-validation

Status: candidate; no released workflow.

Credential-free Go vet/test/race validation. Declare module path, Go version source, timeout and service requirements. No arbitrary shell hook. Return failure if any required check fails. Caller retains events, required-check names and custom gates.

## Verification gate

Test failure propagation, malformed module paths, module directories containing spaces, race failures, cancellation, merge-queue events and required-check behavior. Two real modules must adopt without losing validation.

No execution or real consumer adoption is recorded yet.
