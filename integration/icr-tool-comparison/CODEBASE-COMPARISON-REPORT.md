# Codebase comparison and integration assessment

Assessment date: 2026-09-10. **COMPARISON_STATUS = SATURATED.**

## Executive Summary

**Retain separate repositories. Make the portable evidence release a read-only dependency of icr-tool before considering shared application code.** This is an architectural recommendation, not implemented integration.

icr-tool is an offline desktop application with working draft forms, deterministic burden/cost functions, Markdown and Excel output, document review, source-vintage management and corpus search. The benchmark repository is a research and institutional-evidence system with completed federal and TSA analysis, a verified portable JSON release, and a browser/Anvil evidence-inspection foundation. Its calculation and production-review workbench modules are still placeholders. [E01–E06, E14]

They overlap in source discovery, arithmetic checks and the intended drafting/review journey. Their strongest implemented capabilities occupy different layers: icr-tool creates and checks draft estimates; the benchmark explains where assumptions came from, which historical tasks are comparable, what remains unresolved, and how published numbers reconcile. Neither supersedes the other as a whole. [E07–E14]

Both can operate offline using JavaScript and local assets, so the evidence consumer is technically compatible with the application without a service or repository merge. Compatibility is not semantic equivalence: SQLite source IDs, draft inputs and rule scores cannot stand in for immutable evidence identities, assumption applicability or adjudications. icr-tool also has consequential gaps between its schema, UI and export behavior. Those need a separate implementation gate before rich model interchange or calculation reuse. [E03, E07–E09, E11–E14, E19, E21]

## Inspection basis and repository identities

| Repository | Inspected full HEAD | Branch | Origin | Initial state |
|---|---|---|---|---|
| Lukemendels/ICR-12-15-Benchmark | `29af4a08f098ebd797f1449ca4fa3418afcaf10c` | main | https://github.com/Lukemendels/ICR-12-15-Benchmark.git | Clean |
| Jpatel3333/icr-tool | `e72fae4b1d2a37d7a22aeb8ab5b3555f423af79e` | main | https://github.com/Jpatel3333/icr-tool.git | Clean, newly cloned sibling |

Local paths are `~/Projects/ICR-12-15-Benchmark` and `~/Projects/icr-tool`. These are the exact code/data baselines inspected throughout. The assessment closeout commit adds only this folder and does not change either inspected application state. Its own SHA is discoverable from Git history rather than embedded circularly in its contents.

Evidence IDs refer to [evidence-log.md](evidence-log.md), whose entries distinguish code/data observation, documentation, historical test receipts, fresh execution and inference. No external research, dependency installation, application modification or source copying was performed. Architectural coverage, not file-by-file enumeration or production certification, is the scope.

## Repository Profiles

### icr-tool

`app/src/routes` owns Overview, Draft, Review, Sources and Search. Svelte 5 reactive page state drives editing and previews. `app/src/lib/calc` holds pure functions; `model/draft.ts` defines a Zod project schema; `review` parses documents and runs rules; `cite`, `export` and `import` provide footnotes, outputs and BLS workbook parsers. `db/db.ts` isolates most SQL access, though the Review route issues a context query directly. [E01–E03, E11, E15]

`app/src-tauri` provides the Rust/Tauri host, file dialogs, filesystem, SQLite and external-browser opening. `data/icr.db` is a tracked input artifact produced by a pipeline outside this repository. `docs` describes rules, usage and rounding; `CLAUDE.md` records project conventions. npm and Cargo lockfiles pin dependency resolutions; Tauri configuration packages a Windows NSIS installer. Boilerplate static assets and icons are packaging resources, not domain capabilities. No tracked CI workflow was found in `.github`. [E01, E15–E16, E22]

The application is more than a prototype shell, but the code does not establish full Items 12–15 modeling, lossless editing of every schema field, or production deployment validation. Its documented 97-test expectation is not a newly measured result in this assessment.

### Benchmark / workbench

