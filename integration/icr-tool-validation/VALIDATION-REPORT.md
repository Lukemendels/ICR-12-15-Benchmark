# ICR Tool executed baseline and integration readiness

## Executive Summary

**ICR_TOOL_VALIDATION_STATUS = COMPLETE.** The validation mission completed; the application does not have an all-green acceptance result.

`icr-tool` installs with its existing npm lockfile, passes Svelte/TypeScript checks, and produces the static frontend build on Linux. The first install hit a read-only default npm cache; using `/tmp` resolved it without changing dependencies. The existing test command fails: **11 suites pass, one suite fails to load; 89 tests pass and two skip**. Six golden-review tests never register because their fixture uses an absolute path on Jay's Windows machine. One of the 89 passing tests returns without assertions because its external workbook is missing.

The simple draft, calculation, save/reload, Markdown, XLSX, source-vintage update, corpus search, review, and review-save paths execute programmatically. These runs use real application functions with host I/O replaced by local files and SQLite on disposable copies. They are not desktop UI tests. Rust/Cargo are absent, as are Linux GTK3/WebKit2GTK development metadata; backend/host compilation and executable behavior remain unvalidated. Windows deployment remains pending.

Execution confirms all seven material comparison concerns. Rich drafts lose data through the form, growth and dollar conversion do not drive exports, Item 13 includes respondent labor, source IDs alone count as sourced, independent local source IDs collide, review context mislabels a current ECEC value as a corpus mode, and Item 15 has parsing but no bridge engine. XLSX also omits sources used only for Federal/other costs from its Sources sheet.

**Retain icr-tool as the leading production-shell candidate, conditionally.** Its portable engines and frontend build are useful foundations to extend. Its current draft model/form/export contract is not safe as the working ICR authority. Resolve lossless persistence, portable evidence identity, and output semantics before adopting benchmark evidence into drafts. No fixes or integration were implemented.

## Exact Validation Baseline

| Field | Captured value |
|---|---|
| icr-tool origin | `https://github.com/Jpatel3333/icr-tool.git` |
| icr-tool commit | `e72fae4b1d2a37d7a22aeb8ab5b3555f423af79e` |
| benchmark origin | `https://github.com/Lukemendels/ICR-12-15-Benchmark.git` |
| benchmark commit used | `61879d1b8c017d71c1dd9ec382d3d8972a40621e` |
| Branches / initial status | Both `main`; both clean |
| Platform | Linux Mint 22.2, x86_64; kernel `7.0.0-31-generic` |
| Node / npm | `v24.21.0` / `11.19.0` |
| Rust / Cargo | Both absent from PATH; no `~/.cargo/bin` or `~/.rustup` found |
| Python | `3.12.3` |
| Install | `npm ci --cache /tmp/icr-validation-npm-cache`, in `icr-tool/app` |
| Date | 2026-09-10 |

No pull or target revision change occurred. Manifests, both lockfiles, README, CLAUDE.md, Vite/Svelte configuration, Cargo build script and Tauri configuration were inspected before installation. SHA-256 receipts for both lockfiles and the tracked database are in [validation-state.json](validation-state.json). The previous comparison report, evidence log and state were read and reused. Benchmark semantic comparisons below use existing `methodology/requirements-floor.md`, `canonical-model.md` and `canonical-data-dictionary.md`; no new policy research was conducted.

## Dependency Installation

The repository declares Node 20+, stable Rust and Windows MSVC/WebView2 prerequisites. npm installed 255 packages and audited 256 in six reported seconds using the lockfile. The original `npm ci` exited 226 with `EROFS` under `~/.npm/_cacache`; extraction/cleanup warnings accompanied that failed attempt. A normal `npm ci` retry with a writable temporary cache succeeded. Neither tracked lockfile changed.

npm reports deprecated transitive packages and five audit entries: three low and two moderate, arising from cookie/SvelteKit and uuid/ExcelJS chains. These are audit results, not five independently demonstrated application exploits. The advisory output is retained; reachability was not assessed. No audit fixes, upgrades or lockfile regeneration were attempted. npm also reports esbuild's postinstall outside its allowScripts policy; the supplied platform binary nevertheless executes both builds and the diagnostic harness successfully.

Cargo fetch/check/test commands were attempted with `--locked`; all stop at missing Cargo. No crate resolution or Rust compilation is claimed. No system packages, Rust toolchain, global npm tooling or application dependencies were added.

