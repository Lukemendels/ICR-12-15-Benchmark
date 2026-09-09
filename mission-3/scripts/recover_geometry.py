"""Preserve OOXML grid spans and merge origins; never guess missing coordinates."""
import json,pathlib,zipfile,hashlib,xml.etree.ElementTree as ET,sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def text(el):return '\n'.join(''.join(t.text or '' for t in p.iter(W+'t')) for p in ([el] if el.tag==W+'p' else el.findall('.//'+W+'p')))
def extract(doc,ref):
 raw=ROOT.parent/'retrieval-cache'/(doc['id']+doc['format']);b=raw.read_bytes();assert hashlib.sha256(b).hexdigest()==doc['sha256_raw']
 body=ET.fromstring(zipfile.ZipFile(raw).read('word/document.xml')).find(W+'body');tables=[];context=[]
 for el in body:
  if el.tag==W+'p':
   s=text(el)
   if s.strip():context.append(s)
  elif el.tag==W+'tbl':
   width=len(el.findall(W+'tblGrid/'+W+'gridCol'));rows=[];active={};issues=[]
   for ri,tr in enumerate(el.findall(W+'tr')):
    before=tr.find(W+'trPr/'+W+'gridBefore');col=int(before.get(W+'val')) if before is not None else 0;cells=[];grid=[None]*width;newactive={}
    for ci,tc in enumerate(tr.findall(W+'tc')):
     sp=tc.find(W+'tcPr/'+W+'gridSpan');span=int(sp.get(W+'val')) if sp is not None else 1
     vm=tc.find(W+'tcPr/'+W+'vMerge');merge=vm.get(W+'val','continue') if vm is not None else None;origin=[ri,ci];s=text(tc)
     if merge=='continue':
      prev=active.get(col)
      if prev is None:issues.append({'row':ri,'col':col,'issue':'orphan_vertical_continuation'})
      else:origin=prev['origin'];s=prev['resolved_text']
     c={'cell':ci,'col':col,'span':span,'vmerge':merge,'text':text(tc),'origin':origin,'resolved_text':s,'footnote_ids':[x.get(W+'id') for x in tc.iter(W+'footnoteReference')]};cells.append(c)
     for k in range(col,col+span):
      if k>=width:issues.append({'row':ri,'col':k,'issue':'outside_grid'});grid.extend([None]*(k-len(grid)+1))
      grid[k]=s
      if merge:newactive[k]=c
     col+=span
    active=newactive;rows.append({'row':ri,'cells':cells,'grid':grid})
   tables.append({'table':len(tables),'context':context[-3:],'grid_columns':width,'rows':rows,'issues':issues})
 return {'ref':ref,'document_id':doc['id'],'source_id':'M3-SRC-'+ref+'-'+doc['id'],'source_url':doc['url'],'sha256_raw':doc['sha256_raw'],'source_text_path':doc['path'],'epistemic_status':'NORMALIZED','transformation':'OOXML gridSpan and vMerge expanded by explicit grid coordinate; continuation references retain original cell origin; no semantic scalar assignment. Zero-based table/row/cell coordinates in word/document.xml.','tables':tables}
if __name__=='__main__':
 coverage=[json.loads(l) for l in (ROOT/'mission-3/extractions/04-credential-portfolio-coverage.jsonl').read_text().splitlines()];register=[]
 for r in coverage:
  m=json.load(open(ROOT/'mission-3/sources'/r['ref']/'source.json'));d=next(d for d in m['documents'] if d['id']==r['document_id']);out=ROOT/'mission-3/geometry'/r['ref']/(d['id']+'.json');out.parent.mkdir(parents=True,exist_ok=True);g=extract(d,r['ref']);out.write_text(json.dumps(g,ensure_ascii=False,separators=(',',':'))+'\n');register.append({'ref':r['ref'],'document_id':d['id'],'path':str(out.relative_to(ROOT)),'tables':len(g['tables']),'rows':sum(len(t['rows']) for t in g['tables']),'issues':[i for t in g['tables'] for i in t['issues']]})
 (ROOT/'mission-3/extractions/06-cohort-geometry-register.json').write_text(json.dumps(register,indent=2)+'\n');print('Documents',len(register),'tables',sum(r['tables'] for r in register),'issues',sum(len(r['issues']) for r in register))