| Area | Responsibility and maturity |
|---|---|
| Root retrieval, batch, curation and checkpoint Python scripts; `raw/`, `icrs/`, `data/`, `logs/` | Research acquisition, archives, structured extractions, sources, claims, model sections, score/check tables and historical iteration outputs. Not an application backend. |
| `methodology/`, `research/` | Frozen rubric, canonical model/dictionary, sampling and limitations, state, provenance and validation receipts. |
| `report/`, `mission-4/` | Completed federal benchmark report and TSA technical/leadership reports, with transformation scripts, figures, tables and audit records. |
| `mission-3/`, `evidence-graph/`, `analysis/` | Archived TSA statements and lineage, graph nodes/edges, reviewed assumptions, comparison/reconstruction registers, quantitative checks, challenges and open questions. Completed frozen research. |
| `loop-5/` | Portable-release assembly, source auditing, clean-load verification and freeze state. Packaging infrastructure, not a scenario calculator. |
| `release/icr-evidence/v1.0.0/` | Canonical portable evidence product: JSON, schemas, indexes, provenance, contracts, runtime consumer and validation receipts. |
| `icr-workbench/src`, `assets/foundation`, `tests` | Working evidence shell, verified loader/provider, independent state envelopes and build/acceptance tools. Modeling/review remain reserved modules. |
| `icr-workbench/assets/anvil`, `governed-library/` | Pinned Anvil compiler/authoring contract and derived governed foundation capability. |
| `icr-workbench/dist` | Generated standalone HTML and Anvil transfer ZIP; modular source remains authoritative. |

This map is supported by code and final state rather than the root README, which still calls Mission 3 and the application future work. Mission 4's handoff also predates the completed leadership brief recorded in the portable report register. These are historical navigation/state descriptions, not evidence that later artifacts are absent. [E04–E06, E13, E17–E20]

## Architecture Comparison

| Boundary | icr-tool | Benchmark/workbench | Architectural meaning |
|---|---|---|---|
| Host | Tauri/Rust desktop; SvelteKit static SPA | Standalone browser HTML; Anvil-compatible source project | Preserve host independence; neither requires the other's UI framework. |
| Domain execution | TypeScript calculations and Markdown review rules | Evidence validation/query runtime; research arithmetic replay | Reuse data contracts first; their validators answer different questions. |
| State | Page-local reactive form state; explicit JSON drafts; mutable SQLite | Verified immutable public base; separate in-memory overlay and project envelopes | Do not combine evidence and working-state mutation paths. |
| Source access | SQLite integer source IDs and reference series | Stable string IDs, qualified addresses, provenance and graph edges | Requires namespaced identity/locator translation. |
| Output | Markdown and value-based XLSX | Evidence records, reports, standalone inspection package | Evidence packaging is not estimate generation. |
| Evolution | npm/Cargo/application and DB schema versions | Release/schema/component pins, manifest digests, governed capability versions | Application upgrades and evidence upgrades need independent lifecycle decisions. |

Both runtimes are local and have no implemented authentication, live model integration or application server in the inspected flows. Source URLs can open externally. Research retrieval scripts use the network, but that is a separate historical pipeline; the release consumer does not fetch source publications. [E01, E03–E05, E14–E19, E22]

## Workflow Comparison

**icr-tool drafting:** inspect corpus/source health → add sources or import a local OEWS/ECEC workbook → create activity and Federal-cost rows with source IDs or explicit unverified notes → inspect calculated previews → save/open `.icrdraft.json` → export Markdown or XLSX. Loading a draft checks selected wage/load-factor series for newer data and offers explicit adoption. A series reference is not a complete dependency graph or automatic multi-document update system. [E02–E03, E07–E09, E15]

**icr-tool review:** select a Markdown/text supporting statement and optionally a control → parse sections, tables, figures and footnotes → run 25 rules with available inventory/date/reference context → show score, findings and table-cell passports → save the run/findings to SQLite. The UI does not import PDF/DOCX for review. Parsing Item 15 headings does not implement Item 15 rules or change accounting. Passports are built in memory; `saveReviewRun` writes runs/findings, not the existing `claim_passports` table. [E10–E11, E16]

