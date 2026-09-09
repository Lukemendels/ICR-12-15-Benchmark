# Research-derived tool requirements — provisional v0.5.0

This is a specification for later development. No modeling application has been built. Evidence references identify a useful method or observed failure; they do not endorse the entire collection.

| ID | Behavior | Empirical basis | Acceptance condition |
|---|---|---|---|
| TR-01 | Inputs carry source, locator, date, price year, unit and transformation. | TSA HME and CBP pipeline, SRC-0054/0044 | An input ledger traces the final value through all transformations. |
| TR-02 | Generate tables and prose from one model version. | CFPB HMDA, SRC-0052 | Title, legal authority and every total agree across outputs. |
| TR-03 | Preserve exact units and precision until display. | FRA HOS, SRC-0070 | Eight minutes remains 8/60 hours, not .13. |
| TR-04 | Distinguish unique respondents, responses, assets, sites and chemicals. | EPA TRI and OSHA extinguishers, SRC-0062/0060 | Repeated activity rows do not inflate unique respondents. |
| TR-05 | Validate exclusive pathways and overlapping occupations. | TSA HME and FMCSA HOS, SRC-0054/0074 | Partition shares sum to one; nested SOC groups are flagged. |
| TR-06 | Preserve alternative compensation methods and denominators. | TSA flight training, OSHA extinguishers, BLS NCS | Direct compensation and wage/compensation-share remain distinct. |
| TR-07 | Model overhead components, allocation bases and overlap. | EPA PCB and EBSA, SRC-0056/0102 | Industry-to-occupation matrices reproduce; profit is not silently treated as internal labor cost. |
| TR-08 | Maintain an obligation ledger across controls. | BLS SOII, FDA preventive controls, CMS hospital | Transfers and exclusions identify controls, baselines and effects. |
| TR-09 | Separate internal hours from outside services and preserve agency conventions. | OSHA extinguishers and EBSA claims | Outsourced activity is charged once; classification deviations are documented. |
| TR-10 | Separate gross resource cost, fees, offsets and broader benefits. | CBP pipeline, USCIS I-751, TSA fee programs | Unknown costs cannot be replaced by claimed savings. |
| TR-11 | Model capital stock, purchase/replacement cohorts, life and horizon. | EPA CGP and FMCSA ELDs | Annual purchases are not divided by approval years without justification. |
| TR-12 | Federal costs expose workload and contract/system allocations. | TSA aircraft operator, FCC satellite, PHMSA approvals | Staff counts multiply hours and narrative rates match tables. |
| TR-13 | Generate separate bridges for responses, hours and Item 13 dollars. | FCC IPCS, SRC-0064 | 6690 + 5900 + 1760 + 825 = 15175, with reasons and classifications. |
| TR-14 | Maintain multiple named baselines. | FCC notice revision and FERC amendment | Notice, approval and analytical baselines are never silently substituted. |
| TR-15 | Support statistical model nodes alongside workload equations. | IRS business tax, SRC-0094 | Coefficients, calibration, restricted inputs and replication evidence are inventoried. |
| TR-16 | Store validation observations with measurement scope. | Census AIES, SRC-0099 printed page 19 | Sample, segment and statistic accompany observations; means and medians remain distinct. |
| TR-17 | Separate model recalibration from requirement changes. | IRS Item 15 | Time-to-purchased-service redistribution appears in the change ledger. |
| TR-18 | Identify stale sources and unsupported assumptions. | EPA TRI constants and TSA HME growth | Refresh reports distinguish old evidence from unsupported extrapolation. |
| TR-19 | Check workbook formulas independently of caches. | EPA CGP, SRC-0023 | Formula, cached value and independent result are retained. |
| TR-20 | Distinguish zero, missing and not applicable. | SEC interactive data versus BLS SOII | Deferred federal cost remains missing; a justified zero can earn full credit. |

Narrative generation must mark unresolved material inputs for analyst judgment. Defaults should preserve evidence without encouraging unsupported precision.
