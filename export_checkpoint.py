"""Export exact current text files for GitHub API; no evidence mutations."""
from pathlib import Path
import json,sys
R=Path(__file__).parent
old=json.loads(Path('/tmp/icr-committed-text.json').read_text());new={}
for p in R.rglob('*'):
 if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts and p.suffix in ['.md','.json','.jsonl','.csv','.py','.txt']:
  rel=str(p.relative_to(R));new[rel]={'path':rel,'mode':'100644','type':'blob','content':p.read_text()}
changes=[v for k,v in new.items() if old.get(k)!=v]
prefix=sys.argv[1];batch=[];size=0;files=[]
for e in changes:
 n=len(json.dumps(e).encode())
 if batch and size+n>210000:
  f=f'{prefix}-{len(files)}.json';Path(f).write_text(json.dumps(batch));files.append(f);batch=[];size=0
 batch.append(e);size+=n
if batch:
 f=f'{prefix}-{len(files)}.json';Path(f).write_text(json.dumps(batch));files.append(f)
Path('/tmp/icr-next-text.json').write_text(json.dumps(new));print(json.dumps({'changed':len(changes),'files':[(p,len(Path(p).read_text())) for p in files]}))