**Research workflow:** archive source documents → extract source-specific models and register claims → normalize with original values/locators retained → test arithmetic and comparability → challenge candidate findings → freeze evidence → publish analytical reports → package validated release. This is completed research infrastructure, not a process to rerun automatically whenever a draft changes. [E12–E13, E17, E20]

**Workbench workflow:** open bundled HTML → verify release before enabling navigation → choose a TSA package → page through activities, linked sources and task/method findings → inspect release identity and store status. Provider APIs expose additional exact-facet queries and typed relationships; the UI is narrower than the provider. Graph visualization, DHSChat packets, A2UI, calculations and production review are documented future boundaries. Overlay/project JSON APIs exist, but the shell offers status rather than import/edit controls, and reload clears their in-memory state. [E04, E14, E18]

## Domain Model Comparison

| Concept | icr-tool implementation | Benchmark model/evidence | Translation requirement |
|---|---|---|---|
| Collection/version | Optional control number and draft metadata; schema v1 | Collection/scenario dictionary; package/version lineage and baselines | A control number alone cannot identify an approval or evidence version. |
| Population/respondents | Numeric respondents on each activity; totals sum rows | Population unit, segment, eligibility, lifecycle, overlap | Retain person/entity/event distinctions; do not treat activity sums as unique respondents. |
| Frequency/time | Responses/respondent/year; minutes/response | Source periods, triggers, recurrence, active/elapsed/statistic boundaries where known | Convert units only when meaning is resolved; missing fields stay unknown. |
| Burden | Respondents × frequency × minutes/60 | Observed formulas and independent checks; richer model specification | Preserve source result separately from a newly calculated scenario. |
| Labor/wage | One base wage × load factor per activity; optional SOC | Role/NAICS/locality/statistic/vintage; multiple compensation denominators and overhead | Same numeric factor can have different economic meaning. |
| Nonhour costs | Optional per-respondent other cost; already-annualized startup/O&M entries | Purchased services, capital cohorts/life, annualization, payer/exclusions | Do not collapse all costs into a generic activity total. |
| Government | Labor, per-response and fixed union in engine/schema | Federal activity/allocation, gross resources, fee offsets, net effects | UI currently exposes only labor/fixed; allocations require richer semantics. |
| Growth/prices | Flat/fixed-percent/series projection and deflator helpers | Period, scenario, index rationale and nominal-update controls | Helpers are not wired into current exports; dollarYear is not proof of conversion. |
| Assumptions | Sourced/unverified inputs, notes, frozenParameters | Evidence observations, applicability, method families, provenance and unresolved scope | Evidence becomes a draft input only through an explicit analyst decision. |
| Item 15 | No implemented change-event/baseline model | One verified displayed TWIC bridge; broader future change/decomposition specification | Do not mistake one checked bridge for a generic causal engine. |
| Narrative/formulas | Hard-coded TypeScript functions and output templates; appended overrides | Inert source formulas plus future expression-tree and narrative-binding specification | A later shared engine needs a bounded model, not evaluation of evidence strings. |

The benchmark's 27-entity model 0.5.0 is a research dictionary/specification, not a ready-to-load executable scenario schema. Its detail is useful for gap analysis; it cannot simply replace `DraftProject`. [E02, E07–E09, E12, E23]

### Material implementation limits

