# ICR Tool PR 2 — portable evidence identity handoff

ICR_TOOL_PR_02_STATUS = OPEN_FOR_REVIEW

Recorded 2026-09-10.

| Field | Value |
|---|---|
| Implementation repository | Jpatel3333/icr-tool |
| PR | #2 |
| URL | https://github.com/Jpatel3333/icr-tool/pull/2 |
| Title | Add portable evidence bindings and verified release pins |
| Relationship | Stacked on open, unmerged PR #1 |
| Target branch | fix/lossless-draft-roundtrip |
| Exact base SHA | 5021df7d109950ab17b7717cc7c0839adaf51007 |
| Feature branch | feat/portable-evidence-provenance |
| Exact pushed head SHA | eeec878528da4ee1e04b24ee600ef5343aa6c3a5 |
| Current implementation main | e72fae4b1d2a37d7a22aeb8ab5b3555f423af79e |
| Benchmark start SHA | 572e1999cdb49bbffac1ab4896393e11f043a78a |
| Disposition | Open, unmerged; auto-merge null; not self-approved |

PR #1 was inspected through the live GitHub API after fetching origin before coding,
at validation, and immediately before opening PR #2. It remained open/unmerged with
head 5021df7 and base e72fae4. PR #2 therefore branches from and targets PR #1 rather
than main. Once PR #1 merges, retarget to main and revalidate. Neither PR was merged.
No CI or automated-review polling followed creation; one metadata read confirmed the
created PR's target, exact SHAs and unmerged state.

Both working trees were clean at start. No legitimate local work was overwritten.
The implementation is one focused commit. No application code is copied into this
handoff, and frozen evidence remains unchanged.

## Start-state model and fresh defect reproduction

DraftProject schema was version 1. Sourced inputs carried a finite value plus positive
local integer sourceId, optional locator/rawQuote, or explicit UNVERIFIED/note. SQLite
IDs were local primary keys, not external identities. JSON preserved supported fields
after PR #1; ordinary unknown keys were stripped by Zod and future versions rejected.
Existing imports/vintage operations remained mutable local context. Markdown/XLSX
used local citation mappings, with previously recorded provenance/output limitations.

Freshly read the actual INSERT INTO sources SQL from exact base 5021df7 via git show.
Executed it against two disposable SQLite backups of data/icr.db: ID 8 named Source
Alpha in A and Source Beta in B. SELECT by the same integer returned different names.
The authoritative database stayed byte-identical. The new automated test independently
recreates a collision using two in-memory SQLite contexts and proves a serialized
external binding resolves identically through independently loaded pinned releases.
Working value 777 stays 777; both synthetic local source tables retain one row.

## Contract and schema decision

DraftProject schema **2** adds project-level `evidenceBindings`. All valid v1 projects
load through migration, preserving their supported value model/defaults; all new saves
use v2, including projects without evidence. Old readers reject version 2 rather than
silently stripping evidence. V1 envelopes already carrying evidenceBindings reject as
mislabeled, and unsupported future/nonnumeric versions reject. Strict evidence schemas
do not change existing ordinary unknown-key behavior elsewhere in the value model.

Binding envelope version 1 includes:

- relation `historical-evidence`;
- release ID, version, schema version and exact externally trusted manifest SHA-256;
- explicit evidence kind and existing producer stable string ID;
- full hydrated record snapshot and discovered source citation records.

Supported typed references cover source, activity, assumption, claim, quantitative
check, comparison, within-ICR finding, analysis finding and bridge. Kinds select fixed
canonical datasets; activity/assumption resolution validates declared node type.
Comparisons/findings use complete registers rather than graph projections. Qualified
index addresses are retrieval addresses, not invented identities.

The attachment point is intentionally the project. This PR does not assign historical
evidence to individual numeric inputs through an adoption policy. Working sourced or
UNVERIFIED inputs remain independent. Evidence bindings do not satisfy numeric sourcing
requirements, approve applicability, or change calculations. **Historical evidence is
evidence of prior practice, not automatic approval of a current ICR value or TSA default.**

