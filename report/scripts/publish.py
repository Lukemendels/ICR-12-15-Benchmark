from pathlib import Path
import json,csv,re,hashlib,subprocess
import pandas as pd
R=Path(__file__).resolve().parents[2];O=R/'report';REF='16aeb85d976eb3a89ecb3872d4dda94753e77cd3';BASE='https://github.com/Lukemendels/ICR-12-15-Benchmark/blob/'+REF+'/'
S={j['source_id']:j for j in map(json.loads,(R/'data/sources.jsonl').read_text().splitlines())}
I=pd.read_csv(R/'data/icrs.csv');D=pd.read_csv(O/'tables/benchmark-comparison.csv');src_icr={sid:r for _,r in I.iterrows() for sid in r.source_ids.split(';')}
# Display titles are editorial descriptions; canonical titles are preserved in references.json.
for sid,j in S.items():
 if j.get('document_type')=='Supporting Statement A' and sid in src_icr:j['display_title']='Supporting statement A: '+src_icr[sid]['title']
 else:j['display_title']=j['title'].replace('_',' ').removesuffix('.pdf').removesuffix('.docx')
 j['short_title']=(src_icr[sid]['title'] if sid in src_icr and j.get('document_type')=='Supporting Statement A' else j['display_title'])
 if len(j['short_title'])>74:j['short_title']=j['short_title'][:71].rsplit(' ',1)[0]+'...'
# Citation-friendly expansions never alter the frozen registry.
authors={'DHS/TSA':'Transportation Security Administration','DOL/BLS':'Bureau of Labor Statistics','DOC/CENSUS':'U.S. Census Bureau','DOL/OSHA':'Occupational Safety and Health Administration','DOL/EBSA':'Employee Benefits Security Administration','DHS/USCG':'U.S. Coast Guard','TREAS/FINCEN':'Financial Crimes Enforcement Network','TREAS/IRS':'Internal Revenue Service','FCC':'Federal Communications Commission','SEC':'Securities and Exchange Commission'}
authors.update({'DOL/ETA':'Employment and Training Administration','EPA/OCSPP':'U.S. Environmental Protection Agency','Treasury/FinCEN':'Financial Crimes Enforcement Network','USDA/NASS':'National Agricultural Statistics Service','U.S.Census Bureau':'U.S. Census Bureau'})
for sid,title in {
'SRC-0024':'5 CFR 1320.3: Definitions', 'SRC-0025':'5 CFR 1320.8: Agency collection responsibilities',
'SRC-0026':'Job Openings and Labor Turnover Survey: Frequently asked questions',
'SRC-0027':'May 2023 occupational employment and wage estimates: Rail transportation (NAICS 482000)',
'SRC-0028':'Employer Costs for Employee Compensation: June 2025',
'SRC-0029':'Salary Table 2025-DCB', 'SRC-0030':'Geographic mobility: 2023 tables',
'SRC-0031':'Employment Cost Index', 'SRC-0032':'County Business Patterns',
'SRC-0033':'Gross domestic product price index', 'SRC-0034':'Estimating burden',
'SRC-0192':'Commercial Buildings Energy Consumption Survey: 2018 data',
'SRC-0193':'Manufacturing Energy Consumption Survey',
'SRC-0194':'Employment Projections: Occupational projections and characteristics',
'SRC-0195':'Current Employment Statistics', 'SRC-0196':'Producer Price Indexes',
'SRC-0197':'Annual Survey of Manufactures', 'SRC-0198':'Service Annual Survey',
'SRC-0199':'Salaries and wages: Salary tables',
'SRC-0181':'Security-plan burden calculation supplement: Appendices A-B',
'SRC-0200':'Employer Costs for Employee Compensation: September 2023'
}.items():
 S[sid]['display_title']=title;S[sid]['short_title']=title
def full(sid):
 j=S[sid];author=authors.get(j.get('authoring_entity'),j.get('authoring_entity',''));year=j.get('year') or 'n.d.';control=f" (OMB Control No. {j['omb_control_number']})" if j.get('omb_control_number') else ''
 return f"{author}. ({year}). *{j['display_title']}*{control}. {j.get('publisher','')}. <{j['url']}>."