1. **UI/schema roundtrip:** `buildProject` reconstructs only the form subset. It omits growth, activity notes, frozen parameters, capital costs and narrative overrides; `loadProject` has no per-response government branch. A rich valid project can therefore lose fields or become unusable through the UI. This is a direct control-flow finding, not a browser-tested reproduction. [E07]
2. **Annualization and price conversion:** exports compute base activity values; Markdown averages repeated copies of the same total for selected years. `projectPopulation` and `toDollarYear` appear in library/tests but are not called by those exports. `threeYearAverage` accepts any nonempty number of years despite its name. [E08–E09]
3. **Item 13 boundary:** Markdown's exclusion wording is followed by a labor-plus-other-cost table; XLSX also places labor there. This conflicts with the benchmark's separate hour monetization/nonhour-cost model and the export's own wording. Empty capital lists also produce a substantive “no costs” sentence, although absence of entries does not establish an observed zero. [E09, E12]
4. **Calculation precision:** icr-tool intentionally uses float64 with roundLast/roundThenSum and decimal-string tie handling. Benchmark evidence retains frozen float artifacts and numeric strings, while the future dictionary requests decimal/rational precision. Reuse must declare a numerical contract; rounding a displayed source must not mutate its evidence value. [E05, E08, E12]
5. **Source proof:** schema locator/rawQuote fields are optional, unlike the stronger CLAUDE.md convention. The form accepts an ID without a locator; footnote export resolves source-level records rather than transmitting each input's locator/quote. A source ID is not validation of the number's support or applicability. [E21]

## Data Architecture Comparison

The actual bundled SQLite database has schema user_version 1: 59 ICRs, 473 document metadata records, 928 sections, 348 burden records, 321 extracted tables, seven source-index records and 4,479 reference-series rows. The latter include 2,640 OEWS wages (2023–24), 140 ECEC factors (2026), and 1,699 enplanement rows (2024). FTS5 indexes sections and sources. Empty review, passport, locator and edit tables describe supported storage shapes, not evidence of populated workflows. Database integrity_check returned `ok`. [E10]

The 59 ICRs comprise 43 non-benchmark and 16 benchmark rows. The UI calls non-benchmark rows TSA. These are not the same unit or selection as the federal benchmark's 73 unique controls, or the TSA release's 90 recent packages across 48 control histories. Corpus count differences are not completeness rankings; full population/lineage equivalence is not established. [E10, E13, E22]

On first launch Tauri copies the bundled database into writable app-config storage. Local sources, appended vintages and review runs live together there. An app reinstall with a new corpus does not merge it into an existing copy. SQL helpers preserve older vintages with supersession pointers and log reasons, but multi-step imports/review writes do not show one encompassing transaction. The external corpus pipeline and future migration policy remain important operational dependencies. [E03, E15]

Draft JSON stores numeric SQLite source IDs, not a portable snapshot of the source registry or a global source namespace. Two independently edited databases can assign different meanings to the same integer. The series supersession key includes kind/key1/key2, whereas draft `seriesRef` and `latestSeriesFor` omit key2: future interchange must define sufficient identity rather than reuse these fields unexamined. [E02–E03, E21]

The release uses authoritative JSON and JSON-pointer indexes, stable source/claim/graph IDs, original and normalized values, and content-addressed provenance references. Qualified retrieval keys are addresses rather than new analytical identities. It contains excerpts and publication URLs, not all original binaries or report PDFs. A future SQLite projection must be disposable, reproducible and equivalent to canonical JSON. [E05, E14, E19]

The exact evidence pin is `ICR-EVIDENCE-1.0.0`, manifest SHA-256 `572e8a414c5867e75a5d24eb4d5e939a475969c92bb1d81b3f183f436b4663a9`. Canonical files are the manifest and its 87 inventoried files. Two administrative closeout files are outside that inventory; only those are removed from the actual directory listing by the workbench adapter. The manifest's historical CANDIDATE label is reconciled by the matching freeze receipt/state, not by rebuilding it. [E13, E18–E19]

## Evidence and Validation Comparison

