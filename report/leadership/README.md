# Leadership brief

Primary output: [Federal-ICR-12-15-Benchmark-Findings-and-Recommendations.pdf](final/Federal-ICR-12-15-Benchmark-Findings-and-Recommendations.pdf).

Separate editorial derivative of the complete technical report. Source report and frozen research are unchanged.

- `edit-diagnosis.md`: pre-draft editorial decisions.
- `source/brief.md`: narrative with internal citation tokens and explicit page boundaries.
- `source/render.py`: PDF authoring and footnote/reference generation; requires ReportLab and Matplotlib (bundled DejaVu fonts).
- `source/citation-registry.json`, `references.json`, `references.md`: cited-source traceability.
- `internal-metadata.json`: evidence/report pins and artifact hashes; never rendered.
- `audit/`: evidence, editorial, PDF bounds and layout review.

Run `python3 report/leadership/source/render.py` from the repository to regenerate. The renderer reads the existing technical reference registry and writes only under report/leadership. Its sole figure and both tables are generated from the source; no copied technical figures are needed.
