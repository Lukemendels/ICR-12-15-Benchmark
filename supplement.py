from pathlib import Path
import re,json,urllib.request,zipfile,io,xml.etree.ElementTree as ET,hashlib
R=Path(__file__).parent
ref='202502-2040-002';d=R/'icrs'/ref/'raw';s=(d/'documents.html').read_text()
for rel,name in re.findall(r'downloadBtnOnClickHandler\("([^\"]+)"\)[^>]*>\s*(.*?)\s*</button>',s,re.S):
 if '.xlsx' not in name:continue
 url='https://www.reginfo.gov'+rel;b=urllib.request.urlopen(url,timeout=30).read();p=d/'burden-calculation-tables.xlsx';p.write_bytes(b)
 z=zipfile.ZipFile(io.BytesIO(b));ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
 strings=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))] if 'xl/sharedStrings.xml' in z.namelist() else []
 records=[]
 for f in z.namelist():
  if re.match(r'xl/worksheets/sheet\d+.xml',f):
   for c in ET.fromstring(z.read(f)).findall('.//s:c',ns):
    v=c.find('s:v',ns);form=c.find('s:f',ns);val=v.text if v is not None else None
    if c.attrib.get('t')=='s' and val is not None:val=strings[int(val)]
    if val is not None or form is not None:records.append({'sheet_part':f,'cell':c.attrib['r'],'value':val,'formula':form.text if form is not None else None})
 (d/'burden-calculation-tables.cells.json').write_text(json.dumps(records,indent=2))
 (d/'burden-calculation-tables.manifest.json').write_text(json.dumps({'title':name.strip(),'url':url,'sha256':hashlib.sha256(b).hexdigest(),'retrieved_date':'2026-09-09','notes':'Read-only XML extraction; values are saved workbook caches, not freshly recalculated.'},indent=2))
 print('cells',len(records))
 for x in records:
  if x['formula'] or x['cell'].startswith(('A','B')):print(x)