| Asset/control | Consumable contribution | Boundary |
|---|---|---|
| Federal benchmark, models, source/claim registry | Historical methods, reconstructable examples, citations and rationale | Read-only evidence; purposive research is not an agency ranking. |
| Federal assumption library | 24 method/applicability entries with exemplar references | Reusable reference guidance, not approved scalar defaults. |
| TSA graph and histories | Versioned activity/assumption observations, source relationships and predecessors | Preserve epistemic labels and incomplete coverage. |
| TSA assumption-family catalog | 17 discovery families | Keyword-discovery layer; use reviewed ASSUMPTION nodes for observations. |
| Comparison/reconstruction registers | 32 task/method adjudications plus eight within-ICR findings | Keep register membership, explanations and failed/unknown comparisons. |
| Quantitative checks / Item 15 bridge | 341 TSA checks and one validated displayed-component reconciliation | Executable release acceptance checks are bounded; source formulas remain inert. |
| Runtime consumer | Hash/schema/relationship checks, deterministic exact-facet paging, hydration | Dependency-free ES module; no FTS/language search or automatic judgments. |
| Canonical dictionary | Shared vocabulary and future model requirements | Specification only. |
| Raw archives, research scripts, reports | Audit/research lineage and deeper interpretation | Keep separate from deployed drafting runtime; no acquisition pipeline migration now. |

icr-tool's 25-rule engine checks arithmetic, required wording, source citations/currency and limited cross-corpus context. Its score starts at 100 and deducts by finding severity; missing optional context skips dependent checks. A high score therefore is not a statement of complete coverage or institutional approval. Table-cell passports describe parsed locations and limited recomputation, not externally verified claim objects. [E11, E16]

The strongest conflict in comparison logic is XCOMP-301: it describes a corpus-mode factor, but the screen supplies a latest private-industry ECEC value. XCOMP-302 needs wageSeriesCounts that the screen does not provide. Benchmark comparisons instead inspect actor, task, period, units, lifecycle, vintage and explanations before classification. Do not feed historical differences directly into automated “align with the mode” deductions. [E11–E12]

**Fresh checks in this assessment:** read-only SQLite integrity/count/schema queries passed; Node v24.21.0 `loadRelease` passed inventory/schema/provenance/graph checks; all 12 supplied `acceptance` cases passed, including Federal cost recomputation, the TWIC bridge, comparator retrieval and unresolved questions. No source URLs were fetched. [E10, E19]

**Existing evidence reused:** research and release validation receipts, and workbench's 26-test foundation PASS/deterministic build/package receipts. The test source includes integrity failure cases, store separation and compiler contracts. Some tests write outputs or transiently modify source, so the suite was inspected rather than rerun in the protected working tree. These receipts explicitly report no browser DOM execution, pending Windows/WebView2 deployment validation and no actual Anvil runtime import. [E16–E20]

**Not freshly executed:** icr-tool Vitest, Svelte type checks, frontend build or desktop installer. The clean clone has no node_modules; no dependencies were installed for this inspection mission. Test source includes meaningful golden arithmetic, rounding/schema regressions, 13 seeded review defects and repeated Markdown output checks. External BLS workbook tests skip/return when untracked `data/manual` inputs are missing. Export-to-review tests do not prove full UI roundtrip fidelity, and neither repository's tests establish empirical validity of every assumption. [E16]

## UI and Build/Runtime Comparison

icr-tool owns the more developed estimation user journey. Workbench owns the more explicit immutable-evidence browsing boundary. Similar five-route shells do not imply interchangeable screens. Svelte components call host plugins; foundation provider/store modules are assembled with the frozen consumer into an Anvil governed capability. Importing either application's whole shell into the other would couple packaging and state without resolving semantics. [E01–E04, E18]

icr-tool uses TypeScript, Svelte 5/SvelteKit 2, Vite 6, Zod, ExcelJS, Tauri v2 and Rust; npm and Cargo manage builds. The declared parser dependencies include unified/remark packages, while the inspected supporting-statement parser itself implements section/table handling directly. README prerequisites are Node 20+, Rust/MSVC and WebView2 for the Windows target. A browser-only preview cannot substitute for SQLite/dialog integration. [E01, E15–E16]

Workbench build tooling documents Node 24+ and Python 3.12+; its runtime needs Web Crypto, TextEncoder/Decoder and DecompressionStream. HTML bundles a deterministic compressed evidence payload, with no CDN, server or runtime package installation. Anvil source/capability locks and a separate governed library constrain compilation. Research/report tools separately use Python, pandas/numpy/matplotlib, document extraction and publication tooling. Those are build/research dependencies, not requirements for consuming evidence. [E17–E19]

