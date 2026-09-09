from pathlib import Path
import json,re,hashlib,datetime
R=Path(__file__).parent
f=R/'data/sources.jsonl';old=[json.loads(l) for l in f.read_text().splitlines() if l];byurl={x['url']:x for x in old}
def add(url,**kw):
 if url in byurl:return byurl[url]['source_id']
 row={'source_id':f'SRC-{len(old)+1:04d}','url':url,'authoring_entity':None,'title':None,'year':None,'publication_date':None,'document_type':None,'omb_control_number':None,'publisher':None,'retrieved_date':'2026-09-09','locator':None,'notes':None,**kw};old.append(row);byurl[url]=row;return row['source_id']
add('https://pra.digital.gov/uploads/supporting-statement-a-instructions.pdf',authoring_entity='Office of Information and Regulatory Affairs',title='Creating a Supporting Statement Part A',document_type='Instructions',publisher='General Services Administration, PRA guide',locator='Items 12–15, pages 2–3',local_path='raw/guidance/supporting-statement-a-instructions.pdf',notes='Undated document; available through current official PRA guide. Item 12 outside-party routing text conflicts with Item 13; do not silently correct source.')
add('https://www.rocis.gov/rocis/downloadResourceDocument.do?uuid=632c6a25-57d2-45f3-84d7-701437f7c73a',authoring_entity='Regulatory Information Service Center',title='ROCIS PRA Module User Guide',year=2026,publication_date='2026-06',document_type='System user guide',publisher='RISC/OIRA',locator='Pages 49–51; Appendix supporting-statement instructions pp. 120–121',local_path='raw/guidance/rocis-pra-guide.pdf',notes='Version 9.0. Appendix numbering shifts after Item 14; use question meaning, not number alone.')
for p in sorted((R/'icrs').glob('*/retrieval.json')):
 m=json.loads(p.read_text());ref=m['icr_ref'];s=(p.parent/'raw/record.txt').read_text();
 def field(a,b):
  x=re.search(re.escape(a)+r'\s*(.*?)'+re.escape(b),s,re.S);return x.group(1).strip(' |\n') if x else None
 agency=field('Agency/Subagency:','Agency Tracking No:');title=field('Title:','Type of Information Collection:');control=field('OMB Control No:','ICR Reference No:')
 sub=re.search(r'Date (?:Received in OIRA|Submitted to OIRA):\s*(\d\d/\d\d/\d{4})',s)
 recordid=add(m['record_url'],authoring_entity=agency,title=title,document_type='ICR package record',omb_control_number=control,publisher='Reginfo.gov, OMB/GSA',publication_date=sub.group(1) if sub else None,locator='ICR summary of burden and status',local_path=str((p.parent/'raw/record.html').relative_to(R)))
 ids=[]
 for d in m['documents']:
  ds=(p.parent/'raw/documents.txt').read_text();match=re.search(re.escape(d['title'])+r'\s*\|?\s*(\d\d/\d\d/\d{4})',ds)
  sid=add(d['url'],authoring_entity=agency,title=d['title'],document_type='Supporting Statement A',omb_control_number=control,publisher='Reginfo.gov, OMB/GSA',publication_date=match.group(1) if match else None,locator='Items 12–15 and footnotes',local_path=d['path'],sha256=d['sha256'],notes='Publication date records document upload, where available; ICR submission date is separate.');ids.append(sid)
 m.update({'agency':agency,'title':title,'omb_control_number':control,'submission_date':sub.group(1) if sub else None,'record_source_id':recordid,'supporting_statement_source_ids':ids});p.write_text(json.dumps(m,indent=2))
f.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in old))
print([(p.parent.name,json.loads(p.read_text()).get('supporting_statement_source_ids')) for p in (R/'icrs').glob('*/retrieval.json')])
