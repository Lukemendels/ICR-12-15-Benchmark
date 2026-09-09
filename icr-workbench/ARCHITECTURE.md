# ICR Workbench architecture · 0.1.0

## Authority and project contract

`icr-workbench/` is the editable application authority. `paperclip.tool.json` follows the actual Paperclip v1 schema from Paperclip-Workbench commit `8f9f0db512873907c6963e327ebd539b8ffb9d66`; source HTML, CSS and JavaScript are separate files. The shared compiler and authoring validator are vendored unchanged with byte pins in `assets/anvil/upstream-pin.json`. The stable ABI requires `dist/icr-workbench.html`, its embedded descriptor, STICKSHIFT_TOOL identity, and authored launch skill. Extra Workbench configuration belongs in assets, not invented manifest fields.

Authority order: frozen release and its external pin → exact governed capability release → modular application source and project configuration → separate local overlay and working model → derived standalone HTML and transfer ZIP. `dist/` never becomes source. Neither the ZIP nor an installed runtime is the editable project authority.

The single JavaScript entry is the existing Anvil compiler contract, not a giant HTML source. It owns only navigation and UI orchestration. Loader, query provider, stores and future interfaces have separate source modules under `assets/foundation/`. Those modules plus the unchanged frozen consumer and byte-exact evidence payload are packaged as one pinned governed foundation capability. This keeps evidence and implementation bytes out of model context while preserving normal Anvil edits to HTML/CSS/JavaScript. Capability source changes require explicit capability release/pin regeneration and review, not ambient library changes.

## Evidence path and immutable base

Development reads `../release/icr-evidence/v1.0.0/`. A transfer contains exact canonical files in a separate `evidence/icr-evidence/v1.0.0/` folder. Packaging verifies the SHA-256 of the exact manifest including newline and every listed artifact before copying or embedding anything. There is no hand-maintained evidence fork.

Actual local bytes → adapter `readBytes(relativePath)` and actual `listPaths()` → unchanged `loadRelease` with required digest → all inventory/schema/reference checks → version-pin checks → recursive object freeze → queryable base. The runtime capability embeds losslessly compressed canonical bytes; browser DecompressionStream restores them before verification. File selection and a caller-supplied read-only host adapter use the same path. No file-URL fetch is used. All bytes are verified before exposing records. Failure leaves the UI unavailable and actionable error text visible.

Only `FREEZE-RECEIPT.json` and `validation/final-acceptance-gate.json` may be removed from the actual release-directory listing. `loop-5/freeze-state.json` is outside that directory and is not an allowlisted path inside it. Unknown files, duplicate paths, path traversal, and missing artifacts fail. The manifest's historical CANDIDATE metadata is not lifecycle authority; the supplied freeze receipt establishes the frozen state for the pinned digest.

All loaded base objects are recursively frozen, including nested records, indexes, manifest and validation results. The adapter exposes no write method. Query pages may be newly allocated but record references remain frozen. Hydrated objects are frozen before return. An explicit evidence upgrade changes the project pin and capability release; never follow `latest`.

## State ownership

| Store | Owner | Mutation/export rule |
| --- | --- | --- |
| App configuration | Project assets and manifest | Reviewed source change |
| Evidence identity | `assets/evidence-pin.json` | Exact release upgrade only |
| Loaded public base | Verified foundation capability | Deeply immutable; no local write/export merge |
| TSA-local overlay | Overlay store closure | Frozen contract, `local:<organization>:<uuid>` IDs; independent JSON export |
| Working ICR model | Project store closure | `project:<uuid>` envelope; independent export; no calculation model yet |
| UI/session | UI controller | Navigation and selected package only; no analytical authority |

No implicit localStorage persistence: local browser data would not provide access control or dependable portable storage. Local envelopes are in memory; explicit user-selected imports and exports establish the future persistence boundary. The foundation supplies validation/storage interfaces and independent exports; the UI does not create invented internal evidence or dummy ICR models.

Overlay validation reuses the release schema and enforces the exact base digest, namespace consistency, unique IDs and base-reference resolution. Competing proposals remain distinct records. No proposal is merged into the base. Approval status is supplied human metadata, never inferred by this tool. A project envelope pins the base and contains a separate workspace; it cannot replace base IDs. Restricted-data handling, export review and endpoint access controls belong to the receiving institution. Public runtime assets contain public evidence only.

## Modules and governed capabilities

`assets/foundation/adapter.js`: strict byte/File/host loading, bundled decoding, version checks, recursive freeze.

`assets/foundation/provider.js`: `createQueryProvider(base)` returns bounded `query(request)`, `portfolio()`, `activities(ref, page)`, `source(id)`, `sourcesFor(record)`, `hydrate(record)`, and typed `neighbors(id, type)`. It delegates exact facets/pagination to the frozen consumer. Source lookup uses indexes/sources.json; provenance observations link to registered sources. Linked public documents need connectivity only when the operator opens them; excerpts remain offline.

