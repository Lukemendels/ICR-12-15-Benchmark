from pathlib import Path
import json,re,sys,hashlib,zipfile,io,xml.etree.ElementTree as E
from retrieve import get,extract,clean
R=Path(__file__).parent
ref=sys.argv[1]; terms=sys.argv[2:];d=R/'icrs'/ref/'raw'
registry=[json.loads(x) for x in (R/'data/sources.jsonl').read_text().splitlines()]
byurl={x['url']:x for x in registry}
m=json.loads((d.parent/'retrieval.json').read_text())
for rel,name in re.findall(r'downloadBtnOnClickHandler\("([^\"]+)"\)[^>]*>\s*(.*?)\s*</button>',(d/'documents.html').read_text(),re.S):
 name=clean(name)
 if not any(t.lower() in name.lower() for t in terms):continue
 url='https://www.reginfo.gov'+rel
 if url in byurl:print('cached',name);continue
 b=get(url);ext=Path(name).suffix.lower();p=d/('supplement-'+re.search(r'objectID=(\d+)',url).group(1)+ext);p.write_bytes(b)
 if ext=='.xlsx':
  z=zipfile.ZipFile(io.BytesIO(b));ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'};strings=[''.join(x.itertext()) for x in E.fromstring(z.read('xl/sharedStrings.xml'))] if 'xl/sharedStrings.xml' in z.namelist() else [];cells=[]
  for part in z.namelist():
   if re.fullmatch(r'xl/worksheets/sheet\d+.xml',part):
    for c in E.fromstring(z.read(part)).findall('.//s:c',ns):
     v=c.find('s:v',ns);f=c.find('s:f',ns);value=v.text if v is not None else None
     if c.attrib.get('t')=='s' and value is not None:value=strings[int(value)]
     if value is not None or f is not None:cells.append({'sheet':part,'cell':c.attrib['r'],'value':value,'formula':f.text if f is not None else None})
  p.with_suffix('.cells.json').write_text(json.dumps(cells,indent=2));notes='Read-only cell extraction; observed workbook caches not fresh recalculation.'
 else:p.with_suffix('.txt').write_text(extract(b,p));notes='Original plus text extraction.'
 dm=re.search(re.escape(name)+r'[\s|]*(\d\d/\d\d/\d{4})',(d/'documents.txt').read_text())
 row={'source_id':f'SRC-{len(registry)+1:04d}','authoring_entity':m['agency'],'title':name,'year':int(dm.group(1)[-4:]) if dm else None,'publication_date':dm.group(1) if dm else None,'document_type':'ICR quantitative/methodological supplement','omb_control_number':m['omb_control_number'],'url':url,'publisher':'Reginfo.gov, OMB/GSA','retrieved_date':'2026-09-09','locator':'See local text/cell evidence','local_path':str(p.relative_to(R)),'sha256':hashlib.sha256(b).hexdigest(),'notes':notes};registry.append(row);byurl[url]=row;print(row['source_id'],name)
(R/'data/sources.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in registry))
