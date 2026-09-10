# ICR Tool PR 1 — persistence handoff

ICR_TOOL_PR_01_STATUS = OPEN_FOR_REVIEW

Recorded: 2026-09-10.

| Field | Value |
|---|---|
| Implementation repository | Jpatel3333/icr-tool |
| PR | #1 |
| URL | https://github.com/Jpatel3333/icr-tool/pull/1 |
| Title | Preserve DraftProject data across Draft form roundtrips |
| Target | main |
| Exact base SHA | e72fae4b1d2a37d7a22aeb8ab5b3555f423af79e |
| Feature branch | fix/lossless-draft-roundtrip |
| Exact pushed head SHA | 5021df7d109950ab17b7717cc7c0839adaf51007 |
| Disposition | Open for review; not merged or approved; auto-merge not enabled |

## Recovery and base

Recovered the partial session's clean branch with two already-pushed commits, 9fec139 and 2c10c7a, and no PR. Inspected and retained sound production changes. Added a follow-up commit for targeted assertions, mutation-isolation/preview checks, a smaller application-local synthetic fixture, and concise validation documentation. Removed the copied diagnostic JSON and raw terminal log from the final diff. Published history was not rewritten.

Origin was fetched during recovery and immediately before PR creation. Main remained at the prior validated SHA, with no intervening upstream commits. The branch merge base equals the recorded base. The feature branch alone was pushed to the implementation repository; remote head SHA was verified.

Supporting validation and table-checker reviews were read and reused. No table-checker code was migrated, no benchmark dependency was introduced, and no frozen evidence was modified.

## Core invariant and implementation

For every field and variant supported by the current DraftProject schema, load into the Draft workflow followed by no-edit build/save preserves semantically meaningful supported state. Editing one exposed field must preserve unrelated supported fields.

Root cause: the form represented only a subset of DraftProject, and build reconstructed a fresh project from that subset. Omitted supported fields received defaults or disappeared. Creation date was regenerated on every build. Per-response Federal costs loaded as blank fixed rows.

The Draft page retains the validated project and each row's original supported payload, then overlays editable form fields. This preserves growth, notes, wage/SOC/series data, raw quotes and locators, frozen parameters, capital costs, narratives and creation date. Row removal/reordering operates on row-owned retained data. Zod validates and clones built results; output mutation does not change retained nested state.

Fixed and labor Federal inputs remain editable with provenance preserved. Loaded per-response inputs remain visibly read-only and retain their discriminator and payload; names/removal remain editable. Their preview uses the existing Federal calculator. Incomplete nonempty optional costs block saving; deliberate removal remains possible.

Numeric edits retain existing source bindings. Changing source ID or locator drops the old hidden quote; switching to UNVERIFIED removes sourced proof. Exact schema-valid notes, including whitespace, survive. This does not create a new source-proof policy.

## Files changed in the PR

Paths relative to icr-tool:

- app/src/routes/draft/+page.svelte
- app/src/lib/model/draft-workflow.test.ts
- app/src/lib/model/fixtures/rich-draft.ts
- docs/validation/draft-roundtrip.md

No implementation code is copied into this handoff.

## Regression coverage

Thirteen tests cover schema serialization versus actual Draft conversion; rich no-edit and repeated save/reload; unrelated name/title and numeric/Federal edits; explicit date, growth, notes, SOC/wage/series and provenance assertions; frozen parameters; startup/O&M costs; narratives; all Federal variants; minimal optional fields and zero/whitespace values; source replacement and UNVERIFIED conversion; optional-cost clearing/incomplete-edit rejection; row deletion/reordering; invalid/successive loads; actual Federal preview; and isolation of returned nested objects from subsequent builds.

The repository-contained fixture is synthetic, has no machine-specific path, and requires no database records or benchmark data. The harness extracts actual production page function declarations, state initializers and derived expressions using declared TypeScript tooling. It supplies host I/O adapters and evaluates derived expressions on demand. It does not execute Svelte DOM/reactivity or Tauri IPC.

## Exact validation results

Linux, Node v24.21.0. Commands run from the implementation repository's app directory, or that directory in a detached exact-base worktree as indicated.

| Command / checkout | Outcome |
|---|---|
| npx vitest run src/lib/model/draft-workflow.test.ts — exact base with final tests/fixture added | 1 schema control passed; 12 workflow assertions failed; failures were behavioral assertions, not harness/import errors |
| npx vitest run src/lib/model/draft-workflow.test.ts — feature branch | 13 passed |
| npx vitest run src/lib/model/draft-workflow.test.ts src/lib/calc/regressions.test.ts — final feature state | 29 passed, 2 suites passed |
| npx vitest run src/lib — pristine exact base | 89 passed, 2 skipped; 11 suites passed, 1 suite failed at import |
| npx vitest run src/lib — final feature state | 102 passed, 2 skipped; 12 suites passed, 1 suite failed at import |
| npm run check — final feature state | Passed: 0 errors, 0 warnings |
| npm run build — final feature state | Passed: static frontend produced; existing annotation/chunk-size warnings remain |
| git diff origin/main...HEAD --check | Passed |

The existing review/golden.test.ts imports an absent absolute Windows Markdown fixture, so its six tests never register. This failure was freshly reproduced on the exact base and remains unrelated to this PR. No existing test was concealed, disabled or replaced with invented evidence. All new tests pass. The existing two import skips remain.

Windows/Tauri/WebView2 integration remains pending. No OS/Rust tooling was installed and no desktop-host execution is claimed. No post-creation CI/review polling was performed.

## Compatibility

DraftProject schema/version (1), existing JSON validity, unknown/future-field policy, calculation formulas, Markdown/XLSX export implementations, database schema/behavior, dependencies and lockfiles are unchanged. Unknown keys retain existing Zod behavior; unsupported schema versions are rejected. This is not a future-schema interchange promise.

Retained data can now reach existing exporters instead of disappearing in form conversion. Per-response values now reach the existing preview formula. These are persistence/coverage corrections, not methodology changes. No Tauri host implementation changed.

## Explicitly deferred

Portable evidence/source identities; evidence ingestion and benchmark adapters; source-proof contract; annualization/export projection; dollar-year semantics; Item 13 boundary; XLSX Sources completeness; XCOMP context; Item 15 reconciliation; table/narrative reconciliation; table-checker parsing; AI/DHSChat integration.

The PR establishes a persistence foundation before richer institutional evidence is attached to working projects. It does not imply approval of a future evidence architecture. PR 2 has not begun. Jay/human or automated review is the next action; the PR remains unmerged.
