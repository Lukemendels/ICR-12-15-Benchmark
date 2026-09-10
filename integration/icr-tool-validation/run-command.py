#!/usr/bin/env python3
"""Record a bounded validation command without modifying target source."""
import datetime,json,pathlib,subprocess,sys,time
root=pathlib.Path(__file__).resolve().parent
label,cwd,*command=sys.argv[1:]
t=time.monotonic()
p=subprocess.run(command,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
duration=round(time.monotonic()-t,3)
(root/'logs').mkdir(exist_ok=True)
(root/'logs'/f'{label}.log').write_text(p.stdout)
entry={'label':label,'command':command,'cwd':cwd,'exit_status':p.returncode,'duration_seconds':duration,'at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
with (root/'commands.jsonl').open('a') as f: f.write(json.dumps(entry)+'\n')
print(json.dumps(entry));print(p.stdout[-10000:])