Snapshots preserve absent/null/zero, original and normalized values, locators, quotes,
units, periods and epistemic labels as supplied. Full source original metadata is kept.
Source discovery follows source_id/source_ids inside hydrated records; no unrestricted
transitive graph walk is implied. Numeric SQLite sourceId remains a legitimate internal
identity, with no external fallback, overloading, promotion or import.

## Read-only adapter

Host-independent `loadVerifiedRelease` receives `readBytes(relativePath)` and actual
`listPaths()` plus a required trusted pin. It wraps the unchanged producer consumer:
exact manifest bytes/hash → supported identity/schema → all inventoried hashes/lengths
→ declared JSON/schema checks → references/IDs, graph/index/count reconciliation and
producer bridge integrity checks → queryable release. No unpinned success path exists.
Hash pinning establishes expected content integrity, not publisher authentication.

The supplied runtime is explicitly intended for application inclusion in the producer
README/handoff. Its exact source is frozen commit
007abaf03e7bd950b2e8133ebd299c9f8b2f89de,
release/icr-evidence/v1.0.0/runtime/consumer.mjs, SHA-256
1b0f4267105ca8f63b1311e13bf243bf3a46f77d014b764d74e56d16ea3b931e.
The application records this origin and inclusion intent. Ten format-only schemas
support synthetic fixtures; no substantive corpus/research/report is copied. No blanket
license for the corpus is inferred from runtime inclusion instructions.

The wrapper requires actual enumeration and filters only FREEZE-RECEIPT.json and
validation/final-acceptance-gate.json per the authoritative receipt. Those administrative
files are not trusted evidence. All other extras reject. Paths reject absolute paths,
dot segments, backslashes, colons and control characters before host reads. Filesystem
hosts must additionally reject symlinks, including root ancestors; the optional Node
validation script implements that boundary.

Internal producer data is not exposed. Bytes are copied on ingress, results defensively
cloned and the pin frozen. No release writes, SQLite ingestion/cache, network retrieval,
HTML rendering, formula/script execution or arbitrary SQL/expression query exists.
Exact-facet queries intersect allowed fields, bound limits 1–100 and page by qualified
key. Producer bridge checks validate release integrity only, not project calculations.

Resolution statuses distinguish release-unavailable, release-mismatch, object-missing,
integrity-failure, snapshot-mismatch and verified. Snapshot comparison ignores object
key order but preserves arrays. A mismatch returns resolved data separately without
overwriting stored provenance or working values. Unavailable release leaves the saved
snapshot inspectable and unverified. Different content pins cannot silently supersede
the original. Only producer release/schema 1.0.0 is supported today.

## Files changed in icr-tool

- app/src/lib/model/draft.ts
- app/src/lib/model/draft-workflow.test.ts
- app/src/lib/evidence/contract.ts
- app/src/lib/evidence/release.ts
- app/src/lib/evidence/release.test.ts
- app/src/lib/evidence/fixtures/release.ts
- app/src/lib/evidence/fixtures/schemas.json
- app/src/lib/evidence/vendor/consumer.mjs
- app/src/lib/evidence/vendor/consumer.d.mts
- app/src/lib/evidence/README.md
- app/scripts/validate-evidence.mjs
- docs/validation/portable-evidence.md

12 files; 1,256 insertions, 3 deletions relative to PR #1. No calculation, export,
database, lockfile, dependency or Tauri host file changed.

## Synthetic and regression validation

32 new passing cases: 30 evidence cases and 2 schema/workflow cases. They cover trusted
pin, modified manifest/artifact, malformed manifest and inventoried JSON, missing/extra
files, administrative exclusions, unsupported identity/version/schema, contract failure,
unresolved reference, duplicate identity, inconsistent counts, unsupported schema keyword,
unsafe paths, source/non-source distinction, hydration, bounded query/pagination,
null/absent/zero, mutation isolation, unavailable/missing/mismatched release/object,
snapshot drift, SQLite collision independence and no silent upgrade. The A/B test uses
changed content/digests within the supported format; unsupported versions reject separately.

