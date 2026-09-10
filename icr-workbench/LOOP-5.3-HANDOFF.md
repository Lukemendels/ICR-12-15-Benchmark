# Loop 5.3 handoff — Evidence Explorer and DHSChat Bus

Loop 5.2 delivers the foundation only. The authoritative editable root is `icr-workbench/`; application 0.1.0 consumes `icr-evidence-foundation@1.0.1` from the separate pinned `governed-library/`. Public evidence is `ICR-EVIDENCE-1.0.0`, with exact manifest SHA-256 `572e8a414c5867e75a5d24eb4d5e939a475969c92bb1d81b3f183f436b4663a9`. Read ARCHITECTURE.md, SKILL.md, assets/capabilities.json, assets/evidence-pin.json and assets/dependencies.lock.json before extending. Reuse Checkpoints A and B; do not restart evidence research or alter the frozen release.

## Existing interfaces and boundaries

`globalThis.ICRFoundation` exposes the governed closure. In `assets/foundation/adapter.js`, `loadAdapter({readBytes,listPaths})` returns a Promise of a verified, recursively immutable base. `bytesAdapter(entries)`, `fileAdapter(files)` and async `bundledAdapter()` supply bytes without file-URL fetch. Actual path inventory, exact digest, component versions and frozen consumer validation precede exposure. Loader-owned membership rejects forged bases.

`assets/foundation/provider.js`: `createQueryProvider(base)` exposes `query({filters,limit,after})` with exact facets, limits 1–100 and opaque continuation; unknown operators fail. Pages contain records, total and next. `portfolio()`, `selectPackage(ref)`, `activities(ref,page)` and `findings(ref,page)` support the shell. `neighbors(id,edgeType)` resolves frozen adjacency IDs. `source(id)`, `sourcesFor(record)`, `sourceLinks(record)` and `hydrate(record)` resolve registered source and provenance relationships. Preserve IDs, epistemic labels, units, missingness and overlapping representation warnings. The canonical consumer/indexes define supported filter semantics; never add arbitrary SQL or executable query expressions.

`assets/foundation/render.js`: `textNode(document,tag,text,className)`, `safeSourceURL(url)` and `sourceLink(document,source)` provide text-only nodes and restricted HTTP(S) links. Do not use stored HTML, scripts or executable formulas.

`assets/foundation/stores.js`: `createStores(base)` returns independent `overlay` and `project` closures with `importJSON`, `exportJSON`, `snapshot` and `clear`. The public base has no mutation API. TSA-local proposals pin that base and use local organization IDs; working projects use separate project IDs and an empty workspace envelope. Snapshots are immutable, exports separate, persistence in memory only. The shell shows store status; no institutional records are bundled and no quantitative model exists.

## Navigation and exact extension points

`src/index.html`, `src/style.css`, and `src/app.js` remain modular authority. The private app closure owns route, package selection and pagination. Routes are Home, Evidence, Create / Model, Review, and Settings / Release. Create and Review are explicit unavailable modules.

- Evidence graph visualization: extend `evidence()` at its existing `Loop 5.3: mount graph visualization here` comment in `src/app.js`. Consume provider pages and `neighbors(id,type)` with registered IDs; preserve bounded retrieval and provenance links.
- DHSChat query packets: the reserved `dhschat-query-packets` entry in `assets/capabilities.json` is the contract slot. Define a new validated adapter module under `assets/foundation/` that maps allowlisted, release-pinned packets to `provider.query(request)`; no packet API is implemented yet.
- Deterministic evidence/data packets: the reserved `data-packets` entry in `assets/capabilities.json` is the contract slot. Define a separate serializer over bounded provider results, hydrated provenance and exact release identity; specify ordering, pagination and epistemic labels before implementation.
- Schema-validated A2UI: the reserved `a2ui-rendering` entry in `assets/capabilities.json` is the contract slot. Define an allowlisted packet schema and separate renderer using the existing safe DOM helpers. No schema or renderer currently exists. Packet-provided components, code and silent store mutations must remain prohibited.

New governed modules require explicit capability version/pin/lock preparation, not an ambient change to 1.0.1. `tests/build.mjs` currently assembles adapter/render/provider/stores in `implementation()` and exposes a fixed public API there; future approved module/API additions must update that assembly explicitly. Loop 5.3 has not been implemented by closeout.

## Build, validate and transfer

From `icr-workbench/` with Node 24+ and Python 3.12+:

```sh
node tests/build.mjs
node --test tests/foundation.test.mjs
python3 tests/package.py
python3 tests/acceptance.py
```

Acceptance orchestrates the existing tests, build, package extraction/rebuild and closeout reports. It checks repository checkpoint ancestry when run in the repository; an extracted transfer instead supports build, foundation tests and package reproduction without Git history. Only an explicitly reviewed new capability release uses `node tests/build.mjs --prepare-capability` after version updates.

Standalone: `icr-workbench/dist/icr-workbench.html`. Transfer: `icr-workbench/dist/ICR-Workbench-Anvil-Project.zip`. Extract all three sibling roots: editable `icr-workbench/`, read-only `governed-library/`, and byte-exact `evidence/icr-evidence/v1.0.0/`. Select project and library separately in Anvil; do not select the ZIP or whole repository. The ordinary shared Anvil compiler consumes the already prepared capability; no receiving-runtime Node prebuild is required. Dist is derived. Validation reports remain repository-side to avoid ZIP/hash self-reference; source, handoff, tests and standalone are transferred.

## Validation scope and human authority

Linux platform-independent foundation tests, shared compiler/authoring contract validation and extracted-package byte reproduction are the closeout evidence. Windows status is `WINDOWS_WEBVIEW2_DEPLOYMENT_VALIDATION_PENDING`; actual host import is `ANVIL_RUNTIME_IMPORT_NOT_EXECUTED`. Later, validate project/library selection, compilation, offline evidence load and navigation in the supported Windows/WebView2/Anvil deployment device. Linux source-contract tests are not host execution.

Core operation is offline and requires modern Web Crypto and DecompressionStream. Opening external source documents requires connectivity. No full browser DOM smoke test was executed. There is no natural-language query, DHSChat integration, A2UI implementation, graph visualization, durable local storage, quantitative modeling, Items 12–15 generation, production QA or TSA-specific workflow customization.

Humans decide comparability, assumption transfer, proxies, missing substantive inputs, official corrections, program-change versus adjustment classification, Item 15 causal decomposition, interpretation, narrative adoption and publication. Preserve unresolved limitations and proposed versus approved states. The tool is not an SSI security boundary or institutional approval mechanism.
