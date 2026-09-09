"""Reproducible public Reginfo portfolio discovery; no prior-session inputs."""
import sys,json,pathlib,urllib.request,urllib.parse,re,datetime,hashlib,concurrent.futures
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[2]))
from retrieve import clean
ROOT=pathlib.Path(__file__).resolve().parents[2]
def get(url):
 with urllib.request.urlopen(url,timeout=45) as r:return r.read()
def search(name,extra):
 params={'operation':'2','page':'-1','requestTypeCategory':'ICR','agencyCode':'1600','subAgencyCode':'1652',**extra}
 url='https://www.reginfo.gov/public/do/PRASearch?'+urllib.parse.urlencode(params)
 b=get(url);p=ROOT/'mission-3/raw/search'/f'{name}.html';p.write_bytes(b)
 txt=clean(b.decode());p.with_suffix('.txt').write_text(txt)
 refs=sorted(set(re.findall(r'PRAViewICR\?ref_nbr=(\d{6}-\d{4}-\d{3})',b.decode())))
 return {'name':name,'url':url,'parameters':params,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(b).hexdigest(),'path':str(p.relative_to(ROOT)),'refs':refs,'count':len(refs)}
if __name__=='__main__':
 qs=[('recent',{'dateType':'RE','startDate':'09/09/2021','endDate':'09/09/2026'}),('active',{'icrStatus':'AC'}),('pending',{'icrStatus':'RE'})]
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(lambda q:search(*q),qs))
 (ROOT/'mission-3/search-register.json').write_text(json.dumps(r,indent=2)+'\n')
 print([(x['name'],x['count']) for x in r])
