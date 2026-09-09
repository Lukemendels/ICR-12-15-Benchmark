# ICR Workbench 0.1.0

Open `dist/icr-workbench.html` directly in a supported modern browser. The file bundles the pinned public evidence and verifies it before enabling inspection. No server, CDN, model API or runtime package manager is needed. External published-document links require connectivity only when opened.

The editable project is `icr-workbench/`. Read `ARCHITECTURE.md` and `SKILL.md` before source changes. `src/` contains the minimal five-route shell. `assets/foundation/` contains the loader, bounded query provider, separate state stores and safe DOM helpers. The separate `governed-library/` contains a pinned derived foundation capability.

From the project root:

```sh
node tests/build.mjs
node --test tests/foundation.test.mjs
python tests/package.py
python tests/acceptance.py
```

Build/test tooling requires Node 24+ and Python 3.12+. Normal Anvil compilation uses the included governed capability directly. Select the project root and the separate governed-library root in Anvil. Do not select the repository or ZIP as a project, or edit the compiled HTML as source.

A reviewed capability source change requires an explicit version/pin update followed by `node tests/build.mjs --prepare-capability`; ordinary builds refuse stale source locks. Foundation capability 1.0.1 completes the unreleased Checkpoint A source, adds verified-base membership checks, explicit component version checks, named package/finding retrieval, and safe rendering helpers. Workbench application version remains 0.1.0.

The TSA-local overlay and working-project envelopes are independent in-memory APIs with explicit JSON import/export. The shell exposes their status, without inventing internal records or a calculation model. Reloading clears local envelopes. Graph visualization, DHSChat query/data packets, A2UI, calculations and production review are not implemented.