## Test Results

See [test-results.md](test-results.md), [commands.jsonl](commands.jsonl) and bounded [logs](logs/).

- Existing Vitest: 12 discovered files; 11 pass, one fails during module import. 89 tests pass, two explicitly skip, six golden tests cannot register. Of the 89, one import test exits without assertions. Thus 88 reported passes execute assertion bodies; this is not a count of individual assertions.
- `npm run check`: zero errors, zero warnings; covers repository-configured Svelte/TypeScript checking.
- Existing Gate 4 passes. A diagnostic replay of its unchanged fixture declarations confirms **13/13 seeded defects detected**, score 50 and auto-fail. The suite's threshold is only 12/13.
- Existing Markdown export-to-review tests pass; their name does not establish UI or JSON roundtrip fidelity.
- No lint script/configuration, separate schema test command, browser test framework or Rust test modules were found. Schema/calc/review tests are included in Vitest. Watch and development commands are not separate quality gates.

## Build Results

| Layer | Status | Evidence / limitation |
|---|---|---|
| npm dependency install | PASS | Writable-cache retry succeeds; lockfiles unchanged |
| frontend unit tests | FAIL | Missing absolute Windows golden fixture; other collected cases as above |
| frontend type/Svelte checks | PASS | 0 errors, 0 warnings |
| frontend production build | PASS | Vite/static adapter writes `app/build`; command 20.188 seconds |
| Cargo dependency resolution | PLATFORM_BLOCKED | Cargo absent; `cargo fetch --locked` cannot start |
| Cargo check | PLATFORM_BLOCKED | Cargo absent |
| Cargo tests | PLATFORM_BLOCKED | Cargo absent; no repository Rust unit tests found |
| Tauri host build | PLATFORM_BLOCKED | `cargo metadata` cannot start, including `--no-bundle` attempt |
| Linux executable/run | PLATFORM_BLOCKED | No host binary built; GTK3/WebKit2GTK development entries absent |
| Windows NSIS packaging | PLATFORM_BLOCKED | Linux environment; Windows deployment pending |
| database integrity | PASS | Read-only integrity `ok`, no FK violations, user_version 1 |
| representative draft workflow | PARTIAL | Underlying page functions save/load simple data; rich fields lost; no DOM/IPC |
| representative review workflow | PARTIAL | Engine, page context and audit SQL execute; host/reload UI untested |
| Markdown export | PARTIAL | Generated and parsed; growth, Item 13 and provenance limitations |
| XLSX export | PARTIAL | Generated and reopened; cells verified; semantics/provenance limitations |

Build warnings are not compilation failures: two Zod comment annotations are removed, the largest minified chunk is about 940 kB, and the first build sees the generated `.svelte-kit/tsconfig.json` absent at startup. Check/build were launched concurrently on a fresh dependency state, so that initial generated-config warning cannot establish a persistent defect. Both complete successfully. No redundant build reruns were needed.

`npm run tauri build --no-bundle` initially had its flag consumed by npm and effectively attempted the documented default build. The corrected `npm run tauri -- build --no-bundle` fails at the same missing-Cargo metadata step. Neither reached Rust compilation or NSIS packaging. **WINDOWS_DEPLOYMENT_VALIDATION_PENDING** includes MSVC, Tauri/WebView2 IPC/plugins, installer, bundled resource location, device launch and update behavior.

## Capability Coverage

This inventory classifies baseline automated coverage, with fresh diagnostics identified separately. TESTED means the bounded named behavior executes assertions, not that the entire capability is production-ready.