# Appendices: exact fields with explicit source notes; citations added before exhaustive material.
a=[]
def add(t):a.append(t)
def table(headers,rows):
 def esc(t):
  t=str(t).replace('\n',' ')
  return ''.join({'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_\allowbreak{}','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}','/':r'/\allowbreak{}'}.get(c,c) for c in t)
 n=len(headers)
 if headers[0]=='ICR reference':w=[.19,.14,.48,.12,.07]
 elif headers[0]=='ICR':w=[.25]+[.075]*10
 elif headers==['Entity','Principal fields','Relationship/control']:w=[.20,.37,.43]
 elif headers[0]=='TSA ICR':w=[.28,.18,.32,.22]
 elif headers[0]=='Component':w=[.34,.08,.15,.15,.15,.13]
 elif headers[0]=='ID':w=[.17,.24,.59]
 elif headers[0]=='Case':w=[.21,.37,.42]
 elif headers[0]=='Dimension':w=[.25,.09,.66]
 else:w=[1/n]*n
 spec='@{}'+''.join(r'>{\raggedright\arraybackslash}p{\dimexpr '+str(v)+r'\linewidth-2\tabcolsep\relax}' for v in w)+'@{}'
 head=' & '.join(r'\textbf{'+esc(v)+'}' for v in headers)+r' \\'
 body='\n'.join(' & '.join(esc(v) for v in row)+r' \\' for row in rows)
 return '\n'+r'\begingroup\fontsize{9.5}{11.8}\selectfont'+'\n'+r'\begin{longtable}{'+spec+'}\n'+r'\toprule'+'\n'+head+'\n'+r'\midrule\endfirsthead'+'\n'+r'\toprule'+'\n'+head+'\n'+r'\midrule\endhead'+'\n'+r'\bottomrule\endfoot'+'\n'+body+'\n'+r'\end{longtable}\endgroup'+'\n'