`assets/foundation/stores.js`: separate overlay and project closures, validated replacement, immutable snapshots and independent JSON exports. No generic base setter.

`assets/capabilities.json`: logical interfaces, implemented versus reserved state, versions and source paths. `assets/dependencies.lock.json` pins exact generated capability descriptor/implementation/skill/test digests. The separate generated `governed-library/` root must be opened read-only in Anvil. No project workflow writes the selected library. No transitive solver, CDN, model API, network or ambient package dependency exists.

Canonical JSON and frozen indexes are the initial provider. Future SQLite must be a reproducible disposable projection with conformance against this same interface; no evidence may exist exclusively in a database.

## Build, candidate and promotion

From this root: `node tests/build.mjs` validates pins and sources and uses the unchanged Anvil compiler. `node --test tests/foundation.test.mjs` tests behavior. `python tests/package.py` produces a deterministic transfer archive. Authoring needs Node 24+ and Python 3.12+ for those repository commands; normal Anvil compilation and application runtime do not.

`node tests/build.mjs --prepare-capability` is the explicit release preparation operation: it verifies canonical evidence, packages the foundation modules and exact consumer into a governed capability, writes its hash lock, then compiles. It is not the ordinary build. A capability source change must increment capability version and undergo review before preparation/promotion. Unchanged inputs reproduce identical bytes. Ordinary build refuses stale or altered dependencies. The capability folder is a derived release of this project's bounded foundation source, not a hand-edited source copy.

The transfer archive holds `icr-workbench/`, `governed-library/`, and `evidence/` as separate roots. After extraction, select the first two independently in Anvil. Normal Anvil compilation consumes the pinned generated capability with the modular project directly; no prebuild or Node is needed on the receiving runtime. Repository rebuild commands can reproduce it from canonical source. No candidate, cache or recovery directory enters the transfer source.

In Anvil, candidates remain isolated until human promotion; validation and exact source/capability/artifact digest review precede promotion. The operator grants project and library access separately. Ordinary project edits do not authorize library writes. This application does not implement a second promotion engine. Foundation tests exercise the actual upstream authoring candidate/closure primitives and shared compiler. A real Windows/Anvil import, if unavailable, is explicitly recorded as ANVIL_RUNTIME_IMPORT_NOT_EXECUTED, not claimed from source-level checks.

## Safe UI and future bus

Evidence and source text use textContent and DOM element construction. No innerHTML, eval, Function, executable formula evaluation or packet-supplied components. Source links permit only http/https and use noopener/noreferrer. Module placeholders clearly say unavailable. HTML/CSS are trusted application source; stored text is data. The packed payload is encoded, never inserted as executable evidence text.

Loop 5.3 extends the Evidence route using provider pages and registered graph/provenance IDs. The future DHSChat path is plain-language question in DHSChat → validated bounded query packet → provider → provenance-bearing data packet → DHSChat analysis → schema-validated allowlisted A2UI packet → safe renderer. These packet adapters and renderer are reserved interfaces, not working controls. Packets carry release identity, bounded pagination and epistemic labels; no scripts, arbitrary queries, silent mutations, or automatic analytical decisions.

Loop 5.4 can implement the calculation module and project schema from the frozen architectural model, which is not yet an executable model schema. Loop 5.5 can add narrative bindings, deterministic QA, renewal and Item 15 change accounting. Loop 5.6 can adapt TSA-local workflow and host persistence after actual endpoint testing. Later mission briefs govern exact sequencing.

## Human decisions and security assumptions

Software must not decide task comparability, assumption applicability/transfer, proxies, missing substantive inputs, official corrections, program change versus adjustment, causal Item 15 decomposition, analytical interpretation, narrative adoption or publication approval. Future decision records must identify the human disposition and provenance rather than silently closing questions.

Trusted code, trusted external digest and a modern browser with Web Crypto, TextEncoder/Decoder and DecompressionStream are assumed. A digest proves expected bytes, not institutional approval or publisher authentication. The application is not an SSI security boundary, does not grant filesystem/network privileges, and does not claim that public evidence is complete or that unknown values equal zero. No service worker, local server, runtime package installation or live model is needed.

## Checkpoint B bounded completion repairs

The initial foundation capability is released as `icr-evidence-foundation@1.0.1`. The application remains 0.1.0. Loader-owned WeakSet membership now prevents a caller from forging a verified base merely by copying the manifest hash onto a frozen object. All pinned component versions are checked explicitly. Provider adds `selectPackage(ref)`, `findings(ref, page)` for the complete task/method register, and safe `sourceLinks(record)`; `assets/foundation/render.js` holds text-node and protocol-restricted source-link helpers. No evidence bytes or frozen consumer code change.

The five routes are orchestrated by `src/app.js`; UI/session state stays in its private closure. The Evidence route pages activities in groups of ten, provides package selection, source links and frozen task/method adjudications. Create / Model and Review remain clearly labeled boundaries. Build commands resolve either the repository release root or the transfer's sibling evidence root. The exact payload is bundled as gzip-compressed base64 with deterministic ordering; source authority remains modular.
