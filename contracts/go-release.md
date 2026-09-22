# delivery.go-release

Status: candidate; no released workflow.

Bind checkout to intended release revision. Validate the native version stamp and complete expected architecture/asset set before publication. Publication requires explicit job permissions; external repository credentials are separate. Caller owns version/tag scheme and prerequisite gates.

## Verification gate

Test wrong version, missing asset, failed prerequisite, wrong checkout revision and denied publication permission. Synthetic assets do not establish real release compatibility.

No execution or real consumer adoption is recorded yet.
