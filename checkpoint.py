"""Refresh derived views and export an incremental GitHub text tree; no network writes."""
from pathlib import Path
import json,csv,statistics,zipfile,xml.etree.ElementTree as E,sys,datetime,hashlib
R=Path(__file__).parent
reviews=[json.loads(p.read_text()) for p in sorted((R/'icrs').glob('*/extraction.json'))]
# Lossless structured cell evidence for every Word table, including supplements.
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
for d in reviews:
 out=[]
 for p in (R/'icrs'/d['icr_id']/'raw').glob('*.docx'):
  with zipfile.ZipFile(p) as z:
   root=E.fromstring(z.read('word/document.xml'))
   for n,t in enumerate(root.findall('.//w:tbl',ns),1):
    rows=[[''.join(c.itertext()) if False else ' '.join(t.text or '' for t in c.findall('.//w:t',ns)) for c in row.findall('w:tc',ns)] for row in t.findall('w:tr',ns)]
    out.append({'file':str(p.relative_to(R)),'table':n,'rows':rows})
 if out:(R/'icrs'/d['icr_id']/'table-evidence.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
rows=[]
for a in sorted(set(d['agency'] for d in reviews)):
 x=[d['total_score'] for d in reviews if d['agency']==a];rows.append({'agency':a,'n':len(x),'mean':round(statistics.mean(x),2),'median':statistics.median(x),'min':min(x),'max':max(x),'population_sd':round(statistics.pstdev(x),2),'inference':'purposive descriptive sample; no agency population rank'})
with (R/'data/agency-summary.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
lines=['# Provisional observed leaders',f'\nReviewed: {len(reviews)}. Scores measure accessible documentation. One-point differences are not evidence of meaningful superiority. Ties are preserved.','\n| Dimension | Score | Observed ICRs |','|---|---:|---|']
for k in ['total_score']+list(reviews[0]['score']):
 val=lambda d:d['total_score'] if k=='total_score' else d['score'][k]
 best=max(map(val,reviews));lines.append(f"| {k} | {best} | {'; '.join(d['icr_id'] for d in reviews if val(d)==best)} |")
lines+=['\nItem12 spans reproducibility, provenance, segmentation and labor; do not call a single column the Item12 winner. SEC ADV-E is concise; BLS SOII has the highest observed overall score. Census AIES supplies direct measurement triangulation. FCC IPCS supplies an exact change bridge.','\nLegitimate Item13 zeros are eligible for full credit. Nonzero purchased-service exemplars include OSHA extinguishers and FCC satellite. EPA monitoring gives explicit capital/O&M separation but incomplete annuity inputs. No fully validated nonzero capital leader is established.','\nAgency means and dispersion are descriptive (data/agency-summary.csv). Highest agency-level quality and most consistent agency are not established from these heterogeneous purposive cases.']
(R/'methodology/leaders.md').write_text('\n'.join(lines)+'\n')
# Keep locally archived text paths valid when original HTML is omitted from remote text tree.
p=R/'data/sources.jsonl';sources=[json.loads(l) for l in p.read_text().splitlines()]
for s in sources:
 lp=s.get('local_path') or ''
 if lp.endswith('.html') and (R/lp).with_suffix('.txt').exists():s['local_path']=str(Path(lp).with_suffix('.txt'));s['archive_format']='Extracted text of official HTML; retrieval manifest retains URL.'
p.write_text(''.join(json.dumps(s,ensure_ascii=False)+'\n' for s in sources))
errors=[]
if len({d['omb_control_number'] for d in reviews})!=len(reviews):errors.append('duplicate control number')
for d in reviews:
 if sum(d['score'].values())!=d['total_score']:errors.append(d['icr_id']+' score sum')
 for c in d.get('checks',[]):
  actual=eval(c['formula'],{'__builtins__':{}},{'sum':sum,'round':round})
  if abs(actual-c['calculated'])>1e-5:errors.append(d['icr_id']+' check calc')
(R/'research/validation-checkpoint.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'review_count':len(reviews),'unique_controls':len({d['omb_control_number'] for d in reviews}),'sources':len(sources),'errors':errors,'scope':'Intermediate structural and arithmetic validation; not final freeze gate.'},indent=2))
old=json.loads(Path('/tmp/icr-committed-text.json').read_text())
new={}
for p in R.rglob('*'):
 if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts and p.suffix in ['.md','.json','.jsonl','.csv','.py','.txt']:
  rel=str(p.relative_to(R));new[rel]={'path':rel,'mode':'100644','type':'blob','content':p.read_text()}
changes=[v for k,v in new.items() if old.get(k)!=v]
prefix=sys.argv[1] if len(sys.argv)>1 else '/tmp/icr-delta'
batch=[];size=0;files=[]
for e in changes:
 n=len(json.dumps(e).encode())
 if batch and size+n>210000:
  f=f'{prefix}-{len(files)}.json';Path(f).write_text(json.dumps(batch));files.append(f);batch=[];size=0
 batch.append(e);size+=n
if batch:
 f=f'{prefix}-{len(files)}.json';Path(f).write_text(json.dumps(batch));files.append(f)
Path('/tmp/icr-next-text.json').write_text(json.dumps(new))
print(json.dumps({'changed':len(changes),'batches':files,'errors':errors}))
