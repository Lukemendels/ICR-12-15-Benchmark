import urllib.request, pathlib, re, json, hashlib, datetime, concurrent.futures, subprocess, zipfile, io, xml.etree.ElementTree as ET
from html import unescape
ROOT=pathlib.Path(__file__).parent

def get(url):
 with urllib.request.urlopen(url,timeout=45) as r: return r.read()
def clean(s):
 s=re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',s,flags=re.S|re.I)
 s=re.sub(r'</(?:tr|p|div|h[1-6])>|<br\s*/?>','\n',s,flags=re.I)
 s=re.sub(r'</(?:td|th)>',' | ',s,flags=re.I)
 return '\n'.join(' '.join(unescape(re.sub('<[^>]+>',' ',l)).split()) for l in s.splitlines() if re.sub('<[^>]+>',' ',l).strip())
def extract(b,p):
 if b[:2]==b'PK':
  z=zipfile.ZipFile(io.BytesIO(b)); ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'};lines=[]
  for part in ['word/document.xml','word/footnotes.xml','word/endnotes.xml']:
   if part not in z.namelist():continue
   lines.append('PART '+part)
   x=ET.fromstring(z.read(part))
   for node in x.iter():
    if node.tag.endswith('}tr'):
     lines.append(' | '.join(' '.join(t.text or '' for t in c.findall('.//w:t',ns)) for c in node.findall('./w:tc',ns)))
    elif node.tag.endswith('}p') and not any(node in list(tr.iter()) for tr in x.findall('.//w:tr',ns)):
     lines.append(''.join(t.text or '' for t in node.findall('.//w:t',ns)))
  return '\n'.join(lines)
 if b[:4]==b'%PDF':
  subprocess.run(['pdftotext','-layout',str(p),str(p)+'.layout.txt'],check=True)
  return pathlib.Path(str(p)+'.layout.txt').read_text()
 return clean(b.decode(errors='replace')) if b'<html' in b[:500].lower() else '[UNEXTRACTED BINARY]'
def fetch(ref):
 d=ROOT/'icrs'/ref/'raw';d.mkdir(parents=True,exist_ok=True)
 if (d.parent/'retrieval.json').exists():return ref,'cached'
 meta={'icr_ref':ref,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'documents':[]}
 try:
  for kind,route in [('record','PRAViewICR'),('documents','PRAViewDocument')]:
   u=f'https://www.reginfo.gov/public/do/{route}?ref_nbr={ref}'; b=get(u);(d/(kind+'.html')).write_bytes(b);(d/(kind+'.txt')).write_text(clean(b.decode()))
   meta[kind+'_url']=u
  s=(d/'documents.html').read_text();start=s.find('Supporting Statement A');end=s.find('Supporting Statement B',start); sec=s[start:end if end>0 else None]
  docs=re.findall(r'downloadBtnOnClickHandler\("([^\"]+)"\)[^>]*>\s*(.*?)\s*</button>',sec,re.S)
  for i,(rel,name) in enumerate(docs):
   name=clean(name);u='https://www.reginfo.gov'+rel;b=get(u); ext='.docx' if b[:2]==b'PK' else '.pdf' if b[:4]==b'%PDF' else '.bin';p=d/f'supporting-statement-a-{i+1}{ext}';p.write_bytes(b)
   txt=extract(b,p);(d/f'supporting-statement-a-{i+1}.txt').write_text(txt)
   meta['documents'].append({'title':name,'url':u,'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(b).hexdigest(),'text_chars':len(txt)})
  (d.parent/'retrieval.json').write_text(json.dumps(meta,indent=2));return ref,[(x['title'],x['text_chars']) for x in meta['documents']]
 except Exception as e:
  meta['error']=str(e);(d.parent/'retrieval-error.json').write_text(json.dumps(meta,indent=2));return ref,str(e)
if __name__=='__main__':
 import sys
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
  for r in ex.map(fetch,sys.argv[1:]): print(r,flush=True)