add('\\newpage\n\n# Appendix A. Complete reviewed sample\n\nAll 73 observations are shown in agency/ICR order, not score order. Dates are actual OIRA receipt dates; the ICR reference prefix is not a submission date. Scores are within-sample public reconstruction judgments. Full titles, archetypes, complexity, relevance, and source IDs are preserved in `report/tables/benchmark-comparison.csv`.[@M1|data/icrs.csv; data/scores.csv]\n')
rows=[]
for _,r in D.sort_values(['agency','icr_id']).iterrows():rows.append([r.icr_id,r.agency,r.title,r.submission_date,int(r.total)])
add(table(['ICR reference','Component','Collection','Received','/100'],rows))
add('\n\n# Appendix B. Rubric and dimension scores\n\nThe frozen rubric retains nine dimensions and 100 total points. Full credit requires the standard below; approximate anchors are 25% for an asserted total, 50% for partial reconstruction with material gaps, and 75% for mostly reconstructable work with bounded gaps. Explicit justified zeros remain eligible for full credit.[@M1|methodology/rubric.md]\n')
add(table(['Dimension','Max.','Full-credit standard'],[
['Reproducibility',20,'Disclosed inputs, units, frequency, annualization, and rounding support total reconstruction.'],['Provenance',15,'Material inputs identify source, dataset, codes, dates, geography, and transformations.'],['Segmentation',15,'Meaningful respondent and task variation is represented without gratuitous complexity.'],['Labor',10,'Occupation, wage, benefits, overhead bases, and transformations are defensible.'],['Item 13',10,'Applicable purchases and capital reconstruct; zero is justified where appropriate.'],['Item 14',10,'Attributable Federal workload and resources reconstruct, or zero is defensible.'],['Item 15',10,'Old/new bridge identifies changes, reasons, classifications, and effects.'],['Validation',5,'Assumptions have proportionate empirical support or justified uncertainty.'],['Consistency',5,'Tables, prose, package totals, and baseline agree within explained tolerances.']]))
add('\n## Full dimension scores\n\nR=reproducibility; P=provenance; S=segmentation; L=labor; V=validation; C=consistency. Maxima: 20, 15, 15, 10, 10, 10, 10, 5, 5. Each row is one ICR. All 657 dimension rationales and locators are preserved in the accompanying scoring table.[@M1|data/scores.csv; icrs/*/extraction.json]\n\n\\small\n')
cols=['reproducibility','provenance','segmentation','labor','item13','item14','item15','validation','consistency','total']
add(table(['ICR','R','P','S','L','13','14','15','V','C','Total'],[[r.icr_id]+[int(r[c]) for c in cols] for _,r in D.sort_values('icr_id').iterrows()]))
add('\\normalsize\n\n# Appendix C. Descriptive summaries and sensitivity\n\nAgency/component statistics describe only reviewed observations. A standard deviation of zero for n=1 contains no evidence about institutional consistency. Population-formula SD means division by the observed n, not a population inference. The sample is purposive and heterogeneous.[@M1|data/agency-summary.csv; methodology/calibration.md]\n')
G=pd.read_csv(R/'data/agency-summary.csv')
add(table(['Component','n','Mean','Median','Range','SD'],[[r.agency,int(r.n),f'{r["mean"]:.2f}',f'{r["median"]:.1f}',f'{int(r["min"])}-{int(r["max"])}',f'{r.population_sd:.2f}'] for _,r in G.iterrows()]))
add('\n## Sensitivity definitions\n\nThe cost-exclusion view is `(total - Item13 - Item14) / 80 × 100`; Item 12 is the sum of reproducibility, provenance, segmentation, and labor. Neither replaces the rubric. The table below shows all ten TSA cases; the machine-readable sensitivity file retains all 73.[@M1|data/score-sensitivity.csv]\n')
T=D[D.agency=='DHS/TSA']
add(table(['TSA ICR','Original /100','Excluding 13-14 /100','Item 12 /60'],[[r.icr_id,int(r.total),f'{r.excluding_13_14_rescaled:.2f}',int(r.item12_composite_out_of_60)] for _,r in T.iterrows()]))
add('\nAmong components with at least three reviewed ICRs, BLS has the highest observed mean (76.67; n=3), while Census has the narrowest observed dispersion (SD 1.41; n=3; range 71-74). These are descriptive sample results, not agency quality or consistency rankings.[@M1|data/agency-summary.csv]\n')
add('\n\n# Appendix D. Source and assumption catalogs\n\n## Source catalog\n\nThese 28 entries preserve the frozen catalog\'s analytical coverage. Update frequencies are as recorded in the release, not newly verified publication schedules. Citations identify the selected sources; administrative entries may describe an unavailable underlying query. Exact original fields remain in `data/data-sources.csv`.[@M1|data/data-sources.csv]\n')
# editorial summaries normalized for readable publication
catalog=[
('SRC-0024','Burden definitions','As amended; Federal scope. Map obligations to included and excluded activities, documenting usual/customary treatment. Cite section and paragraph. The regulation does not supply response times.'),
('SRC-0025','Agency estimation responsibilities','As amended; Federal scope. Identify the evidence supporting the estimate. Cite section and paragraph. Compliance with a process is not an accuracy guarantee.'),
('SRC-0026','JOLTS','Monthly flows, with annual revisions; industry and selected geographic detail, not occupation-specific turnover. Preserve series, denominator, reference period, and vintage. Do not treat a monthly flow as a unique annual probability.'),
('SRC-0027','OEWS','Annual occupational wages and employment, with SOC/NAICS and geographic detail. Select mean, median, or percentile deliberately; retain codes, year, and table. Wages exclude benefits and may be suppressed.'),
('SRC-0028','ECEC','Quarterly wages, benefits, and compensation for broad worker groups. Use direct compensation or an explicit matched ratio. Cite reference quarter, publication date, table, and row. Benefits are not overhead.'),
('SRC-0029','OPM 2025 DCB salary table','Annual grade/step pay for the Washington locality. Cite year, locality, grade, and step; document benefits and any hourly divisor. Salary is not a contractor rate.'),
('SRC-0030','CPS geographic mobility','Annual mobility by demographic and labor-force characteristics. Preserve affected population and denominator. Residential movement is not necessarily professional contact change and may overlap other events.'),
('SRC-0031','Employment Cost Index','Quarterly wage/compensation indexes for broad groups. Update a level by the ratio of matched periods. Cite series, quarters, seasonal status, and vintage. The index is not itself a wage observation.'),
('SRC-0032','County Business Patterns','Annual establishment, employment, and payroll counts by NAICS, size, and geography. Map the legal respondent unit explicitly. Cite year, industry, geography, and table; account for exclusions and suppression.'),
('SRC-0033','BEA GDP price index','Quarterly broad output-price indexes with revisions. Preserve NIPA table, line, periods, and release. A general price ratio may not represent equipment, IT, or labor cost change.'),
('SRC-0034','PRA burden guidance','Updated guidance on activities, loaded wages, and cost categories. Cite heading, URL, and retrieval date; interpret alongside regulations and the frozen instruction-conflict register.'),
('SRC-0102','EBSA overhead methodology','June 2019 method; input updates are separate. Allocate selected industry expenses through occupational employment, then divide by employment and hours. Preserve matrices, exclusions, and price years. Worked-example inconsistencies and average/marginal cost interpretation require review.'),
('SRC-0099','AIES burden measurement','One-time research supplement, printed p. 19. Retain sample, segment, statistic, and preparation/completion scope. The response-analysis survey, instrument, and paradata are not interchangeable measures of mean total effort.'),
('SRC-0094','Business taxpayer burden model','Annual updates and periodic calibration; entity and industry characteristics generate time and purchases. Preserve model version, calibration years, legal cutoff, and prediction inputs. Public coefficients/microdata are unavailable in the selected package.'),
('SRC-0192','EIA CBECS','Periodic commercial-building survey; the selected vintage is 2018. National/regional building and floorspace data can support asset proxies with explicit coverage assumptions. Cite table, vintage, and uncertainty; buildings are not respondents.'),
('SRC-0193','EIA MECS','Quadrennial manufacturing survey program with industry and regional detail. Align manufacturing and nonmanufacturing universes to avoid overlap. Cite reference year, table, release, and transformation.'),
('SRC-0194','BLS Employment Projections','Annual projections releases with SOC and employment-matrix detail. Preserve base and horizon; annualize growth geometrically where appropriate. Openings differ from net growth and new regulated entrants.'),
('SRC-0195','BLS CES','Monthly employment, earnings, and hours with revisions. Cite series and seasonal status. Industry earnings are not occupation-specific pay or benefits, and employee coverage may differ from respondents.'),
('SRC-0196','BLS PPI','Monthly industry/commodity price indexes with revisions. Apply a matched index ratio and retain series and price years. Producer prices are not automatically the relevant purchased-service, consumer, or wage index.'),
('SRC-0197','Historical Census ASM','Historical annual manufacturing expenses, employment, and payroll by industry. Exclude direct inputs before overhead allocation. Check transition to AIES when refreshing. The source page was inaccessible at freeze; this entry is not a claim of independent table validation.'),
('SRC-0198','Historical Census SAS','Historical annual service-industry revenue and expenses. Preserve expense categories and allocation denominators. Industry averages need not represent marginal collection costs; check coverage changes and AIES transition. Source-page access was blocked at freeze.'),
('SRC-0199','OPM salary tables','Annual base/locality schedules; special rates separately. Use a published hourly rate or a stated annual divisor. Cite year, locality, grade, and step. Benefits require separate support.'),
('SRC-0161','EPA CEMS cost workbook','Historical engineering method, not current prices. Retain principal, life, discounting, installation, and recurring-cost scope. Cite workbook sheet/cells. Separate labor and wider regulatory costs before PRA use.'),
('SRC-0187','RMP administrative population','March 2025 extract described in OSHA process safety. Preserve facility filters, chemical/process scope, and coverage adjustments. PSM and RMP universes differ; the exact filtered extract is not public.'),
('SRC-0174','MISLE security-plan population','Program-specific administrative counts described by the Coast Guard. Preserve extraction date, vessel/facility definitions, and query. Published counts do not expose the underlying query.'),
('SRC-0185','BSA E-Filing workload','Calendar 2022 SAR submissions described by FinCEN. Preserve unique filers, reports, categories, and case stages. Restricted microdata prevent independent querying of published aggregates.'),
('SRC-0144','ETA unemployment-insurance workload funding','FY2025 workload/funding assumptions. Preserve pay, workload, and productive-hours allocation; the 1,711-hour denominator is program-specific, not a universal Federal conversion.'),
('SRC-0164','CMMC system and vendor evidence','Final-rule labor, contract, and system cost tables. Separate staged assessments, internal staff, vendor prices, implementation, and recurring systems. Retain allocation denominators and avoid duplicating labor embedded in capital.')]
for sid,name,text in catalog:add(f'\n**{name}.** {text}[@{sid}|{next(x["dataset"] for x in csv.DictReader(open(R/"data/data-sources.csv")) if x["source_id"]==sid)}]\n')
assert len(catalog)==28
add('\n## Assumption catalog\n\nThe 24 recurring types below are a review checklist, not default parameter values. Each requires a justification, applicability boundary, source or expert basis, and review date. The full original strong/weak evidence descriptions are retained in `data/assumptions.csv`.[@M1|data/assumptions.csv]\n')
A=list(csv.DictReader(open(R/'data/assumptions.csv')))
assumptions=[('Response time','Task-matched timing; mode, sample, date, and distribution.'),('Population','Dated count with filters, coverage, and unique entity definition.'),('Frequency','Events per eligible entity per defined period; overlap treatment.'),('Pathway share','Dated mutually exclusive modes or explicit additive stages.'),('Familiarization','Text/task boundary, role, and entrant/update cohort.'),('Labor mix','Observed task roles or justified role-hour shares.'),('Wage selection','Occupation, industry, geography, statistic, vintage, and rationale.'),('Benefits','Matching worker universe and explicit denominator.'),('Overhead','Components, allocation base, nonoverlap, and cost interpretation.'),('Outsourcing','Dated price evidence and contract scope; no duplicated internal labor.'),('Capital life','Asset inventory, service life, and replacement schedule.'),('Usual/customary','Evidence of existing practice and obligation ownership.'),('Federal review','Workload, task time, compensation, and contract evidence.'),('Inflation','Index identity, base/target periods, and economic rationale.'),('Nonreporter determination','Potentially affected nonfilers and screening tasks.'),('Change classification','Named baseline, changed input/requirement, reason, and effect.'),('Measurement scope','Sample design, active/elapsed time, preparation, and statistic.'),('Statistical calibration','Model version, coefficients/access limits, and diagnostics.'),('Manager/legal review','Observed routing and boundaries distinct from preparation.'),('IT implementation','Scoped build, recurring operations, payer, and asset treatment.'),('Federal allocation','Usage driver with numerator and complete denominator.'),('Discount/annualization','Principal, life, rate convention, and price basis.'),('Case conversion','Dated funnel including decisions that do not produce filings.'),('Cohort/horizon','Start/end dates, eligibility, replacement, and sunset.')]
add(table(['ID','Assumption','Evidence/control'],[[r['assumption_id'],name,desc] for r,(name,desc) in zip(A,assumptions)]))
add('\n\n# Appendix E. Calculation checks and evidence qualifications\n\nAll 267 recorded expressions were replayed for this report. The table gives frozen numerical statuses, not defect prevalence. One collection can contribute multiple dependent checks, and some checks intentionally test a counterfactual or conflicting display. Read the interpretation and source before drawing a conclusion.[@M1|data/calculation-checks.csv; research/final-validation.json]\n')
add(table(['Frozen status','Expressions'],[['Exact',133],['Within display rounding',52],['Difference requires interpretation',82],['Total',267]]))
add('\n**Frozen-record qualification M2-OBS-001.** HME\'s pathway-share expression is 1.312 against 1, but the numerical label says within display rounding. The interpretation correctly flags apparent double counting. The report uses the semantic interpretation and does not alter the record or scores. Correcting the canonical status would require a new evidence version.[@M1|data/calculation-checks.csv, HME Agentpathway share]\n')
add('\n**Source-binding qualification M2-OBS-002.** The historical capital-recovery check is attached to SRC-0146 in the check table, while its inputs and method are documented in the frozen SRC-0162 extraction, with SRC-0161 providing related workbook methodology. This report cites those method sources directly and retains the reported $72,752 separately from $72,740.52 recomputed. It does not amend the frozen check binding. A canonical correction would require a new evidence version.[@M1|data/calculation-checks.csv, Capital recovery exemplar; raw/methods/epa-yeast-2017-extraction.json]\n')
add('\nThese issues limit automated interpretation of the status and citation fields; they do not change the reported score comparisons. The report\'s citation registry records the sources actually supporting its statements. No broad research was reopened, and no new evidence release was created.\n')
add('\n## Selected numerical distinctions\n')
add(table(['Case','Observed comparison','Interpretation'],[['Aircraft operators','Narrative $54,658; Table 2 $20,165,327','Inconsistent displayed values; possible copy/version issue.'],['Certified cargo','Components 6,049 h; subtotal 4,451 h','Confirmed displayed subtotal discrepancy; intended value unresolved.'],['HME pathways','Shares 1.312; mutually exclusive target 1','Potential scope duplication, not rounding.'],['Surface cybersecurity','Printed Federal rows 1,149 h; total 881 h','Displayed arithmetic discrepancy.'],['Airport applicant labor','$34.48 used; footnote gives about $50.19','Transformation/version ambiguity; not a verified corrected estimate.'],['Airport Federal costs','$921,400.97 recomputed; $921,402 reported','Small precision/reconciliation residual.'],['TWIC totals','One-hour and one-dollar differences','Rounding/precision questions, not evidence of material scope error.']]))
add('\nSources and locators for each row are cited in Sections 7 and 9 and preserved in `report/tables/reconstruction-risks.csv`. No corrected agency total is asserted.\n')
add('\n\n# Appendix F. Canonical entity contract\n\nVersion 0.5.0 contains the following 27 entities. These summaries preserve the frozen relationships; the authoritative dictionary supplies full fields and constraints. The model is a research architecture, not a completed implementation.[@M1|methodology/canonical-data-dictionary.md]\n')
entities=[]
for line in (R/'methodology/canonical-data-dictionary.md').read_text().splitlines():
 if line.startswith('|') and not line.startswith('| Entity') and not line.startswith('|---'):
  cells=[x.strip() for x in line.strip('|').split('|')]
  if len(cells)==3:entities.append(cells)
