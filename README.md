# Federal ICR Items 12-15 benchmark

**Mission 2: REPORT_COMPLETE** - [Read the analytical report](report/final/ICR-12-15-Benchmark-Report.pdf).

This study benchmarks observable federal Supporting Statement A methodology, with TSA as the principal application case. The purposive evidence base contains 73 unique recent controls, 38 agency/component labels and ten TSA collections. It supports methodological comparison, not agency population rankings or conclusions about undisclosed internal work.

## Research sequence

1. **Mission 1 - Federal benchmark evidence.** Frozen release `M1-1.0.0`, rubric `1.0.0`, canonical model `0.5.0`, at commit `16aeb85d976eb3a89ecb3872d4dda94753e77cd3`. The authoritative Mission 1 state remains `EVIDENCE_FROZEN`.
2. **Mission 2 - Analytical report.** Synthesis, quantitative comparisons, source-traceable footnotes, TSA actions and future modeling requirements. Final status, evidence pin and artifact hash: [report metadata](report/final-metadata.json).
3. **Future Mission 3 - TSA evidence graph and consistency analysis.** Compare assumptions across similarly shaped TSA collections, then retrieve useful federal analogues. Not implemented here.
4. **Future application - Evidence-grounded ICR modeling and review.** Structured model to validated calculations to defensible Excel to Supporting Statement narrative. Not implemented here.

## Read and reproduce

| Purpose | Location |
|---|---|
| Primary PDF | [Final report](report/final/ICR-12-15-Benchmark-Report.pdf) |
| Editable source and build instructions | [Report README](report/README.md); report/source; report/scripts |
| Figures and exact figure data | report/figures; report/figure-data |
| Normalized comparisons and classifications | report/tables |
| Report audit trail | report/audit |
| Frozen state and handoff | research/research-state.json; research/mission-2-handoff.md |
| Frozen dataset, scores and checks | data/icrs.csv; data/scores.csv; data/calculation-checks.csv |
| Structured extraction and archived sources | data/model-sections.jsonl; icrs; raw |
| Source/claim registries | data/sources.jsonl; data/claims.jsonl |
| Frozen methods and limitations | methodology; research/limitations.md |
| Freeze validation and hashes | research/final-validation.json; research/evidence-manifest.json |

The report finds strong TSA activity, occupation and cohort methods alongside distinct public reconstruction risks. Useful frontier practices are distributed across federal collections. No unique agency superiority or effect of recent internal TSA process changes is established.

All Mission 1 evidence files remain unchanged. This README is the authorized navigation update; its historical frozen version remains accessible at the evidence commit. Mission 2 adds report artifacts and separately documents two frozen-record qualification issues without changing checks or scores. Null remains missing/not normalized, never an inferred zero.