No shared service, authentication scheme, environment secret or live external API is required by the inspected application paths. External source links are protocol restricted; workbench uses text-node rendering, and icr-tool escapes FTS snippets before inserting highlight markup. These observations are not a general security certification or proof of deployment suitability. [E18, E22]

## Capability Matrix

Classifications describe the scoped row, not overall repository quality.

| Capability | icr-tool | Benchmark/workbench | Relationship and reason |
|---|---|---|---|
| Offline application shell | Working desktop navigation | Working standalone evidence shell | SAME_CAPABILITY: local navigation/runtime, different hosts. |
| Activity drafting/live math | Forms and pure functions | Placeholder calculation route | ICR_TOOL_MORE_MATURE. |
| Markdown document review | Parser, 25 rules, scoring/passports | Production review placeholder | ICR_TOOL_MORE_MATURE. |
| Estimate Markdown/XLSX | Implemented, with noted semantics/coverage gaps | Future scenario outputs | UNIQUE_TO_ICR_TOOL at executable app level. |
| Current wage/compensation-series maintenance | Local imports, vintages, health and pickers | Historical methods/observations | UNIQUE_TO_ICR_TOOL as operational source maintenance. |
| Corpus search | FTS text search | Exact facets, provenance and graph traversal | COMPLEMENTARY: text discovery and structured evidence questions. |
| Source tracking | Source IDs, citations and edit logs | Claims, locators, hashes, transformations | COMPLEMENTARY, requiring identity mapping. |
| Institutional evidence/provenance | Corpus/index; external build pipeline | Frozen audited research and portable release | BENCHMARK_WORKBENCH_MORE_MATURE. |
| Historical task comparability | Heuristic XCOMP rules/context | Reviewed scope/lineage/challenge registers | BENCHMARK_WORKBENCH_MORE_MATURE. |
| Corpus norm as authority | Factor-mode-style deductions | Explicit applicability and negative matches | POTENTIAL_CONFLICT: disagreement need not mean defect. |
| Rich population/capital/renewal model | Partial draft schema | Broader non-executable dictionary | NOT_COMPARABLE: running subset versus specification. |
| Item 15 baseline evidence | No dedicated model | Verified TWIC component bridge/history | UNIQUE_TO_BENCHMARK, not a general calculator. |
| Immutable release ingestion | No such path found | Pin, inventory, schema and source checks | UNIQUE_TO_BENCHMARK. |
| Local project/overlay storage | Durable draft files and mutable DB | Separated validated in-memory envelopes | COMPLEMENTARY: durability and evidence separation solve different needs. |
| Arithmetic correctness controls | Golden/seeded/unit tests | Source reconstruction and release checks | COMPLEMENTARY: engine regression versus published-evidence validation. |
| Frozen report publication/research | Not present | Completed reports and pipelines | UNIQUE_TO_BENCHMARK. |
| AI/graph visualization | No live AI flow | Reserved DHSChat/A2UI/graph interfaces | NOT_COMPARABLE as implemented functionality; no working integration to reuse. |

## Overlap and Duplication

Both systems index supporting statements, retain cost/burden concepts, calculate or check arithmetic, handle source citations, and expose an offline shell. Duplicate data may represent the same publication, but matching control numbers or URLs does not establish equivalent package versions, locators or extraction coverage. icr-tool already has a substantial corpus: the release should supplement it rather than erase it. [E10, E13–E14, E22]

The largest avoidable future duplication is independently building another calculation/draft engine inside workbench without first evaluating icr-tool's existing pure functions and tests. Conversely, rebuilding the benchmark graph and provenance in mutable SQL would discard a tested data contract. Existing formula and citation utilities are reuse candidates, not automatically approved replacements. [E08, E12, E18–E19]

## Complementary Capabilities

An analyst could use benchmark evidence to find a related activity, inspect its original observation and applicability limits, record a deliberate local assumption decision, and then calculate a draft in icr-tool. This combines implemented strengths without converting historical observations into defaults. The product should retain the release pin, source and observation IDs, locator, original unit/period and transformation alongside that decision. This is a proposed future flow. [E05, E12, E14, E23]