assert len(entities)==27
add(table(['Entity','Principal fields','Relationship/control'],entities))
add('\n## Reproduction and navigation\n\nRun `python report/scripts/analyze.py`, then `python report/scripts/publish.py`, from a checkout containing the pinned evidence and report source. The first script joins and checks the frozen tables and regenerates figure data and charts. The second resolves deterministic first-use footnotes and references, generates appendices, and renders the PDF with Pandoc and XeLaTeX. `report/audit` contains numerical, citation, argument, and visual review records. The report metadata records its evidence pin and output hash.\n')
add('\nThe report-specific comparison tables retain stable ICR and source IDs. They supplement the frozen release without replacing its extractions, scores, or research status. Future graph construction and modeling applications are separate work.\n')
appendices='\n'.join(a);(O/'source/appendices.md').write_text(appendices)
text=(O/'source/report.md').read_text()+'\n'+appendices
# Every citation occurrence carries a locator; source first-use state spans body and appendices.
seen={};notes=[];tracking=[]
pat=re.compile(r'\[@(SRC-\d{4}|M1)\|([^\]]+)\]')
def cite(m):
 sid,loc=m.groups();num=len(notes)+1;first=sid not in seen
 if sid=='M1':
  note=(f'*Federal ICR benchmark evidence release M1-1.0.0*. (2026). Rubric 1.0.0; canonical model 0.5.0. Repository commit `{REF}`. ' if first else '*Federal ICR benchmark*, M1-1.0.0. ')
  # Link to the first actual file, retain complete locator text.
  p=loc.split(';')[0].split(',')[0].strip()
  link=BASE+p if (R/p).is_file() else 'https://github.com/Lukemendels/ICR-12-15-Benchmark/tree/'+REF
  note+=(f'{loc}. <{link}>.' if first else f'[{loc}]({link}).')
 else:
  assert sid in S,sid
  note=full(sid) if first else f"{authors.get(S[sid].get('authoring_entity'),S[sid].get('authoring_entity',''))}, *{S[sid]['short_title']}*."
  note+=' '+loc+'.'
 seen.setdefault(sid,num);notes.append(f'[^{num}]: '+note);tracking.append(dict(footnote=num,source_id=sid,first_use=first,locator=loc,source_url=S[sid]['url'] if sid!='M1' else link))
 return f'[^{num}]'
