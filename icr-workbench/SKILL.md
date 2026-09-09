---
name: icr-workbench
description: Extend the modular Anvil ICR Workbench foundation using pinned public evidence, separate overlays and project state; use for bounded Workbench source changes.
---

# ICR Workbench

Read ARCHITECTURE.md for boundaries, assets/evidence-pin.json for identity, and paperclip.tool.json for actual Anvil entries. Application version starts at 0.1.0. Source is this folder; dist HTML and ZIP are derived. Do not edit frozen release files or reopen completed evidence research.

Use src/index.html, src/style.css and src/app.js for normal Anvil changes. Runtime guidance is skills/icr-workbench.md. Foundation capability modules are in assets/foundation; their generated governed release is separately pinned and selected read-only. Do not paste evidence or library implementation into model context. Request only the files relevant to the current change.

Evidence loading: `ICRFoundation.loadAdapter({readBytes,listPaths})` verifies the exact manifest hash, all artifacts and schema before returning deeply frozen base objects. File/ArrayBuffer and bundled adapters avoid file:// fetch. Exclude only the two documented administrative files from actual path listings. A mismatch, unknown file, missing byte or unsupported version must fail closed. Never substitute latest or synthesize a directory listing from the manifest.

Use `createQueryProvider(base)` for frozen exact-facet queries and provenance. Respect pagination, missing values, epistemic status and record_kind; overlapping activity representations must not be summed. Base objects have no mutation API. Overlay envelopes use the release contract, exact base pin and local namespace. Working project envelopes use project IDs and remain independent. Neither store merges into the base; both export independently.

Render stored strings with textContent and safe DOM nodes; only http/https source links. Do not evaluate stored formulas, HTML or future packets. DHSChat and A2UI are reserved boundaries, not implemented features.

Build: `node tests/build.mjs`. Test: `node --test tests/foundation.test.mjs`. Transfer: `python tests/package.py`. Explicit capability release preparation: `node tests/build.mjs --prepare-capability`; bump its version and review changed identity for substantive capability changes. Ordinary build never silently updates a lock. Anvil uses the shared compiler directly with separately selected project/library roots.

Keep proposals isolated; validate source/capability/artifact identities and obtain explicit human promotion in Anvil. An existing programming request authorizes its scoped repository work; these instructions do not introduce a second approval flow. Do not claim a real Anvil import from contract-only validation.

Human judgment remains required for comparability, assumption applicability, proxies, missing inputs, corrections, Item 15 causal/classification decisions, interpretation, narrative adoption and publication. Later loops extend Evidence visualization and the query/data/A2UI bus, then quantitative modeling, production and TSA adaptation. Read LOOP-5.3-HANDOFF.md before extending.
