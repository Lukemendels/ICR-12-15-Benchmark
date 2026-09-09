# U.S. Business Income Tax Returns

Reviewed under rubric1.0.0. 202511-1545-005; sources SRC-0093, SRC-0094, SRC-0100, SRC-0101.

Score 73/100. Single-analyst public-evidence assessment; small score differences are not meaningful agency rankings.

## Scoring

- reproducibility: 12/20. Aggregate and change arithmetic are reproducible, but model coefficients and microdata are not available in this package.

- provenance: 11/15. Tax-year survey, model update, legal cutoff and economic inputs identified; coefficient-level provenance incomplete.

- segmentation: 15/15. Entity type, size, receipts, preparation method and tax complexity are explicitly modeled.

- labor: 7/10. Economic-value methodology has floor and ceiling tied to wage/compensation data; exact function and inputs are not exposed.

- item13: 7/10. Survey/model estimates include preparer fees and software; aggregate out-of-pocket estimate lacks public reconstruction coefficients.

- item14: 6/10. 383 product allocations supplement the cost estimate; processing subtotal does not add and several federal categories are excluded.

- item15: 9/10. Separates technical recalibration, projection and legislation with quantified time and dollar changes; ROCIS classification needs reconciliation.

- validation: 4/5. Business taxpayer survey anchors the model; uncertainty and validation performance are not reported in this statement.

- consistency: 2/5. Main time and dollar bridges reconcile; federal processing sum is inconsistent.

## Reconstruction issues

- Public statement and accessible supplements do not expose coefficients needed to regenerate the statistical burden estimates.

- Paper processing 9655592 plus electronic 2601760 equals 12257352, versus reported 13571960.

- Technical versus legislative analytical labels must be mapped explicitly to ROCIS program-change and adjustment categories.

## Methods worth testing

- Maintain statistical model version, calibration population, coefficients, legal cutoff and access restrictions as first-class model entities.

- Item 15 can distinguish real obligation changes from model recalibration, projection updates and redistribution between time and purchased services.
