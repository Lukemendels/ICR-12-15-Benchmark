# TSA consistency and defensibility technical report

Completed report: `final/TSA-ICR-Consistency-and-Defensibility-Report.pdf` (55 PDF pages including cover, contents, appendices and references). Reporting state and leadership-phase handoff are in `mission-4/`. No leadership brief was created.

## Evidence boundary

This report consumes the authoritative frozen repository at `b96aaaa4d81fe4df432602a0ae1346be78a151b1`, with Mission 3 evidence M3-1.0.0 and graph 1.0.0. All 2,189 original files retain their frozen Git blob identities. No new broad research or evidence re-adjudication was performed.

## Reproduce

Use a checkout containing the frozen evidence and this reporting directory. A standalone source archive must be overlaid into that checkout; it does not duplicate the frozen evidence corpus. Run from the repository root:

```bash
python -m pip install -r report/tsa-consistency/technical/scripts/requirements.txt
python report/tsa-consistency/technical/scripts/build.py
python report/tsa-consistency/technical/scripts/audit.py
```

The build requires DejaVu Serif and Sans fonts at `/usr/share/fonts/truetype/dejavu`. Runtime versions are in `audit/runtime.json`. `build.py` invokes `prepare.py` to derive tables, appendices and citation data from frozen records, then creates four figures and the searchable PDF. No research or frozen evidence validation scripts are executed. PDF and figure metadata timestamps may vary between builds; substantive values, classifications and layout are reproducible with the recorded environment.

Render a rebuilt PDF with Poppler for a new visual inspection:

```bash
pdftoppm -r 100 -png report/tsa-consistency/technical/final/TSA-ICR-Consistency-and-Defensibility-Report.pdf /tmp/tsa-report-page
```

The visual audit applies to its identified PDF hash, not automatically to future builds. Inspect every page after report changes.

## Deliverables and audit trail

- `source/report.md`: editable analytical manuscript.
- `source/appendices.md`: complete 32-comparison register, eight-case reconstruction register and terminology guide.
- `source/tables.json`, `tables/*.csv`: 13 report tables and supporting registers.
- `source/references.*`, `source/reference-registry.json`: 61 deduplicated scholarly references and source identities.
- `figures/`: PNG and vector PDF figures; generating source is in `scripts/build.py`.
- `audit/input-register.json`, `claim-source-locators.json`, `citation-use.json`: frozen inputs and claim-to-record-to-reference provenance.
- `audit/`: separate evidence, classification, quantitative, argument, causal-boundary, terminology, citation, figure/table and visual audit results, plus protected-file integrity.
- `audit/completion-audit.json`: final audit disposition and PDF hash.

## Qualifications that must survive reuse

The 32-record task/method register includes cross-ICR, lineage and selected within-package component comparisons. It is not 32 independent cross-program tests. The within-ICR register has seven potentially inconsistent cases and one unresolved valuation-scope case. These denominators do not establish portfolio prevalence. Pending and proposed evidence is identified. Published discrepancies are not official corrected totals or proof of internal causes. Counterevidence and source limitations must accompany compression. Only the registered TWIC baseline/component bridge is fully verified.