text=pat.sub(cite,text);text=re.sub(r'(\[\^\d+\])(?=\[\^)',r'\1\\textsuperscript{,}',text);assert '[@' not in text
used=[sid for sid in seen if sid!='M1'];used.sort(key=lambda sid:(authors.get(S[sid].get('authoring_entity'),S[sid].get('authoring_entity','')),str(S[sid].get('year') or ''),S[sid]['display_title']))
refs='\n\\newpage\n\n# References\n\nOnly externally cited sources appear below. Display titles for supporting statements are editorial descriptions based on their registered collection titles; exact source titles, source IDs, dates, and URLs remain in the accompanying references registry. “n.d.” indicates that the frozen source registry has no publication year. Dates for statements may reflect recorded upload rather than authorship.\n\n'
refs+='\n\n'+r'\small'+'\n\n'+'\n\n'.join(r'\begingroup\interlinepenalty=10000\hangindent=1em\hangafter=1'+'\n\n'+full(sid)+f' [{sid}]'+'\n\n'+r'\par\endgroup' for sid in used)+'\n\n'+r'\normalsize'+'\n'
text+=refs+'\n\n'+'\n\n'.join(notes)+'\n'
(O/'source/report-resolved.md').write_text(text)
(O/'source/references.json').write_text(json.dumps([S[sid] for sid in used],indent=2,ensure_ascii=False)+'\n');(O/'source/citation-registry.json').write_text(json.dumps(tracking,indent=2,ensure_ascii=False)+'\n')
(O/'source/references.md').write_text(refs)
# Claim audit inventory ties each authored paragraph to evidence tags. Human disposition recorded separately.
raw=(O/'source/report.md').read_text();audit=[]
for i,p in enumerate(raw.split('\n\n'),1):
 if p.startswith('#') or not p.strip():continue
 audit.append({'block_id':f'BODY-{i:03}','text':p,'source_ids':list(dict.fromkeys(pat.findall(p)[k][0] for k in range(len(pat.findall(p))))),'locators':[v for _,v in pat.findall(p)],'type':'cited observation/synthesis' if pat.search(p) else 'interpretive framing/recommendation or adjacent cited exhibit','review':'checked against frozen methods, cited extracts, and machine-readable comparisons'})
