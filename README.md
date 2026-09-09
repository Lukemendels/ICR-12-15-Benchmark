# ICR Items12–15 Federal Benchmark — Mission1

This repository is the durable evidence and methodological state for ASTRA Mission1. Read **research/research-state.json** first. Mission2 is synthesis and publication; no modeling application or publication-quality report is built here.

73 unique recent ICR package reviews include10 TSA collections across38 agency/component labels. The study asks whether another analyst can identify inputs, reproduce calculations, update estimates and defend assumptions. The sample is purposive, not representative of all federal ICRs.

| Purpose | Location |
|---|---|
| State and handoff | research/research-state.json; research/mission-2-handoff.md |
| Concise findings and limitations | research/research-summary.md; research/limitations.md |
| Dataset, scores and checks | data/icrs.csv; data/scores.csv; data/calculation-checks.csv |
| Structured models | data/model-sections.jsonl; icrs/*/extraction.json |
| Original evidence and tables | icrs/*/raw; icrs/*/table-evidence.json; raw |
| Source and claim provenance | data/sources.jsonl; data/claims.jsonl |
| Data sources and assumptions | data/data-sources.csv; data/assumptions.csv |
| Compliance, rubric and calibration | methodology/requirements-floor.md; methodology/rubric.md; methodology/calibration.md |
| Architecture and tool specification | methodology/canonical-model.md; methodology/canonical-data-dictionary.md; methodology/tool-requirements.md |
| TSA gaps and exemplars | methodology/tsa-comparison.md; methodology/exemplars.md |
| Sampling and saturation | methodology/sampling-strategy.md; logs; research/saturation-log.md |
| Validation and content hashes | research/final-validation.json; research/evidence-manifest.json |

BLS SOII has the strongest overall observed score83. TSA spans50–76, mean67.4; its flight-training Item12 model is close to the strongest examples. Other agencies contribute stronger change bridges, validation and particular cost methods. This does not establish a population agency ranking or the effect of TSA's reported overhaul.

Original source values are preserved when checks disagree. Correct arithmetic does not prove valid assumptions. Null means missing/not normalized, never zero. The dataset is an evidence foundation, not73 fully executable replacement models. Versions and limitations are in the handoff.
