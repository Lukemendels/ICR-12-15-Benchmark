# ICR Evidence Release 1.0.0

Portable public evidence for a local ICR Workbench. JSON is authoritative. This release contains the 73-ICR federal benchmark and models, 200 federal sources, 389 federal claims, federal method assumptions and the frozen 27-entity canonical model; TSA portfolio, graph, reviewed assumptions, comparisons, within-ICR findings, quantitative checks, predecessor bridge, excerpts, and bounded retrieval indexes. It includes 90 recent TSA packages and 48 assigned control histories. Recency is not approval status.

The original evidence states are M1-1.0.0 and M3-1.0.0; graph 1.0.0; canonical model 0.5.0; rubric 1.0.0. Mission 4 and the completed EAB brief supply the analytical snapshot. Exact commits and input hashes are in the manifest and provenance/input-inventory.json. No new research was conducted.

Start with release-manifest.json, CONTRACTS.md and LOOP-5.2-HANDOFF.md. The graph and indexes are projections; complete adjudication registers govern analytical meaning. Source evidence, normalization, inference, calculated results, unresolved questions and reusable method guidance retain distinct labels. Numeric assumptions are observations, not approved TSA defaults.

## Validation and offline loading

Unzip to a new directory. Obtain the expected manifest SHA-256 from the separately committed freeze receipt. On a machine with Node, run `node runtime/verify.mjs . EXPECTED_MANIFEST_SHA256` from this directory. No package installation, Python, network or repository is needed. Omit the hash only for exploratory loading; a trusted external hash is needed to verify the expected identity. The validator does not write into the release.

For an offline HTML/WebView2 application, include runtime/consumer.mjs in the application build and supply `readBytes(relativePath)` from user-selected files or the host file bridge. Call `loadRelease(readBytes, {expectedManifestHash, listPaths})`. It uses native UTF-8, JSON and Web Crypto only. A File/ArrayBuffer adapter avoids file:// fetch restrictions. Nothing here requires an HTTP server. Consumer returns structured data; it does not render source text as HTML or execute stored formulas.

Validation checks the complete artifact inventory, SHA-256, every listed JSON contract, IDs, provenance, graph endpoints, claim sources, comparison evidence, counts, bridge arithmetic and indexes. The runtime intentionally supports only the JSON Schema keywords used by this release and rejects unsupported keywords. The repository build audit additionally verifies input fingerprints, frozen-tree preservation and lossless reproduction of canonical registers. The clean-load report records isolated release-only retrieval tests.

## Scope and limitations

This is not a Workbench UI, approved ICR model, legal guidance, official correction, internal TSA dataset, or complete archive of publication binaries. Source excerpts and registered analytical evidence are available offline; clicking an external publication requires connectivity. Public links are preserved as frozen locators and were not newly tested for availability. Full reports and original documents remain outside the distribution.

There are 468 principal activity representations and 25 assumption-context activity nodes. Repeated table/narrative, year/annualized and predecessor representations must not be summed. There are 32 task/method adjudications and a separate eight-record within-ICR register. Six unresolved task/method questions are not the seven combined unresolved records. Neither register supports a portfolio inconsistency rate.

Only 40 versions have registered quantitative checks. Row screening does not mean full-model assurance. Null/absent means unobserved, not zero. The federal sample is purposive. Source metadata review flags can predate completed review; canonical analytical registers govern. See KNOWN-ISSUES.md and provenance/limitations.json.

Base evidence remains immutable. Layer TSA-local evidence and project models in separate stores using the overlay contract. Human approval controls applicability, comparability, new assumptions, official corrections, Item 15 cause/classification, and narrative adoption.