| Capability | Existing coverage classification | What execution establishes / remaining gap |
|---|---|---|
| Respondent burden arithmetic | TESTED | Golden population × frequency × time and totals fixtures pass |
| Wage/load-factor calculation | TESTED | Multiplication and source-ID/UNVERIFIED propagation pass |
| Federal costs | PARTIALLY_TESTED | Golden/fixed cost and totals checks pass; diagnostic fixed $1,000 + labor $400 = $1,400; no host/form per-response success |
| Rounding | TESTED | Half-away ties, magnitudes, cascade and mixed-mode rejection |
| Annualization | PARTIALLY_TESTED | Projection/average helper assertions pass; export projection absent, reproduced |
| Dollar-year conversion | PARTIALLY_TESTED | Helper ratio/provenance/missing-year cases pass; export never applies it |
| Schema validation | PARTIALLY_TESTED | Hybrid provenance, dates, nonnegative inputs, unique IDs and year order; no full form preservation |
| Source handling | PARTIALLY_TESTED | Footnote numbering, unknown-ID rejection and staleness; no observation-proof guarantee |
| Source-vintage updates | NOT_TESTED | No baseline tests; diagnostic SQL insert/bulk/supersession and page adoption execute |
| Import | TEST_PRESENT_BUT_NOT_EXECUTED | Two golden workbook tests skip and rejection test returns; diagnostic synthetic OEWS/ECEC and rejection execute |
| Export overall | PARTIALLY_TESTED | Markdown only in baseline; fresh XLSX generation/reopen checks |
| Markdown generation | PARTIALLY_TESTED | Repeat output and review score pass; analytical completeness not asserted |
| XLSX generation | NOT_TESTED | No baseline suite; diagnostic checks sheet values and missing citations |
| Document parsing | PARTIALLY_TESTED | Synthetic Markdown/HTML tables and figures pass; absolute-path real-document suite cannot load; DB document reviewed separately |
| Review rules | PARTIALLY_TESTED | Rule cases and orchestration pass; optional context skipped; no baseline XCOMP-302 case |
| Seeded review defects | TESTED | Existing gate passes; diagnostic confirms all 13 seeded rule IDs |
| Draft save/load | NOT_TESTED | Diagnostic actual page functions + file adapter succeed for subset, fail fidelity for rich draft |
| UI roundtrip | NOT_TESTED | No DOM automation; extracted functions reproduce 23 field changes |
| Item 12 | PARTIALLY_TESTED | Golden hour tables and Markdown; growth, unique-population/overlap and rich-state limits |
| Item 13 | PARTIALLY_TESTED | Arithmetic fixtures pass but preserve labor-in-Q13 semantics; no canonical nonhour contract gate |
| Item 14 | PARTIALLY_TESTED | Golden and simple cost checks; richer allocation semantics and host roundtrip absent |
| Item 15 | NOT_TESTED | No bridge assertions; diagnostic identifies section/text/figures but no reconciliation |
| Corpus search | NOT_TESTED | Diagnostic real `db.ts` FTS queries return results on copied corpus |
| Database migration/update | NOT_TESTED | Vintage appends tested diagnostically; no corpus-upgrade merge implemented |
| Tauri host behavior | PLATFORM_BLOCKED | No Rust, host executable or desktop IPC validation |

## Reproduced Findings

All hypotheses, inputs, exact commands, affected files and field-level differences are in [reproduction-log.md](reproduction-log.md) and [reproduction-results.json](reproduction-results.json).

| Concern | Classification | Executed result |
|---|---|---|
| A. UI/schema roundtrip | CONFIRMED | 23 changed paths: rich fields dropped/defaulted, createdDate replaced; perResponse government cost rebuild returns null |
| B. Annualization/projection | CONFIRMED | Helper produces 100, 110, 121; Markdown averages 100,100,100; dollarYear only changes label |
| C. Item 13 semantics | CONFIRMED | Q13 shows $3,000 labor + $500 other = $3,500; capital/O&M $300 separate; empty capital array yields categorical no-cost prose |
| D. Source proof | CONFIRMED | `{value:100,sourceId:1}` accepted, zero unverified count; input locator and quote absent from export |
| E. Source portability | CONFIRMED | Source #8 is Context A in one copied DB and Context B in another; same draft exports different citations |
| F. Review context | CONFIRMED | Page-fed 1.4294 makes fixture's 1.42 FAIL as “corpus mode”; XCOMP-302 receives no counts and emits nothing |
| G. Item 15 | CONFIRMED | 100 + 20 − 10 = 999 bridge produces no Q15 finding; no baseline/change schema or Q15 export |

Two prior impressions require refinement. “Roundtrip tests” prove Markdown export-to-review compatibility, not lossless editing. Item 15 parsing does preserve heading/text and recognizes quantities, but the diagnostic tokenizer reads `-10 hours` as positive 10; it does not encode the sign or causal role as a bridge component. The architecture recommendation survives, while any interpretation of “working” as verified desktop readiness is explicitly withdrawn.

Additional bounded finding: `export/xlsx.ts` collects Sources-sheet IDs from activity count/time/wage, frozen parameters and capital costs, but excludes IDs used only by Federal costs or activity other-cost inputs. Diagnostic source #8 appears in a Federal row's name but has no Sources-sheet record. Worksheet cells are values rather than Excel formulas. No byte-identical XLSX archive claim is made.

