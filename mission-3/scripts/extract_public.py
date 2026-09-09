"""Lossless Item12–15 evidence indexing plus conservative table/activity normalization.
Candidate tags are discovery aids only; comparisons require explicit adjudication.
"""
import pathlib,json,re,hashlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
def ident(*parts):return hashlib.sha256('|'.join(map(str,parts)).encode()).hexdigest()[:18]
def heading(s):
 x=s.lower().strip();x=re.sub(r'^\d+[.\s)]+','',x)
 if len(x)>1100:return None
 if x.startswith('provide') and ('annual cost burden to' in x or 'capital' in x):return 13
 if re.match(r'(?:provide|12[.\s])',x) and ('hour' in x) and ('burden' in x) and 'federal government' not in x and ('estimat' in x):return 12
 if x.startswith('provide') and ('capital' in x or 'annual cost burden to respondents' in x or 'annual cost burden to respondent' in x):return 13
 if x.startswith('provide') and ('federal government' in x) and ('cost' in x):return 14
 if x.startswith('explain') and ('program changes' in x or 'program change' in x):return 15
 if x.startswith('for collection') and ('published' in x):return 16
 return None
def sections(lines):
 marks=[];last=0
 for i,s in enumerate(lines):
  h=heading(s)
  if h and h>=last:marks.append((i,h));last=h
 # Numbered Word heading may be split; explicit scope remains inspectable.
 out={};current=None
 for i,s in enumerate(lines):
  h=next((h for j,h in marks if j==i),None)
  if h:current=h
  if s.startswith('PART word/footnotes') or s.startswith('PART word/endnotes'):current='footnotes'
  if current in [12,13,14,15,'footnotes'] and s.strip():out[i+1]=current
 return out,marks
def num(x):
 x=x.strip().replace(',','').replace('$','').replace('\u00a0','')
 return float(x) if re.fullmatch(r'-?\d+(?:\.\d+)?',x) else None
def tag(t):
 t=t.lower()
 for name,pat in [('amendment',r'amend|modif'),('renewal',r'renew|recert'),('recordkeeping',r'record|retention'),('enrollment',r'enroll|fingerprint'),('assessment',r'assess|vett|\bsta\b|\bchrc\b'),('reporting',r'report|incident'),('training',r'train'),('survey',r'survey|satisfaction|feedback|evaluation'),('application',r'appli|request|registration'),('coordinator_update',r'coordinator|contact'),('review',r'review|inspect')]:
  if re.search(pat,t):return name
 return 'other_observed_task'
def run(batch,refs):
 obs=[];acts=[];pars=[];coverage=[]
 inv={r['ref']:r for r in json.load(open(ROOT/'mission-3/inventory.json'))}
 for ref in refs:
  f=ROOT/'mission-3/sources'/ref/'source.json'
  if not f.exists():raise RuntimeError('Source unavailable '+ref)
  meta=json.load(open(f))
  for doc in meta['documents']:
   lines=(ROOT/doc['path']).read_text().splitlines();sec,marks=sections(lines)
   coverage.append({'ref':ref,'document_id':doc['id'],'batch':batch,'path':doc['path'],'section_markers':marks,'indexed_nonempty_lines':len(sec),'missing_items':[k for k in [12,13,14,15] if k not in sec.values()],'status':'MACHINE_INDEXED_PENDING_REVIEW','limitations':'Table normalization retains visible cells; no unsupported numeric column interpretation. Narrative durations retain task paragraph; active/elapsed time and scope require source review.'})
   header=[]
   for ln,item in sec.items():
    s=lines[ln-1];pr={'source_id':'M3-SRC-'+ref+'-'+doc['id'],'document_id':doc['id'],'locator':doc['path']+':L'+str(ln),'original':s,'extraction_method':doc['extraction'],'transformation':'Literal source line retained; tags are search aids','status':'PUBLISHED'}
    o={'id':'OBS-'+ident(ref,doc['id'],ln),'ref':ref,'document_id':doc['id'],'control':inv.get(ref,{}).get('control') or None,'item':item,'batch':batch,'text':s,'epistemic_status':'PUBLISHED','provenance':pr};obs.append(o)
    if item==12 and '|' in s:
     cells=[c.strip() for c in s.split('|')];numeric=[num(c) for c in cells]
     if any(re.search(r'per (?:response|respondent)|hour.*burden|annual.*response',c,re.I) for c in cells):header=cells
     # Source rows with substantive task label; exclude arithmetic totals and year-only cohorts.
     label=cells[0]
     if re.search('[a-zA-Z]',label) and sum(n is not None for n in numeric)>=1 and not re.match(r'^(?:total|average|annualized|year|table|\(?[a-z]\)?\s*=)',label,re.I):
      acts.append({'id':'ACT-'+ident(ref,doc['id'],ln),'ref':ref,'control':o['control'],'batch':batch,'activity':label,'shape_tag':tag(label),'actor':'respondent','item':12,'published_cells':cells,'numeric_cells':numeric,'candidate_header':header if len(header)==len(cells) else None,'annual_responses':None,'hours_per_response':None,'minutes_per_response':None,'reported_annual_hours':None,'period':None,'unit':None,'lifecycle':None,'unknown_reason':'Preserved cell-level evidence; scalar fields not inferred from ambiguous/multirow headers. Use curated row mapping where available.','epistemic_status':'NORMALIZED','provenance':{**pr,'status':'NORMALIZED','transformation':'Row split at source table cell separator; numeric tokens parsed without assigning unstated units or semantics'}})
    if item in [12,13,14,15,'footnotes'] and re.search(r'assum|estimat|compensation|wage|\brate\b|\bpercent|\bratio\b|\bfactor\b|\bfee\b|\bminutes?\b|\bhours?\b|baseline|previous|growth|turnover|separation',s,re.I):
     fam='labor_compensation' if re.search(r'wage|compensation|salary|\bSOC\b|ECEC|OEWS',s,re.I) else 'change_baseline' if item==15 else 'nonlabor_cost' if item==13 else 'federal_cost' if item==14 else 'activity_time' if re.search(r'minute|hour',s,re.I) else 'population_frequency'
     pars.append({'id':'PAR-'+ident(ref,doc['id'],ln),'ref':ref,'control':o['control'],'batch':batch,'family':fam,'name':'source_line_'+str(ln),'value':s,'unit':None,'period':None,'vintage':None,'scope':'Source assertion, potentially several inputs; no inferred scalar value','epistemic_status':'PUBLISHED','provenance':pr})
 out=ROOT/'mission-3/extractions';out.mkdir(exist_ok=True)
 for name,data in [('observations',obs),('source-activities',acts),('source-parameters',pars),('coverage',coverage)]:
  (out/f'{batch}-{name}.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data))
 print(batch,'documents',len(coverage),'observations',len(obs),'activity rows',len(acts),'assertion lines',len(pars),'missing',[(x['ref'],x['missing_items']) for x in coverage if x['missing_items']])
if __name__=='__main__':run(sys.argv[1],sys.argv[2:])
