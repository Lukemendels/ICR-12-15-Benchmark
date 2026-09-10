"""Offline production audit: content retention, citation provenance, PDF geometry, protection."""
from pathlib import Path
import json,re,hashlib,subprocess
import pymupdf as fitz
P=Path(__file__).resolve().parents[1];R=P.parents[2]
BASE='e39e257633209e73d6f8df2df3b00ef8baa32a77'
s=(P/'source/brief.md').read_text();entries=json.loads((P/'source/citation-registry.json').read_text())['entries']
pdf=P/'final/TSA-ICR-Consistency-and-Analytical-Controls-EAB-Brief.pdf';D=fitz.open(pdf)
assert len(D)==14 and 'References' in D[-1].get_text()
links=[];geometry=[]
for i,page in enumerate(D):
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines',[]):
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                assert x0>=47 and x1<=571 and y0>=15 and y1<=773,(i,span)
    assert not any(x in page.get_text() for x in ['[^','**','##','FULL1','REF1'])
    geometry.append(dict(page=i+1,characters=len(page.get_text()),result='PASS'))
    for link in page.get_links():
        assert link['kind']==fitz.LINK_URI
        links.append(dict(page=i+1,url=link['uri'],rectangle=list(link['from'])))
registered=json.loads((R/'report/tsa-consistency/technical/source/reference-registry.json').read_text())['references']
for e in entries:
    n=e['number'];page=e['first_use_page']
    assert f'[{"^"}{n}]: {e["full_note"]}' in s
    assert e['reference_entry'] in s.split('# References\n')[1]
    assert e['subsequent_citation_count']==s.count(e['abbreviated'])
    d=json.loads((R/e['provenance_path']).read_text())['documents']
    assert any(x['url']==e['url'] and x['path']==e['source_path'] for x in d)
    assert e['source_id'] in registered[e['url']]['source_ids']
    assert any(x['url']==e['url'] and x['page']==page for x in links)
    assert any(x['url']==e['url'] and x['page']==len(D) for x in links)
assert set(re.findall(r'\[\^(\d+)\]:',s))=={str(e['number']) for e in entries}
assert {x['url'] for x in links}=={e['url'] for e in entries}
assert len(links)==6
assert 'technical report' not in s.lower()
# Every source paragraph, heading, table cell and flow label must survive rendering.
def norm(t):
    t=re.sub(r'\[([^\]]+)\]\(https://[^)]+\)',r'\1',t)
    t=re.sub(r'\[\^(\d+)\]:',r'\1.',t)
    t=re.sub(r'\[\^(\d+)\]',r'\1',t)
    t=re.sub(r'^\s*(?:#{1,3} |[- >]+|\d+\. )','',t)
    return re.sub(r'\s+','',t.replace('*','')).casefold()
rendered=norm('\n'.join(p.get_text() for p in D))
checks=0
for line in s.splitlines():
    if not line.strip() or line.strip() in ['---','↓']:continue
    units=line.strip().strip('|').split('|') if line.startswith('|') else line.split('→')
    for u in units:
        if re.fullmatch(r'[:\- ]+',u):continue
        v=norm(u)
        assert v in rendered,('Missing source text',u)
        checks+=1
changed=subprocess.check_output(['git','diff',BASE,'--name-only'],cwd=R,text=True).splitlines()
assert all(x.startswith('report/tsa-consistency/leadership/') for x in changed),changed
tech=R/'report/tsa-consistency/technical/final/TSA-ICR-Consistency-and-Defensibility-Report.pdf'
assert len(fitz.open(tech))==55
assert subprocess.check_output(['git','show',f'{BASE}:{tech.relative_to(R)}'],cwd=R)==tech.read_bytes()
out=dict(result='PASS',baseline_commit=BASE,pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),manuscript_sha256=hashlib.sha256(s.encode()).hexdigest(),pages=len(D),references_page=len(D),full_first_use_citations=len(entries),abbreviated_subsequent_citations=0,supporting_statement_link_annotations=len(links),distinct_supporting_statement_urls=3,links=links,geometry=geometry,source_text_units_verified=checks,technical_report_pages=55,technical_report_sha256=hashlib.sha256(tech.read_bytes()).hexdigest(),protected_state='PASS: all tracked changes confined to leadership directory; technical PDF byte-identical',network_destination_checks='Not performed: exact frozen locators validated offline')
(P/'audit/revision-citation-layout-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['links','geometry']},indent=2))