## End-to-End Workflow Results

### Draft, calculation and exports

A validated fixture contains 100 respondents × 2 responses × 30 minutes = 100 hours; wage $20 × factor 1.5 = $30/hour; labor $3,000; other cost $5 × 100 = $500. Federal fixed $1,000 plus 10 hours × $40 = $400 yields $1,400. Both exports reproduce these base calculations. XLSX is reopened with the already-declared ExcelJS dependency and its five sheet contents are retained as JSON.

The actual page `loadProject`, `buildProject`, `saveProject`, and export functions execute against temporary files. A pure parse→JSON→parse roundtrip preserves all supported fixture fields, isolating the loss to the form conversion. The form keeps basic values, respondent locators and series references; it drops growth, notes, frozen parameters, capital costs, narrative text, wage SOC, all raw quotes, and government locators. `createdDate` becomes the current date. A per-response Federal item loads as an empty fixed item and blocks subsequent rebuild/save.

A newer vintage changes the fixture wage from 20 to 25 only when the explicit propagation action is applied; the saved/reloaded subset exports $3,750 labor. File writes work through adapters, not real Tauri dialogs or filesystem permissions. This is a partial workflow result, not a full GUI result.

### Review and persistence

The page's actual `runReview` uses the copied corpus query and reviews `MINI_SS`: score 98, excellent, 26 findings, with the 1.42-versus-1.4294 discrepancy. `persistRun` stores one review row and all 26 findings; SQL readback succeeds. The baseline screen exposes audit saving, but no review-run reload UI/API is implemented. Passports are generated but this save API stores findings, not passport objects.

The unchanged Gate 4 fixture declarations reproduce 13/13 seeded defects, score 50, auto-fail. A separate review of SQLite `sectionsFor('1652-0001')` assembles 18 sections, produces 43 findings and 24 passports, score 62 and auto-fail. That is a review output, not a harness failure or an official judgment on the source document; it does not replace or satisfy the missing golden-file suite.

### Sources, database and updates

Read-only `integrity_check=ok`, zero `foreign_key_check` rows, `user_version=1`. The corpus retains 59 ICRs, 473 documents, 928 sections, 348 burden records, 321 extracted tables, seven sources and 4,479 reference rows. Series comprise 2,640 OEWS rows (1,320 each for 2023/2024), 140 ECEC rows (2026) and 1,699 enplanement rows (2024). Source locators, review runs/findings, passports and edit-log tables start empty.

Schema and index definitions are captured in JSON. There is one explicit catalog index entry, SQLite's automatic primary-key index for ICRs; FTS virtual/shadow tables supply text indexing. No standalone application secondary indexes were found. This is not a performance benchmark.

Actual `db.ts` queries through a Node SQLite adapter return 59 ICRs, two wage source-search results, 60 capped burden-section hits and the active management wage $68.15. Copies receive source inserts, series inserts and bulk vintage import, supersession and edit logs. Old value 20 remains in row 4480 linked to newer row 4481 (25). The page detects and adopts the new vintage; the stored reference retains kind/key1/vintage/year and puts the row's quote into `locator`, not `rawQuote`.

A diagnostic fixture initially used undeclared `series_kind='fixture_wage'`; the database correctly rejected it. The harness was corrected to the declared `other` kind. That was a harness setup error, not an application failure.

First-launch copying is **not executed**: `ensure_db` requires the unavailable Tauri host. Inspection confirms copy-if-target-absent and no merge when a target exists. Disposable copies in this mission validate SQL behavior only, not resource resolution or first-launch initialization. Corpus upgrades, partial-copy recovery and preservation of local edits across installer upgrades remain untested. No tracked database byte changed.

## Integration Readiness

**Production shell:** extend rather than replace remains justified by the passing portable arithmetic/review cases, frontend checks/build and exercised programmatic workflows. This is a candidate selection, conditional on host/device deployment testing, not production certification.

**Draft authority:** not ready. Define a versioned supported subset, preserve its fields across editing, reject or preserve unsupported fields explicitly, keep creation identity stable, and support/reject per-response Federal items before allowing them into editable projects. Unknown top-level fields are currently stripped by schema parsing; new evidence fields cannot simply be appended to draft JSON.

