# Canonical model v0.4.0 — provisional architecture
Inputs → assumptions → calculations → validation → output tables → Items 12–15 narrative.
This starting architecture reflects mission requirements, not an empirical conclusion.
Each scenario/version owns collection identity, analysis period, price year, annualization horizon, approval lineage and baseline reference.
Entities: population; segment; activity; population-activity eligibility; frequency; response; time-by-occupation; occupation/SOC; wage observation; benefit observation; loading method; capital asset; recurring purchase; federal activity; federal labor; contract/system allocation; assumption; source; formula; validation; change event; output.
Atomic input fields: stable ID, numeric value, unit, year/period, source ID and locator, extraction versus assumption flag, method, applicability, confidence and owner. Formula fields reference input IDs, preserve full precision, declare rounding only at output, and carry explicit units.
Hours = eligible population × responses/person/year × hours/response; alternative event-based activities explicitly use events/year. Labor = sum(hours by role × loaded hourly cost). Unique respondents must not equal a naive sum of overlapping activity populations.
Compensation alternatives remain separate: direct total compensation; wage × (total compensation/wages); wage + benefit amount; wage/(1-benefit share). A fraction of compensation is not a wage markup. Overhead requires its own base and nonoverlap check. Household time value is distinct from employer compensation.
Item 13: recurring purchases plus documented annualized capital; record useful life, discounting convention, price year, cohort timing, one-time versus recurring, exclusions and potential overlap with labor.
Item 14: incremental government hours × loaded pay plus nonduplicative contract/system/operating allocations. Keep gross cost, offsetting fees and net budget effect separate pending guidance evidence.
Item 15: versioned baseline + quantified program changes + quantified adjustments = proposed estimate, independently for responses, hours and nonlabor cost; labor dollar bridge separately. Interactions require a declared decomposition order or explicit interaction term. Withdrawn/expired approval baseline is not automatically identical to the last historical study baseline.
Outputs are deterministic tables and source-aware narrative. Missing input cannot be filled by prose generation. Validation must distinguish arithmetic accuracy, plausible assumptions, scope completeness and cross-record agreement.


## Empirical additions from iteration 1
An obligation ledger assigns each requirement to an ICR and identifies overlap, exclusions and cross-collection transfers. BLS SOII demonstrates why recording an existing OSHA obligation twice would misstate burden. Capture the justification, not only the exclusion flag.

A period field is mandatory for every rate. JOLTS separations are monthly flows, while residential mobility is annual; neither is automatically a probability that a specific employee needs a contact update. Store events, people, posts and establishments as different units, with explicit mappings.

Capital annualization needs procurement cohorts, asset useful life and the approval horizon as separate concepts. Dividing an annual purchase flow by the three-year approval period can understate annual cost. EPA CGP exposes the need to reconcile the workbook convention with its narrative.

Baseline identity must distinguish prior approved inventory, prior analytical estimate, earlier regulatory program baseline and new proposed estimate. Different deltas can both be correct when their bases differ. Changes between control numbers need a transfer ledger that prevents dropped or duplicate burden.

Arithmetic checks must go beyond cached Excel results. Compare formula meaning with labels, detect inverted rates and confirm frequency reaches both respondent and federal workload calculations. Preserve original formulas and observed cached values separately from independent recomputation.

Versioned source instructions may contain conflicting wording or question numbering. Maintain a guidance interpretation register and route narrative by semantic item identity. All explanatory dollar values must derive from the same model version as tables.

Revision history: 0.1.0 mission-derived initial architecture; 0.2.0 adds the above empirical requirements without claiming saturation.

## Iteration 2 additions
Pathway eligibility must explicitly distinguish mutually exclusive choices from additive activities. TSA HME exposes how adding an online-renewal subset after charging all applicants for in-person enrollment can duplicate burden. Validation requires partition shares to sum to one within the parent population, with explicit exceptions for overlapping activities.

Source transformations must preserve inflation index identity and economic rationale. CBP uses a GDP deflator to update occupational compensation; this is reproducible but should not be silently treated as equivalent to wage inflation.

Cost scope must separate gross collection costs, fee offsets, broader program savings and transfers. A claimed net saving cannot substitute for an unknown purchased-service price. Template text must inherit collection identity, legal authority and variable values from the same scenario as the tables.

Revision 0.3.0 adds partition validation, identity binding and gross-versus-net cost boundaries. No rubric weight change.

## Iteration 3 additions
Eligibility assessment by nonreporters is a distinct activity (EPA TRI). Store calibrated constants with the calibration dataset, reference period, model version and conditions requiring revalidation. Updating population alone does not validate a legacy time coefficient.

Overhead observations need component definitions and bases. EPA PCB exposes a factor containing profit; vendor prices and internal labor resource costs must retain their different economic meanings. Do not collapse them into one generic loading field.

Baseline types include the previous approved inventory, the public-notice proposal, and transferred requirements. FCC IPCS demonstrates exact reconciliation between both prior approval and a subsequently revised notice estimate.

Observed national data-source categories now include EIA building/manufacturing energy surveys as proxies for physical asset populations and BLS employment projections for forecast growth. Store proxy validity separately from source authority. Version0.4.0 is provisional; no saturation.
