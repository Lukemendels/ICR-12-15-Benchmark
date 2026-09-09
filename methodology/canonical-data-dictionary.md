# Canonical quantitative data dictionary — v0.5.0

This describes the future model's data contract. It is not an implemented application. Each table belongs to a collection scenario/version unless explicitly shared. IDs are stable strings; numeric values retain decimal or rational precision, never only formatted text.

| Entity | Principal fields | Relationships and constraints |
|---|---|---|
| Collection | collection_id, OMB_control, component, title, authority, approval_lineage | Identity binds every table and narrative output. |
| Scenario | scenario_id, collection_id, baseline_id, policy_date, price_year, first_year, horizon, status | Approved, proposed and notice versions remain separate. |
| Source | source_id, author, title, publication_date, reference_period, URL, retrieval_date, hash, access_status | Citation-ready metadata; publication date differs from data reference period. |
| Evidence locator | locator_id, source_id, page, table, row, cell, quoted_value, extraction_method | A transformed input links to the original observation and its locator. |
| Population | population_id, unit_type, count, period, query_filters, source_id, coverage, exclusions | Persons, firms, establishments, sites, assets and events are distinct types. |
| Segment | segment_id, parent_population_id, eligibility_rule, share/count, overlap_type | Exclusive partitions sum to one; overlapping groups require an explicit union. |
| Obligation | obligation_id, legal_citation, activity_id, owning_control, exclusion/transfer_reason | Cross-control movements have source and destination entries. |
| Activity | activity_id, segment_id, task, trigger, mode, role_id, one_time_or_recurring | Atomically priced work; a purchased activity is not also charged as internal time. |
| Exposure/frequency | frequency_id, activity_id, events_per_period, periods_per_year, eligibility_share | Annualize rates only after reconciling periods and denominators. |
| Time estimate | time_id, activity_id, value, time_unit, statistic, scope, assumption_id | Mean, median, percentile and elapsed/active time cannot be interchanged. |
| Labor role | role_id, task_description, SOC, NAICS, locality, selection_reason | Industry employment weights are not automatically task labor shares. |
| Wage observation | wage_id, role_id, source_id, year, wage_statistic, base_rate, units | Preserve suppressed values and historical code changes. |
| Compensation method | compensation_id, wage_id, method_enum, benefit_value/share, denominator, reference_period | Direct compensation, wage markup and wage/compensation-share use different equations. |
| Overhead allocation | overhead_id, components, direct_cost_exclusions, industry_matrix, occupation_weights, annual_hours | Monetary units, average/marginal interpretation and potential double counting are explicit. |
| Price transformation | transform_id, input_id, index_series, base_period, target_period, ratio, rationale | Detect overlapping nominal updates; distinguish wage from output-price inflation. |
| Purchased service | service_id, activity_id, quantity, unit_price, price_scope, vendor_evidence, payer | Outside professional hours are a service quantity, not necessarily Item12 respondent hours. |
| Capital asset/cohort | asset_id, cohort_year, quantity, price, useful_life, replacement_rule, residual_value, annualization_method, discount_rate | Asset life, approval horizon and annual purchase flow are separate. |
| Federal activity | federal_activity_id, workload, time, grade/role, locality, benefits_method | Include only attributable resource use; explain zero or allocation. |
| Federal allocation | allocation_id, contract/system/budget_line, gross_cost, allocation_driver, fraction, fee_offset | Gross cost and net budget effect remain separate outputs. |
| Assumption | assumption_id, estimate_method, evidence_ids, justification, applicability, uncertainty, review_date | Unsupported does not mean zero; analyst judgment is identifiable. |
| Statistical model | model_id, version, equation/algorithm, coefficients, calibration_population, training_period, legal_cutoff, diagnostics, access_status | Can generate time and purchases jointly; restricted data limit public replication. |
| Validation observation | observation_id, target_input, method, sample_size, sample_frame, segment, task_scope, statistic, distribution | Distinguish empirical plausibility from spreadsheet arithmetic. |
| Formula | formula_id, expression_tree, input_ids, output_unit, rounding_rule, source_formula, observed_cache | Acyclic dependencies; deterministic evaluation; independent result versus cached value. |
| Change event | change_id, baseline_id, proposed_id, changed_input/obligation, reason, analytical_type, ROCIS_type, delta_by_metric | Old + program changes + adjustments = new, separately for responses, hours and nonlabor dollars. |
| Interaction/decomposition | decomposition_id, changed_inputs, update_order, interaction_term, counterfactual_values | Driver effects depend on order; store the convention rather than hiding interactions. |
| Validation result | check_id, formula/model_version, expected, actual, tolerance, status, severity, disposition | A known source defect is distinct from an extraction defect. |
| Output/narrative binding | output_id, semantic_item, table_cell/sentence, formula_ids, source_ids, scenario_id | Prose cannot invent numbers or inherit values from a different scenario. |

Core equations: annual hours = eligible population × events per eligible entity per year × time per event; labor dollars = sum(role hours × role compensation plus applicable overhead). Event-based and statistical models declare alternative equations rather than forcing every collection into this product.

Every output should preserve both the source-reported total and the independently calculated total where they differ. A corrected estimate is a separate analyst scenario; it must never replace the source evidence silently.