**Evidence dependency:** a future adapter should load exact `ICR-EVIDENCE-1.0.0` as a separately verified read-only dependency using its pinned trusted manifest hash, inventory/schema/reference checks and existing consumer. Preserve public frozen evidence, TSA-local decisions and mutable projects as separate authorities. Retain release ID, manifest hash and limitations; reject tampered/wrong releases; do not migrate the public graph into the mutable corpus. No adapter or acceptance test was implemented here.

**Source identity:** define stable namespaced source and observation IDs plus release identity, locator, original value/unit/period, quote and any transformation/adoption decision. Local SQL integer keys may remain internal, with explicit resolution/remapping and missing-source errors. Drafts must retain the adopted vintage rather than silently changing with the database. Current IDs and citation names cannot provide that contract.

**Outputs:** Item 12 base arithmetic is useful but multi-year/overlap semantics are partial. Item 13 is not reliable under the benchmark's canonical nonhour distinction: the output's own exclusion wording conflicts with its labor table. Item 14 simple arithmetic works, but form fidelity and richer allocations remain partial. Item 15 bridge and draft generation are not implemented. Resolve output contracts before using these exports as evidence-backed analytical results.

**Validation gate:** reuse rounding, schema, burden/gov golden cases, citation handling, seeded defects, parsing and deterministic Markdown tests after supplying portable fixtures. Add supported-field form persistence, growth-aware output, dollar-year policy, source portability/proof, source-sheet completeness, Item 13 contract, migration and real host acceptance. Existing test scores are not a substitute for those checks.

**Host:** Linux validates the portable code and frontend build here. Rust/backend compilation, Tauri plugins/resources/permissions and launch are unvalidated. Windows NSIS/WebView2/install-update/device testing remains a separate required deployment gate.

## Recommended Pre-Integration Fixes

Priorities refer to adopting evidence into working drafts, not to preventing read-only evidence exploration.

| Priority | Issue / minimum acceptance condition |
|---|---|
| BLOCKER | Preserve every supported project/provenance field through form save/load; explicitly reject unsupported variants before editing instead of losing data |
| BLOCKER | Portable source/observation identity and release pin; same draft must not silently resolve to another local source |
| HIGH | Reconcile Item 12 labor versus Item 13 nonhour output, combined/subtotals, and unknown-versus-zero statements |
| HIGH | Apply supported growth/projection and dollar conversion in output, or clearly disallow/label unsupported semantics |
| HIGH | Preserve input-level locators/quotes and include all used sources in both export formats |
| HIGH | Make golden-review fixture portable and import coverage honest; restore a reproducible Linux acceptance gate |
| MEDIUM | Fix XCOMP context contracts; actual corpus statistics or accurately labeled reference comparison; explicit unavailable-context coverage |
| MEDIUM | Define and test corpus upgrade/migration while preserving local sources and reviews; execute first-copy behavior on host |
| MEDIUM | Explicit Item 15 scope decision; implement a bridge only if required for the chosen authoring scope; heading recognition must not imply validation |
| MEDIUM | Triage npm audit reachability and supported updates in a separate dependency task; no forced fixes |
| LOW | Evaluate bundle size and query indexes with measured startup/search workloads; no performance defect established here |

Host deployment validation is a release gate; missing local system tooling is not a product defect to fix through application changes.

## Open Questions

Technical: Where is the exact external golden Markdown fixture and offline DB build pipeline? What DB update/version strategy preserves local edits? How should series key2 and same-year corrections be represented in portable references? What Tauri/Windows device and upgrade environments are available? Are missing-source and UNVERIFIED disclosures equivalent across formats? No broad additional execution would answer these from this environment.

Product/owner decisions for Jay and Luke: Which draft fields/Items are promised in the first supported release? Who approves Item 13 semantics and dollar-year/growth policy? Is Item 15 required before evidence browsing or only before full authoring? Who owns immutable-release publication/trust, source licensing, local adoption decisions and TSA-local restrictions? Which desktop host is institutionally supported?

## Closeout

Only `integration/icr-tool-validation/` is changed in the benchmark repository. icr-tool HEAD, tracked files, lockfiles and database remain at baseline; only ignored node_modules, `.svelte-kit` and build outputs remain. No commit or push was made to icr-tool. Frozen evidence and prior comparison artifacts are unchanged. Final benchmark commit is discoverable via `git log -1 --format=%H -- integration/icr-tool-validation`; its SHA is supplied in the final response because a commit cannot embed its own hash. Push target is benchmark `origin/main`; no CI polling is part of closeout.