icr-tool's engine regression fixtures and benchmark reconstruction cases could later support a common validation corpus with explicit published-versus-calculated expectations. Historical source discrepancies must remain labeled; a new engine is not required to reproduce an erroneous published total as the correct answer. [E08, E12, E16, E19]

## Architectural Conflicts

The principal conflicts are (1) mutable bundled-corpus copies versus immutable release upgrades; (2) local integer IDs versus portable identities; (3) schema richness versus UI/export preservation; (4) Item 12/13 and unique-population semantics; (5) scalar compensation factors versus denominator-specific methods; (6) rule-score norms versus evidence-bounded comparisons; (7) float64 implementation versus richer future precision requirements; and (8) desktop authority versus browser/Anvil host constraints. Evidence for each appears in the corresponding data/domain/validation sections. None is solved by merging Git histories.

A complete evidence release cannot be stuffed into `reference_series`: many observations are text, formulas, unknowns, task contexts or conflicting interpretations. Likewise, workbench's empty project envelope cannot accept an icr-tool draft without defining a new schema and validated migration. Those are explicit future design tasks, not changes authorized by this loop. [E02, E04–E05, E23]

## Integration Options

| Option | Advantages | Disadvantages / technical implications | Assessment |
|---|---|---|---|
| Direct repository merge | Single checkout | Mixes frozen research, two host toolchains and application release responsibilities; resolves no data semantics | Not justified. |
| icr-tool consumes portable evidence release | Existing verified consumer, offline, preserves provenance, independent release lifecycle | Add asset loading and UI bindings; exact pin and update policy; source/observation namespace | Preferred near term. |
| Generated static data dependency | Fits offline packaging and release pinning | A subset can lose provenance or caveats; needs complete dependency closure and validation | Use full canonical release initially; derive views through consumer. |
| Shared package/library | Reduces future duplicated calculation/query logic | Ownership, versioning, TS/JS build and semantic parity need resolution | Medium-term candidate, separate evidence consumer from calculation contract. |
| Local API/service | Separates runtime languages and hosts | Adds process lifecycle, IPC/ports, installation and operational burden absent today | Defer unless a real host constraint requires it. |
| SQLite / structured-data interchange | Familiar search and local performance | Integer collisions, schema/update ambiguity; source truth can drift | JSON authoritative; optional separate derived read-only DB, never sole evidence copy. |
| Selective code migration | Reuse mature pure functions/tests in another host | UI/plugin code is host-bound; existing export and model gaps travel with it | Consider only after parity review; no wholesale screen migration. |
| Shared domain model | Aligns units, assumptions, baselines, validation and outputs | Canonical dictionary is not executable; full schema cannot currently roundtrip through UI | Incremental versioned contract with explicit unsupported cases. |
| Parallel systems, limited interoperability | Lowest initial coupling; preserves distinct environments | Manual cross-reference and duplicated navigation | Credible fallback if Tauri deployment is unsuitable; share release identity first. |

## Recommended Direction

### Near term

Retain icr-tool as the leading candidate for drafting and document review, and retain benchmark/workbench as the evidence producer and reference inspection system. In a separate implementation loop, add consumption of the exact portable release as a verified read-only asset. Use `loadRelease`, bounded queries and provenance hydration through an application adapter, not copied research scripts or edited frozen runtime code. Show release/version and evidence limitations with results. [E14, E18–E19]

Keep three independent authorities: immutable public evidence; mutable local source/assumption decisions; working draft estimates. Preserve icr-tool's existing source-series workflow separately. Do not silently repoint a draft when evidence or wages change. A deployment decision remains conditional on actual Tauri/Windows and institutional host suitability.

The later acceptance gate should require pin/tamper rejection, offline retrieval, preserved source/epistemic fields, no base mutation, and explicit analyst adoption. Before permitting rich model interchange, require lossless supported-field roundtrip, declared rejection/preservation of unsupported fields, stable source remapping, and reconciled Item 12/13, population and annualization outputs. These are proposed criteria, not tests written or implementation performed here.

