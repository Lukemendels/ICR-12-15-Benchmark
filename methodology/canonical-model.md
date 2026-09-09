# Canonical model v0.2.0 — provisional architecture
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
