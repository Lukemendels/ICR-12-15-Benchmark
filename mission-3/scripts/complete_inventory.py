import sys,pathlib,json,re,csv,concurrent.futures
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[2]));from retrieve import clean
from inventory import ROOT,get
rows={}
for q in json.load(open(ROOT/'mission-3/search-register.json')):
 s=(ROOT/q['path']).read_text()
 for tr in re.findall(r'<tr\b[^>]*>(.*?)</tr>',s,re.S):
  m=re.search(r'(PRAViewICR|PRAViewRCF)\?ref_nbr=([^\x27\"]+)',tr)
  if not m:continue
  cells=[clean(x).strip(' |\n') for x in re.findall(r'<td\b[^>]*>(.*?)</td>',tr,re.S)]
  if len(cells)!=10:raise ValueError((m.group(2),cells))
  ref=m.group(2)
  if ref not in rows: rows[ref]=dict(zip(['control','agency','title','request_type','received','concluded','conclusion','expiration','ic_count','form_count'],cells),ref=ref,record_kind=m.group(1),search_membership=[])
  rows[ref]['search_membership'].append(q['name'])
for r in rows.values():
 r['scope']='recent' if 'recent' in r['search_membership'] else 'active_supplement' if 'active' in r['search_membership'] else 'pending_supplement'
 r['exclusion']='Common form request under OPM control; not TSA-authored Supporting Statement A' if r['record_kind']=='PRAViewRCF' else None
 r['record_url']='https://www.reginfo.gov/public/do/'+r['record_kind']+'?ref_nbr='+r['ref']
(ROOT/'mission-3/inventory.json').write_text(json.dumps(sorted(rows.values(),key=lambda r:(r['control'],r['ref'])),indent=2)+'\n')
controls=sorted(set(r['control'] for r in rows.values() if not r['exclusion'] and r['control']))
d=ROOT/'mission-3/raw/histories';d.mkdir(parents=True,exist_ok=True)
def hist(c):
 u='https://www.reginfo.gov/public/do/PRAOMBHistory?ombControlNumber='+c;b=get(u);t=clean(b.decode());(d/(c+'.txt')).write_text(t)
 refs=sorted(set(re.findall(r'PRAViewICR\?ref_nbr=(\d{6}-\d{4}-\d{3})',b.decode())))
 return {'control':c,'url':u,'path':'mission-3/raw/histories/'+c+'.txt','refs':refs}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:h=list(ex.map(hist,controls))
(ROOT/'mission-3/control-histories.json').write_text(json.dumps(h,indent=2)+'\n')
print('rows',len(rows),'controls',len(controls),'histories',len(h));print('active not recent',[(r['ref'],r['title']) for r in rows.values() if r['scope']!='recent'])