### Medium term

Define a versioned executable subset informed by both `DraftProject` and canonical model 0.5.0. Start with collection/version identity, typed populations, activity/frequency/time, compensation method, provenance-bearing inputs and calculation/output contracts. Extend explicitly to nonhour costs, government allocations and Item 15; do not promise all 27 entities immediately.

Evaluate extraction of a host-independent calculation/review library from icr-tool only after resolving the documented gaps. Keep evidence retrieval and calculation versions independently pinned. Workbench can then reuse the agreed contract if a browser/Anvil authoring product is needed; it need not independently rebuild the same formulas. Authoring-host choice does not require merging research repositories.

### Remain separate

Frozen public evidence and research audit trails; TSA-local overlays and access decisions; working scenarios; historical report publication; source-acquisition pipelines; and host-specific UI/packaging. Keep applicability, comparability, official corrections, causal decomposition, Item 15 classification and publication decisions human-owned. Preserve unresolved historical questions. [E05, E12, E23]

## Open Questions

1. Which host is deployable and supported for intended users: Tauri desktop, standalone browser, Anvil, or more than one? Repository receipts do not establish production device suitability.
2. Who owns release publication, trusted digest distribution, source-license/redistribution decisions and long-term maintenance of any shared package?
3. Where is icr-tool's external database build pipeline, and how are provenance, input hashes and corpus version upgrades reproduced without losing local edits?
4. What global identity/locator format should make drafts portable across local source databases and evidence release versions? How should multiple series dimensions and competing updates be handled?
5. Which canonical-model subset is required first, and who adjudicates Item 12/13 boundaries, compensation denominators, overlap, annualization and Item 15 semantics before product acceptance?
6. What restrictions and persistence requirements apply to actual TSA-local material? Neither this public repository inspection nor an in-memory overlay establishes those requirements.
7. Which reviewed assumptions are approved for a particular new activity, with what owner and review date? Libraries contain evidence and methods, not an approved defaults list.
8. What UI/export validation standard is required beyond the existing unit and export-to-review fixtures? Full schema roundtrip and Windows/WebView2/Anvil behavior remain unverified here.
9. Frozen substantive questions remain: six unresolved task/method comparisons (CMP-04, 05, 09, 10, 14, 21), plus one unresolved within-ICR finding; seven reconstruction cases are potentially inconsistent, not official corrections. Their operational causes and task-scope ambiguities cannot be settled by code inspection. [E19, E23]

These are decision/deployment or frozen-evidence limits, not reasons to continue low-value file enumeration.

## Evidence Log Summary

The recommendation rests most strongly on the actual draft schema and form/export paths [E02, E07–E09], SQLite schema and initialization behavior [E03, E10], concrete review context [E11], canonical/comparability contracts [E12], verified consumer/provider [E14, E19], and workbench's explicit module/store boundaries [E04, E18]. Source-proof and immutable-overlay distinctions [E21, E23] explain why a translation boundary is necessary.

See [evidence-log.md](evidence-log.md) for exact baseline commits, paths, functions and validation provenance; [comparison-state.json](comparison-state.json) for coverage and pass history; and [LOOP.md](LOOP.md) for mission boundaries and closeout state.

## Saturation and closeout

Five recorded passes covered the major structures, workflows, models, persistence, runtime, validation, institutional evidence and integration boundaries. Passes 1–3 produced material findings; passes 4–5 cross-checked the proposed boundary and evidence claims without changing the recommendation. Remaining questions require product ownership, deployment tests or substantive analyst decisions rather than more code enumeration. Architectural saturation is reached.

Closeout checks found only the four assessment files added; tracked application code, frozen evidence and all other baseline files remain unchanged. icr-tool remains clean at the inspected SHA, in its own sibling Git repository. No icr-tool source was copied into this folder. The sole comparison commit is to be published to benchmark origin/main; no implementation or post-push CI polling is part of this mission.
