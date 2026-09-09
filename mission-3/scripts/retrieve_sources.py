"""Download public package/documents afresh; preserve text, identities and byte hashes."""
import sys,pathlib,json,re,hashlib,datetime,concurrent.futures
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[2]));from retrieve import clean,extract
from inventory import get,ROOT
CACHE=ROOT.parent/'retrieval-cache';CACHE.mkdir(exist_ok=True)
def fetch(ref):
 d=ROOT/'mission-3/sources'/ref;d.mkdir(parents=True,exist_ok=True)
 if (d/'source.json').exists():return json.load(open(d/'source.json'))
 m={'ref':ref,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'documents':[]}
 try:
  for kind,route in [('record','PRAViewICR'),('documents','PRAViewDocument')]:
   url='https://www.reginfo.gov/public/do/'+route+'?ref_nbr='+ref;b=get(url);(CACHE/(ref+'-'+kind+'.html')).write_bytes(b);txt=clean(b.decode());p=d/(kind+'.txt');p.write_text(txt)
   m[kind]={'url':url,'path':str(p.relative_to(ROOT)),'sha256_raw':hashlib.sha256(b).hexdigest(),'sha256_text':hashlib.sha256(p.read_bytes()).hexdigest()}
   if kind=='record':
    prev=re.search(r'Previous ICR Reference No:\s*(\d{6}-\d{4}-\d{3})',txt);m['previous_ref']=prev.group(1) if prev else None
    status=re.search(r'Status:\s*([^|\n]+)',txt);m['status']=status.group(1).strip() if status else None
   else:html=b.decode()
  start=html.find('Supporting Statement A');end=html.find('Supporting Statement B',start);sec=html[start:end if end>0 else None]
  docs=re.findall(r'downloadBtnOnClickHandler\("([^\"]+)"\)[^>]*>\s*(.*?)\s*</button>',sec,re.S)
  seen=set()
  for rel,title in docs:
   if rel in seen:continue
   seen.add(rel);url='https://www.reginfo.gov'+rel;b=get(url);docid=re.search(r'(?:documentID|documentId)=(\d+)',rel);docid=docid.group(1) if docid else hashlib.sha256(rel.encode()).hexdigest()[:16]
   ext='.docx' if b[:2]==b'PK' else '.pdf' if b[:4]==b'%PDF' else '.bin';p=CACHE/(docid+ext);p.write_bytes(b);t=extract(b,p);out=d/(docid+'.txt');out.write_text(t)
   m['documents'].append({'id':docid,'title':clean(title),'url':url,'path':str(out.relative_to(ROOT)),'sha256_raw':hashlib.sha256(b).hexdigest(),'sha256_text':hashlib.sha256(out.read_bytes()).hexdigest(),'format':ext,'chars':len(t),'extraction':'M1 retrieve.extract: OOXML paragraphs/tables/footnotes or pdftotext -layout','review_status':'NOT_YET_REVIEWED'})
  (d/'source.json').write_text(json.dumps(m,indent=2)+'\n')
 except Exception as e:
  m['error']=str(e);(d/'error.json').write_text(json.dumps(m,indent=2)+'\n')
 return m
if __name__=='__main__':
 if len(sys.argv)>1:refs=sys.argv[1:]
 else:refs=[r['ref'] for r in json.load(open(ROOT/'mission-3/inventory.json')) if not r['exclusion']]
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  for m in ex.map(fetch,refs):print(m['ref'],m.get('status'),len(m['documents']),m.get('error',''),flush=True)