The 13 PR #1 tests remain intact and pass. New workflow coverage executes the actual
Draft page load/build/save/reload functions with deterministic host I/O, then edits an
unrelated title, saves again and checks binding equality and mutation isolation. V1
migration retains supported values and future/mislabeled versions reject. This is
programmatic form/persistence validation, not Svelte DOM or Tauri IPC execution.

| Command (from app except Git) | Exact final result |
|---|---|
| npx vitest run src/lib/evidence src/lib/model src/lib/calc/regressions.test.ts src/lib/cite | 66 passed; 4 suites passed |
| npx vitest run | Exit 1: 134 passed, 2 existing skips; 13 suites passed, 1 suite failed at import |
| npm run check | Exit 0; 0 errors, 0 warnings |
| npm run build | Exit 0; static frontend built; existing annotation/chunk-size warnings remain |
| git diff --check; staged check; full base-to-head check | Passed |
| node scripts/validate-evidence.mjs RELEASE_ROOT TRUSTED_MANIFEST_SHA256 | PASS, repeated at final gate |

Linux Node v24.21.0. The full-suite failure is the same pre-existing
review/golden.test.ts missing absolute Windows Markdown fixture disclosed in PR #1.
Its six tests never register; no tests were hidden, disabled or replaced. PR #1 reported
102 passed / 2 skipped with this same failed suite. The full suite is not claimed green.
Windows/Tauri/WebView2 integration remains pending; no Rust/system packages installed.

## Real frozen release validation

Release: **ICR-EVIDENCE-1.0.0**.

Expected manifest SHA-256:
572e8a414c5867e75a5d24eb4d5e939a475969c92bb1d81b3f183f436b4663a9.

Frozen release commit: 007abaf03e7bd950b2e8133ebd299c9f8b2f89de.

Verified load and all bindings passed. Actual bounded queries selected:

| Kind | Stable ID | Hydrated provenance count |
|---|---|---|
| Source | SRC-0001 | 0; source citation metadata itself retained |
| Activity | ACT-003fd285cdd9afb8df | 1 |
| Assumption | ASSUM-0242ee150af09a5ce8 | 1 |
| Quantitative check | QA-CYBER-COST | 1 |
| Comparison | CMP-01 | 3 |
| Within-ICR finding | FIND-CYBER-COST | 3 |

Limit 101 rejected. All **90 directory files** (88 canonical + 2 administrative)
retained identical hashes. Corpus source rows stayed **7 → 7**. Database SHA-256 stayed
5a3c2bdb5b824b88f10fe21f23da5889fccf20944ca34977e6f9489e506ae50d.
No canonical release or local database mutation occurred. The committed automated suite
is self-contained and does not depend on the sibling release path. The optional script
accepts root/hash arguments and requires the existing development tools plus node:sqlite.

## Compatibility, limitations and deferred work

V1 loads, but newly saved v2 files require the new reader. Existing local sources,
SQLite schema, numeric sourcing, arithmetic formulas and Markdown/XLSX implementations
are unchanged. These project-level bindings are not yet included in Markdown/XLSX
exports. Existing local-only citations remain database-relative. No host integration
or additional approved-assumption behavior is claimed.

Inspected the full delta for portable identity ambiguity, missing trust pins, silent
updates, artifact tamper, unsafe paths, object aliasing, type confusion, null/zero,
snapshot drift, old-reader stripping and working-value mutation. No frozen corpus,
benchmark research/report, absolute machine path or credentials were added to icr-tool.
Only the authorized feature branch was pushed; main was not pushed or merged.

Deferred: quantitative/model-output reconciliation (planned PR 3), growth/dollar-year
export semantics, Item 13/output fixes, XLSX Sources completeness, XCOMP, Item 15 project
bridge, Items 12–15 redesign, Evidence Explorer/graph UI, input-specific evidence
adoption, carry/adapt/replace, analyst approval/applicability, AI/DHSChat and TSA-local
overlays. Future planned work is not implied approval. PR 3 has not begun.

This handoff's commit SHA is discoverable from Git history and reported separately,
because a commit cannot embed its own hash. Benchmark push target is origin/main.
