from pathlib import Path
import json,urllib.request,concurrent.futures,hashlib,csv,datetime,sys
from retrieve import clean
R=Path(__file__).parent
entries=[
('5CFR1320.3','Office of Management and Budget','https://www.ecfr.gov/current/title-5/chapter-III/subchapter-B/part-1320/section-1320.3','Definitions,burden andscope','Burden inclusions;usual/customary exclusions;ten-person definition','12,13','As amended','none','none','Federal','Scope definitions do not supply actual response times','Map legal requirements to included/excluded activities','Section and paragraph','TSAcyber scope question'),
('5CFR1320.8','Office of Management and Budget','https://www.ecfr.gov/current/title-5/chapter-III/subchapter-B/part-1320/section-1320.8','Agency collection responsibilities','Objectively supported burden estimate;consultation','12–15','As amended','none','none','Federal','Compliance floor not an accuracy guarantee','Evidence supporting burden','Section and paragraph','All'),
('JOLTS','Bureau of Labor Statistics','https://www.bls.gov/jlt/jltfaq.htm','FAQ questions7,8,14','Monthly separation flows;reference periods;occupation limitation','12,15','Monthly and annual revisions','No occupation breakdown','Industry','National;state/region withlimits','Employment flows are not unique annual probability;industry proxy may differ from role','Preserve monthly period;sum monthly event counts foryear with correct denominator','BLS,JOLTS release/series/period/vintage','202606-1652-001'),
('OEWS','Bureau of Labor Statistics','https://www.bls.gov/oes/2023/May/naics3_482000.htm','May2023 RailTransportationNAICS482000','Occupation employment;hourly/annual mean andmedian wages','12','Annual','SOC','NAICS','Nationalindustry','No benefits;missing/suppressed estimates;industry occupation proxy','Select role and wage statistic;preserve codes;weighted mix separately','Vintage,NAICS,SOC,tableURL','202606-1652-001'),
('ECEC','Bureau of Labor Statistics','https://www.bls.gov/news.release/archives/ecec_09122025.htm','June2025 ECEC Tables1–4','Wages;benefits;totalcompensation;shares','12,14','Quarterly','Broad occupational group','Broadindustry','Selectedgeographicgroups','Benefits ratio depends on sector/group;not overhead;not freely interchangeable withOEWS','Direct compensation or wage*(total/wages);do not doubleload','Referencequarter,publicationdate,table,row','202606-1652-001'),
('OPM GeneralSchedule','Office of Personnel Management','https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/salary-tables/pdf/2025/DCB.pdf','SalaryTable2025-DCB','Annualpay bygrade/step includinglocality','14','Annual','GSgrade/step','Federal','WashingtonDC locality','Base/locality pay excludes benefits andcontractrates','Add sourcedbenefits;declare annualhours divisor','Year,localitytable,grade,step','202606-1652-001'),
('CPS GeographicMobility','U.S.Census Bureau','https://www.census.gov/data/tables/2023/demo/geographic-mobility/cps-2023.html','2023 geographicmobility,Table2','Moves byemployment anddemographiccharacteristics','12,15','Annual','Laborforcestatus','Limited','National/region','Residentialmovement not necessarily businesscontactchange;overlap withturnover','Affected numerator/denominator andperiod;validateproxy','Year,table,rows,population','202606-1652-001'),
('ECI','Bureau of Labor Statistics','https://www.bls.gov/eci/','EmploymentCostIndex','Wage/compensation indexes','12,14,15','Quarterly','Broadgroups','Broadindustry','Selectedregions','Index measures changes,not wagelevel;matchpopulation andindexbase','Updatedwage=basewage*index_new/index_base','SeriesID,quarters,seasonalstatus,vintage','Candidate,notyetobserved'),
('Census CountyBusinessPatterns','U.S.Census Bureau','https://www.census.gov/programs-surveys/cbp.html','CountyBusinessPatterns','Establishments,employment,payroll bysize andindustry','12,15','Annual','None','NAICS','NationaltoZIPselectedtables','Establishmentnotfirm;coverageexclusions andsuppression','Map regulatoryunit tofirm/site;avoidpopulationdoublecount','Year,NAICS,geography,table','Candidate,notyetobserved'),
('BEA GDPpriceindex','Bureau of Economic Analysis','https://www.bea.gov/data/prices-inflation/gdp-price-index','NIPA priceindexes','Broad output pricechange','13,14,15','Quarterly;revisions','None','Broadaggregates','National','Maypoorlyrepresent IT,equipment orwages','Nominalcost adjustment using appropriate indexratio','NIPAtable,line,period,release','Candidate,notyetobserved'),
('PRA burden guidance','Office of Information and Regulatory Affairs','https://digital.gov/guides/pra/estimate-burden','Burden estimation guidance','Loadedwages;burdenactivities;costcategories','12–15','Asupdated','Laborcategories','None','Federal','Guidance requires interpretation withregulations','Distinguish compliancefloor fromenhancement','Sectionheading,URL,retrieveddate','All')]
def fetch(e):
 name,pub,url,*_=e;p=R/'raw/data-sources'/(''.join(c if c.isalnum() else '-' for c in name)+('.pdf' if '.pdf' in url else '.html'));p.parent.mkdir(parents=True,exist_ok=True)
 try:
  b=urllib.request.urlopen(url,timeout=25).read();p.write_bytes(b)
  if b[:4]!=b'%PDF':p.with_suffix('.txt').write_text(clean(b.decode(errors='replace')))
  return {'url':url,'local_path':str(p.relative_to(R)),'sha256':hashlib.sha256(b).hexdigest(),'retrieval_status':'retrieved'}
 except Exception as ex:return {'url':url,'retrieval_status':'failed','retrieval_error':str(ex)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:results=list(ex.map(fetch,entries))
sources=[json.loads(l) for l in (R/'data/sources.jsonl').read_text().splitlines()];byurl={x['url']:x for x in sources};catalog=[]
for e,r in zip(entries,results):
 name,pub,url,dataset,variables,use,freq,occ,industry,geo,lim,transform,citation,examples=e
 if url not in byurl:
  row={'source_id':f'SRC-{len(sources)+1:04d}','authoring_entity':pub,'title':name+' — '+dataset,'year':None,'publication_date':None,'document_type':'Official dataset or guidance','omb_control_number':None,'publisher':pub,'retrieved_date':'2026-09-09','locator':dataset,'notes':'Dates embedded in title/URL indicate dataset vintage where present;publication date not inferred.',**r};sources.append(row);byurl[url]=row
 catalog.append(dict(zip(['source_id','name','publisher','url','dataset','variables','item_use','update_frequency','occupation','industry','geography','limitations','transformation','citation_approach','example_icrs'],[byurl[url]['source_id'],*e])))
(R/'data/sources.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in sources))
with (R/'data/data-sources.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(catalog[0]));w.writeheader();w.writerows(catalog)
print([(x['url'],x['retrieval_status']) for x in results])
