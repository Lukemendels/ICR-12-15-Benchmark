# Changelog and version policy

## 1.0.0 — 2026-09-09
First portable JSON evidence release from completed federal benchmark, frozen TSA evidence graph, consistency report and EAB leadership brief. Includes schemas, provenance, distinct adjudication registers, exact retrieval indexes, dependency-free consumer, integrity validation and clean-load evidence.

Patch: metadata/provenance correction with unchanged analytical meaning and compatible identities/contracts. Minor: additive evidence, indexes or compatible schema extension. Major: incompatible schema, changed identity meaning or incompatible analytical interpretation. Corrected substantive evidence must be reviewed, identified and versioned; never use a metadata patch to conceal a changed conclusion.

All published versions are immutable, including patches. Every correction creates a new directory, manifest, hashes, validation results and release identity. Never silently replace v1.0.0. A derived SQLite cache may be regenerated from canonical JSON and discarded; its generation must declare the source manifest digest.
