from pathlib import Path
import json,csv,concurrent.futures,hashlib
from retrieve import get,clean
R=Path(__file__).parent
entries=[
('EIA CBECS','Energy Information Administration','https://www.eia.gov/consumption/commercial/data/2018/','2018 Table B1 and detailed building characteristics','Buildings; floorspace; workers; relative standard errors','12;13','Periodic survey; preserve release and revision dates','None','Building activity','National and census region','Building/asset proxy is not respondent count; sampling uncertainty','Floorspace divided by supported equipment coverage; customary-use share separately','202405-1218-005'),
('EIA MECS','Energy Information Administration','https://www.eia.gov/consumption/manufacturing/','Manufacturing Energy Consumption Survey','Establishments; floorspace; energy use','12;13','Quadrennial survey program','None','NAICS manufacturing','National and regions','Different scope from commercial buildings; avoid overlap','Align manufacturing/nonmanufacturing population definitions','202405-1218-005'),
('BLS Employment Projections','Bureau of Labor Statistics','https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm','Table1.2 occupational projections and National Employment Matrix','Employment; projected growth; openings','12;15','Annual projections release','SOC','NAICS via employment matrix','National','Projection is a scenario; openings differ from net growth or respondent entries','Annualize growth geometrically; preserve projection base and horizon','202405-1652-001'),
('BLS CES','Bureau of Labor Statistics','https://www.bls.gov/ces/','Current Employment Statistics earnings series','Employment; average hourly earnings; weekly hours','12;15','Monthly with revisions','All employees or production/nonsupervisory; not SOC','Industry','National; state/metro in separate program','Earnings not benefits; worker universe differs from household respondents','Preserve series ID and seasonal adjustment; do not substitute for task-specific occupation without reason','202405-1220-001'),
('BLS PPI','Bureau of Labor Statistics','https://www.bls.gov/ppi/','Producer Price Index industry and commodity series','Producer price indexes','13;15','Monthly with revisions','None','Industry/commodity','National','Producer prices differ from consumer purchases and wages; product match essential','Cost_new=cost_base*index_new/index_base; preserve seasonal status','202501-1210-006'),
('Census ASM','U.S. Census Bureau','https://www.census.gov/programs-surveys/asm.html','Annual Survey of Manufactures historical tables','Operating expenses; employment; payroll; value of shipments','12 overhead;13','Historical annual series; check transition to AIES','None','NAICS manufacturing','National and selected states','Expense categories include direct inputs; not all are overhead','Remove excluded direct costs; allocate supported expense categories by labor/industry matrix','202501-1210-006'),
('Census SAS','U.S. Census Bureau','https://www.census.gov/programs-surveys/sas.html','Service Annual Survey historical expense tables','Revenue; operating expenses','12 overhead;13','Historical annual series; check transition to AIES','None','Service industries','National','Industry averages are not marginal collection cost; coverage changed','Allocate selected overhead expense, then divide by employment and hours','202501-1210-006'),
('OPM salary tables','Office of Personnel Management','https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/','Annual GS base and locality pay tables','Grade; step; annual and hourly rates','14','Annual; special pay tables separately','Grade/step','Federal','Locality pay areas','Salary excludes benefits; locality must match federal workforce','Use published hourly rate or declared annual denominator; keep benefits separate','202404-2120-002'),
('EPA CEMS model','US EPA','https://www.epa.gov/sites/default/files/2020-08/19-cems.xls','2007 CEMS cost workbook; Costs/Activities/SummaryInfo','Capital principal; O&M; installation; life; discounting','13;14','Historical method, not current prices','Task roles in model','Emission monitoring equipment','Engineering model','Defaults outdated; model includes labor and regulatory scope beyond PRA','Capital recovery P*r/(1-(1+r)^(-n)); cohort and source prices separate','202502-2060-039')]
p=R/'data/sources.jsonl';sources=[json.loads(l) for l in p.read_text().splitlines()];byurl={x['url']:x for x in sources}
def fetch(e):
 if e[2] in byurl:return e,None,None
 try:return e,get(e[2]),None
 except Exception as ex:return e,None,str(ex)
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(fetch,entries))
p=R/'data/data-sources.csv';rows=list(csv.DictReader(p.open()));fields=list(rows[0])
for e,b,err in results:
 name,publisher,url,dataset,variables,use,freq,occ,ind,geo,limits,transform,examples=e
 if url in byurl:s=byurl[url]
 else:
  s={'source_id':f'SRC-{len(sources)+1:04d}','authoring_entity':publisher,'title':name+' — '+dataset,'year':None,'publication_date':None,'document_type':'Official quantitative data program documentation','omb_control_number':None,'url':url,'publisher':publisher,'retrieved_date':'2026-09-09','locator':dataset,'notes':'Catalog documentation, not a new empirical ICR or new source category.'}
  if b:
   q=R/'raw/data-sources'/f"{s['source_id']}.txt";q.write_text(clean(b.decode('utf-8',errors='replace')));s.update(local_path=str(q.relative_to(R)),original_sha256=hashlib.sha256(b).hexdigest(),retrieval_status='archived extracted official HTML')
  else:s.update(retrieval_status='binary fetch failed',retrieval_error=err,local_path=None)
  sources.append(s);byurl[url]=s
 if not any(x['name']==name for x in rows):rows.append(dict(zip(fields,[s['source_id'],name,publisher,url,dataset,variables,use,freq,occ,ind,geo,limits,transform,'Publisher; dataset/series/table; reference period; release vintage; row; URL; transformation',examples])))
for x in rows:
 if x['source_id']=='SRC-0032':x['example_icrs']='202505-1218-008;202508-1218-005'
# Case-level administrative and contract sources remain usable even where microdata are nonpublic.
for sid,name,dataset,variables,uses,limits,examples in [
('SRC-0187','EPA RMP administrative extract','March2025 RMP facility extract','Facilities; processes; chemical coverage; employment','12;15','Public source description; exact filtered extract unavailable; PSM and RMP coverage differ','202508-1218-005'),
('SRC-0174','USCG MISLE administrative extract','Security-plan population counts','Vessels; facilities; security plans','12;15','Underlying query not public; record date and filters before reuse','202408-1625-012'),
('SRC-0185','FinCEN BSA E-Filing statistics','Calendar2022 SAR submissions','Unique filers; reports; categories','12;15','Microdata restricted; published aggregates are reproducible inputs but not independently queryable','202405-1506-005'),
('SRC-0144','ETA state UI funding workload','FY2025 UIPL19-24 allocation assumptions','Salary; productive hours; workload','12;14','Productive1711hours denominator is not generic federal2080/2087; program allocation basis required','202412-1205-002'),
('SRC-0164','CMMC system and vendor cost evidence','RIA cost tables and eMASS historical budgets','Contract rates; systems O&M; staged assessment labor','12;13;14','Vendor profit and internal resource cost differ; capital may contain labor already in12','202405-0704-001;202405-0704-002')]:
 s=next(x for x in sources if x['source_id']==sid)
 if not any(x['name']==name for x in rows):rows.append(dict(zip(fields,[sid,name,s['authoring_entity'],s['url'],dataset,variables,uses,'Administrative/program-specific; freeze extract date','Case-specific roles','Program-specific','Program coverage',limits,'Preserve query filters, activity scope, price year, allocation denominator and access status','Agency; system/report; extraction date; query definition; supporting-statement locator',examples])))
with p.open('w') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
(R/'data/sources.jsonl').write_text(''.join(json.dumps(s)+'\n' for s in sources))
print('catalog',len(rows),'sources',len(sources),'new failures',[(e[0],err) for e,b,err in results if err])
