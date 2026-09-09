# Mission2 handoff

**Evidence:** M1-1.0.0. **Rubric:**1.0.0, unchanged weights. **Canonical model:**0.5.0, frozen reference architecture. Repository state and evidence-manifest hashes identify the frozen contents; the commit containing the freeze is the durable version. Mission1 stops at evidence freeze. Mission2 may synthesize and publish, preserving the limitations below.

Start with research/research-state.json, research/research-summary.md, methodology/exemplars.md and research/limitations.md. The empirical evidence contains73 unique recent controls,38 component labels and10 TSA collections. Primary date window:2023-09-09 through2026-09-09, using actual OIRA receipt/submission dates. Document dates and pending/concluded status are separate; historical methods are not additional recent observations.

Major findings: best practice is distributed across government; TSA shows strong Item12 methods and inconsistent public reconstruction, not demonstrated unique superiority. BLS SOII83 is the highest observed total, followed by EBSA settlement82 and OSHA process safety80. BLS SOII/NCS lead the Item12 composite53/60; TSA flight training52. FCC IPCS leads Item15. No universal nonzero capital exemplar, agency-wide best or most-consistent agency is established. Zero-cost exemplars must be kept distinct from nonzero-cost methods. Descriptive agency dispersion and score sensitivity are already computed.

The causal reason for TSA rigor remains unresolved. EBSA and CMMC directly demonstrate PRA/regulatory-analysis reuse elsewhere. New TSA submissions dated2026-08-21 and2026-09-01 cannot be attributed to the reported overhaul from public evidence. Do not manufacture a before/after result.

| Structured evidence | Location/use |
|---|---|
| Collection and scores | data/icrs.csv; data/scores.csv |
| Descriptive comparisons | data/agency-summary.csv; data/score-sensitivity.csv |
| Quantitative extraction | icrs/*/extraction.json; data/model-sections.jsonl |
| Arithmetic checks | data/calculation-checks.csv;267 checked expressions |
| Original/table evidence | icrs/*/raw; icrs/*/table-evidence.json; raw/methods and raw/guidance |
| Citation metadata | data/sources.jsonl; source access and archive hashes included |
| Consequential findings | data/claims.jsonl; CLM-FINDING-001–020 and historical method claims |
| Sources and assumptions | data/data-sources.csv; data/assumptions.csv |
| Modeling specification | methodology/canonical-model.md; canonical-data-dictionary.md; tool-requirements.md |
| TSA actions | methodology/tsa-comparison.md KEEP/IMPROVE/ADOPT/INVESTIGATE |
| Stop-condition evidence | research/saturation-log.md; logs/iteration-009-results.md; research/final-validation.json |

Report-worthy visuals: dimension heatmap with complexity/relevance annotations; TSA distribution alongside selected close comparators; FCC old-to-new waterfall; alternative wage-loading equations with defined bases; reporting-cycle versus approval-horizon example; Census measurement-scope comparison; source-to-formula-to-table-to-narrative architecture. Use exact machine-readable values and preserve any source uncertainty. Avoid a single unlabeled agency league table.

Questions requiring careful interpretation: Are apparent numeric conflicts caused by rounding, hidden precision or inconsistent versions? Does an agency's zero reflect true incremental scope or financing? Are fees transfers or purchased resource costs? Is occupational employment a defensible task mix? How should unavailable internal models affect judgments about public reconstruction? Which regulatory costs belong within PRA scope? How should conflicting official instruction wording be resolved before software defaults?

Validation is structural, provenance-oriented and selected arithmetic, not independent replication of every internal model. Scores are single-analyst judgments; close scores are not meaningful superiority. All73 statements were reviewed, but underlying citations are not all independently retrieved and peripheral rows may require semantic normalization. Retain these qualifications prominently. Mission2 should not repeat broad discovery without a concrete new question; focused clarification can be recorded as a new evidence version.

Descriptive repeated-component lens (n>=3 only): BLS has the highest observed mean76.67(n3); Census has the narrowest observed score dispersion1.41(n3,range71–74). These are within-sample summaries, not agency population rankings.
