"""Mission 3 final-analysis helpers. No network or frozen-input mutations."""
import json, pathlib, hashlib
ROOT=pathlib.Path(__file__).resolve().parents[2]
def read(p): return json.loads((ROOT/p).read_text())
def rows(p): return [json.loads(s) for s in (ROOT/p).read_text().splitlines() if s.strip()]
def write(p,data):
    q=ROOT/p;q.parent.mkdir(parents=True,exist_ok=True)
    q.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def jsonl(p,data):
    q=ROOT/p;q.parent.mkdir(parents=True,exist_ok=True)
    q.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data))
def ident(prefix,*parts):return prefix+'-'+hashlib.sha256('|'.join(map(str,parts)).encode()).hexdigest()[:20]
def evidence(ref,lines):
    d=read('mission-3/sources/'+ref+'/source.json')['documents'][0]
    ss=(ROOT/d['path']).read_text().splitlines()
    return [dict(source_id='M3-SRC-'+ref+'-'+d['id'],document_id=d['id'],locator=d['path']+':L'+str(n),original=ss[n-1],extraction_method='Reviewed archived source line in its complete statement',transformation='Verbatim source; analysis separately labeled',status='PUBLISHED') for n in lines]
def checkpoint(label,next_step):
    s=read('mission-3/research-state.json');s['MISSION_STATUS']='COMPARISON_ADJUDICATION_AND_VALIDATION'
    if label not in s['completed']:s['completed'].append(label)
    s['next']=next_step;s['final_analysis_base_commit']='d17ed03d740f7c52abfa00cac53f7b8c4fdbb34c'
    write('mission-3/research-state.json',s)
