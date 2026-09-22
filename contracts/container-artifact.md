# delivery.container-artifact

Status: candidate; no released workflow.

Build declared platforms and return a verified digest only after required scanning/signing steps. Bind provenance to source. Publishing may precede scanning; callers must not confuse image existence with promotion approval. Caller owns builder/registry and deployment policy.

## Verification gate

Test failed scan/sign, substituted digest, incomplete platform matrix and source mismatch. Verify consumer promotion consumes the validated digest rather than a mutable tag.

No execution or real consumer adoption is recorded yet.
