# Mission 2 - Federal ICR benchmark report

Primary artifact: [ICR-12-15-Benchmark-Report.pdf](final/ICR-12-15-Benchmark-Report.pdf).

Evidence is pinned to Mission 1 release **M1-1.0.0**, commit `16aeb85d976eb3a89ecb3872d4dda94753e77cd3`; rubric **1.0.0**, canonical model **0.5.0**. Mission 1 state remains EVIDENCE_FROZEN. Mission 2 status is separately recorded in `final-metadata.json`.

- `source/report.md`: editable narrative, with stable source-ID/locator tokens.
- `source/report-resolved.md`: assembled report with deterministic footnotes and references.
- `source/appendices.md`: generated detailed tables/catalogs.
- `source/references.json` and `source/citation-registry.json`: exact canonical metadata plus display overlays and first-use tracking.
- `figures` and `figure-data`: three publication figures and their exact data.
- `tables`: full benchmark, 657 dimension rationales, normalized risk/action/requirement records, and canonical entities.
- `audit`: quantitative, citation, evidence, argument, audience and visual checks.

## Rebuild

From the repository root, run:

```bash
python report/scripts/analyze.py
python report/scripts/publish.py
```

Dependencies: Python with pandas, numpy and matplotlib; Pandoc; XeLaTeX; DejaVu Serif/Sans fonts and standard LaTeX packages. `report/scripts/normalize.py` prepares report-specific classifications and checks a materialized frozen snapshot; it is a preparation step and should be run on the frozen README before the authorized Mission 2 README update. It is not required for a normal render.

Do not modify `data`, `methodology`, `icrs`, `raw`, `research`, or historical logs to update this report. Two frozen-record qualification issues are disclosed in Appendix E and the audit log. Correcting their canonical records requires a new evidence release. Reproducibility here means the reported comparisons and document generation, not complete replication of every agency's internal model.

Later work may construct a TSA evidence graph and evaluate similarly shaped collections. No graph or future ICR modeling application is built in Mission 2.