(O/'audit/claim-audit.jsonl').write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in audit))
(O/'audit/citation-audit.json').write_text(json.dumps({'footnotes':len(notes),'external_sources':len(used),'all_sources_in_frozen_registry':True,'all_external_references_cited':True,'first_use_full_and_subsequent_short':True,'every_citation_has_locator':True,'source_metadata_policy':'Frozen dates preserved; descriptive statement titles mapped to canonical title; no inferred publication dates.','display_title_overlay':'report/source/references.json'},indent=2)+'\n')
cmd=['pandoc',str(O/'source/report-resolved.md'),'--from=markdown+footnotes+raw_tex','--to=latex','--standalone','--pdf-engine=xelatex','--resource-path='+str(R),'--metadata-file='+str(O/'source/metadata.yaml'),'--include-in-header='+str(O/'source/header.tex'),'--include-before-body='+str(O/'source/cover.tex'),'-o',str(O/'final/ICR-12-15-Benchmark-Report.pdf')]
p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);(O/'audit/render.log').write_text(p.stdout+p.stderr);print(p.stdout+p.stderr);assert p.returncode==0
print(json.dumps({'footnotes':len(notes),'external_sources':len(used),'pdf_bytes':(O/'final/ICR-12-15-Benchmark-Report.pdf').stat().st_size}))
