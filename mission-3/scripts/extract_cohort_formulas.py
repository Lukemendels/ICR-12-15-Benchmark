"""Normalize explicit formula-header coefficients without interpreting ambiguous operands."""
import json,re,hashlib
from recover_geometry import ROOT
rows=[];partitions=[]
for p in sorted((ROOT/'mission-3/geometry').glob('*/*.json')):
 g=json.load(open(p))
 for t in g['tables']:
  for r in t['rows']:
   for c in r['cells']:
    s=c['text']
    if '=' not in s:continue
    for match in re.finditer(r'(?<![\w.])((?:\d+(?:\.\d+)?|\.\d+))\s*(%|hours?\b)',s,re.I):
     value=float(match[1]);unit=match[2].lower();family='pathway_share' if unit=='%' else 'task_duration';loc=str(p.relative_to(ROOT))+f'#/tables/{t["table"]}/rows/{r["row"]}/cells/{c["cell"]}'
     headers=[]
     for prior in t['rows'][:r['row']]:
      val=prior['grid'][c['col']]
      if val and val not in headers:headers.append(val)
     rows.append({'id':'COEF-'+hashlib.sha256((loc+'|'+str(match.start())).encode()).hexdigest()[:18],'ref':g['ref'],'family':family,'original_value':match[1],'original_unit':unit,'value':value/100 if unit=='%' else value*60,'unit':'fraction' if unit=='%' else 'minutes','period':None,'scope':headers,'formula':s,'vintage':None,'measurement_basis':'Published formula-header coefficient; may use rounded time','epistemic_status':'NORMALIZED','confidence':'high_transcription_scope_requires_review','provenance':{'source_id':g['source_id'],'document_id':g['document_id'],'locator':loc,'original':s,'extraction_method':'Explicit OOXML formula cell','transformation':'Percent /100 or hours ×60; scope inherited from same grid column headers','status':'NORMALIZED'}})
 (ROOT/'mission-3/extractions/07-cohort-formula-assumptions.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
print('Explicit coefficients',len(rows),'documents',len(set(r['ref'] for r in rows)))
