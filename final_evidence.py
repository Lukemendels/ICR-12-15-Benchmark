from pathlib import Path
import json,hashlib,csv,re,datetime
R=Path(__file__).parent
p=R/'data/sources.jsonl';ss=[json.loads(l) for l in p.read_text().splitlines()]
for s in ss:
 sid=s['source_id'];lp=s.get('local_path')
 if sid in ['SRC-0024','SRC-0025','SRC-0030','SRC-0032']:
  s['initial_archive_path']=lp;s['local_path']='raw/guidance/current-source-verification.json';s['retrieval_status']='Official page verified through web retrieval; extracted result archived';s['archive_format']='Web retrieval result; locate the source URL within JSON';s['notes']=(s.get('notes') or '')+' Initial direct fetch was incomplete or blocked; final web verification supersedes initial retrieval status. eCFR displayed title5 current through2026-09-04.'
 if sid=='SRC-0162':s['local_path']='raw/methods/epa-yeast-2017-extraction.json';s['archive_format']='Structured researcher extraction from official web-readable PDF; original binary403';s['retrieval_status']='Partial archive; source text inspected, binary unavailable'
 if sid=='SRC-0163':s['local_path']='raw/methods/cmmc-final-rule-2024.txt';s['archive_format']='Extracted text from paired official PDF SRC-0164; original HTML URL retained';s['publisher']='GPO/Federal Register'
 if sid=='SRC-0191':s['locator']='85FR31598–31613; methodological Tables1–24; rendered pp31605/31611 inspected'
 lp=s.get('local_path')
 if s.get('sha256'):
  s['original_sha256']=s.pop('sha256');s['hash_note']='Original downloaded-byte hash, where previously recorded; archive may be a text transformation. Use archive_sha256 for local file integrity.'
 if lp and (R/lp).exists():s['archive_sha256']=hashlib.sha256((R/lp).read_bytes()).hexdigest();s['archive_bytes']=(R/lp).stat().st_size
 else:s['archive_sha256']=None;s['notes']=(s.get('notes') or '')+' No complete local original. Treat as catalog/citation evidence at the recorded access depth.'
 if s.get('year') is None and s.get('publication_date'):
  m=re.search(r'(?:19|20)\d{2}',s['publication_date']);s['year']=int(m.group()) if m else None
 if not s.get('notes'):s['notes']='Official package/source metadata; dates as supplied, missing dates not inferred.'
p.write_text(''.join(json.dumps(s,ensure_ascii=False)+'\n' for s in ss))
# Additional recurring assumption types are applications of the existing model.
p=R/'data/assumptions.csv';rows=list(csv.DictReader(p.open()));fields=list(rows[0])
new=[
('manager_legal_review','Observed approval routing; role-hour shares; expert task estimates','Time logs or sample of completed reviews with task boundaries','Unexplained management percentage applied to all hours','Agency workflow; occupation/task studies','Use when substantive review occurs; do not duplicate preparation','202405-0704-002;202508-1218-005'),
('IT_implementation','Staged staff roles; system budget; vendor quote','Scoped implementation tasks, procurement contract and asset life','Fee revenue used as system cost; total program capital copied into PRA','Agency procurement; system lifecycle budgets','Separate one-time build, annual O&M, respondent effort and federal systems','202405-0704-001;202405-0704-002'),
('federal_allocation','Shared platform cost divided by collections; FTE workload shares','Causal usage driver with numerator and complete denominator','Equal split without usage evidence; unallocated program budget','Agency cost accounts; workload systems','Shared platforms; avoid treating funding source as zero resource cost','202412-1205-002;202505-2060-004'),
('discount_annualization','Straight-line or capital recovery annuity with useful life','Documented principal, life, discount convention and replacement schedule','Unexplained annualized number or approval-period division','EPA engineering workbooks; asset inventories','Use real rates with real prices; distinguish annualized resource cost and cash flow','202502-2060-039'),
('case_conversion','Observed cases-to-filings ratio; borrowed industry ratio','Dated event funnel from same population, including nonfiling decisions','Large-bank average extrapolated to all institution types','Administrative case logs; representative industry survey','Security screening and compliance reviews; one case may generate multiple reports','202405-1506-005'),
('cohort_horizon','Year-specific populations; month overlap of reporting cycles','Explicit start/end dates, cohort eligibility and sunset','Rounded.33/.67 substituted without precision; annual flow divided by3','Program schedule; registry cohorts','Reporting periodicity can exceed approval horizon','202401-2070-005;202603-0535-001')]
for vals in new:
 if not any(x['type']==vals[0] for x in rows):rows.append(dict(zip(fields,[f'ASM-{len(rows)+1:04d}',*vals])))
with p.open('w') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
# Historical FinCEN table transcription from rendered source; independent of current aggregate.
(R/'raw/methods/fincen-sar-2020-table-extraction.json').write_text(json.dumps({'source_id':'SRC-0191','locator':'printed31605 Table7; printed31611 Tables21–22 (PDFpages8,14)','extraction_method':'Rendered PDF visually inspected; manual numeric transcription','case_conversion':.42,'original_sars':2335559,'continuing_sars':416135,'case_minutes':{'original':20,'continuing':3,'declined':25},'recordkeeping_minutes':{'batch':5,'discrete':15},'filing_minutes':{'continuing_batch':20,'continuing_discrete':40,'original_standard_batch':40,'original_standard_discrete':60,'original_extended_batch':200,'original_extended_discrete':300},'table22_columns':['activity','hours','cost'],'table22_rows':[['case review',3218296,130819064],['recordkeeping',301183,7228392],['continuing reporting',157844,5524540],['nondepository standard',728133,25484655],['nondepository extended',25425,966150],['depository standard',927774,32472090],['depository extended',103371,3928098]],'reported_hours':5462026,'reported_cost':206422989,'limitation':'Historical segmented source;2024renewal does not update these segment weights.'},indent=2))
print('Registry',len(ss),'assumptions',len(rows))
