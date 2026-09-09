# Loop 5.1 — portable release architecture

Status: INPUTS_VERIFIED / checkpoint A.

Authoritative source head: 1a5b3e852ad1c7d837d65e578bd706a46218311f (completed EAB brief). Mission 3 freeze: b96aaaa4d81fe4df432602a0ae1346be78a151b1. Mission 4 completion: 34d94576f95b3a780ea3ec869b7c9c4fb653baa6. All 2,273 source-head blobs verified against GitHub identities; every existing Mission 3 freeze blob is unchanged at source head.

Release: release/icr-evidence/v1.0.0; identity ICR-EVIDENCE-1.0.0. Canonical UTF-8 JSON; no SQLite needed for this graph size. Original stable IDs and epistemic labels retained. Graph nodes/edges consolidated; complete comparison, within-ICR, QA, bridge and challenge registers retained separately. Federal package includes all 73 models, benchmark, claims, sources, assumption methods, and frozen 27-entity model dictionary. Public source URLs and excerpt provenance retained; complete binary publications excluded.

Portable contracts expose graph projections and canonical analytical registers explicitly. Indexes point to canonical file/JSON pointers; working paths are supplemental provenance only. Missing values remain missing. Same labels and index membership do not establish comparability. The six unresolved task/method comparisons remain distinct from within-ICR and general research questions.

Authoritative counts: 90 recent packages; 48 control histories; 135 versions including lineage; 468 principal activity representations plus 25 assumption-context nodes; 162 assumptions; 341 checks; 32 comparisons (15 consistent, 8 explained, 3 not comparable, 6 unresolved); eight within-ICR findings (7 potentially inconsistent, 1 unresolved). No combined portfolio inconsistency rate.

Validation: source byte fingerprints; JSON Schemas; relationships; graph and claim/source resolution; register equivalence; count reconciliation; full inventory SHA-256; offline release-only consumer and acceptance queries. A browser-compatible dependency-free JS consumer/validator and optional Node CLI will accompany JSON. Build-time Python standard library is allowed but not required to consume evidence. External manifest digest and freeze receipt avoid circular self-hashing and release-commit self-reference.

Checkpoints: A architecture; B datasets/contracts; C indexes/snapshot/manifest; D validation; E release-only acceptance, ZIP and immutable freeze with Loop 5.2 handoff. Only release/ and loop-5/ paths may be added or edited.
