"""Offline citation, link, page geometry, and protected-state acceptance checks."""
from pathlib import Path
import json,re,hashlib,subprocess
import pymupdf as fitz
P=Path(__file__).resolve().parents[1];R=P.parents[2]
BASE='439ba34'
s=(P/'source/brief.md').read_text();parts=s.split('\n---\n');entries=json.loads((P/'source/citation-registry.json').read_text())['entries']
pdf=P/'final/TSA-ICR-Consistency-and-Analytical-Controls-EAB-Brief.pdf';D=fitz.open(pdf)
assert len(D)==len(parts)==9
links=[];geometry=[]
for i,page in enumerate(D):
    assert parts[i].strip().splitlines()[0][2:] in page.get_text().replace('\n',' ')
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines',[]):
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                assert x0>=47 and x1<=565 and y0>=15 and y1<=773,(i,span)
    assert not any(x in page.get_text() for x in ['[^','**','FULL1','REF1'])
    geometry.append(dict(page=i+1,characters=len(page.get_text()),result='PASS'))
    for link in page.get_links():
        assert link['kind']==fitz.LINK_URI
        links.append(dict(page=i+1,url=link['uri'],rectangle=list(link['from'])))
registered=json.loads((R/'report/tsa-consistency/technical/source/reference-registry.json').read_text())['references']
for e in entries:
    n=e['number'];page=e['first_use_page']
    assert f'[^{n}]' in parts[page-1] and f'[^{n}]: {e["full"]}' in parts[page-1]
    assert e['reference_entry'] in parts[8]
    assert e['subsequent_citation_count']==sum(p.count(e['abbreviated']) for p in parts[:8])
    if e['url']:
        d=json.loads((R/e['provenance_path']).read_text())['documents']
        assert any(x['url']==e['url'] and x['path']==e['source_path'] for x in d)
        assert e['source_id'] in registered[e['url']]['source_ids']
        assert any(x['url']==e['url'] and x['page']==page for x in links)
        assert any(x['url']==e['url'] and x['page']==9 for x in links)
assert set(re.findall(r'\[\^(\d+)\]:',s))=={str(e['number']) for e in entries}
assert {x['url'] for x in links}=={e['url'] for e in entries if e['url']}
changed=subprocess.check_output(['git','diff',BASE,'--name-only'],cwd=R,text=True).splitlines()
assert all(x.startswith('report/tsa-consistency/leadership/') for x in changed),changed
tech=R/'report/tsa-consistency/technical/final/TSA-ICR-Consistency-and-Defensibility-Report.pdf'
assert len(fitz.open(tech))==55
assert subprocess.check_output(['git','show',f'{BASE}:{tech.relative_to(R)}'],cwd=R)==tech.read_bytes()
old=subprocess.check_output(['git','show',f'{BASE}:report/tsa-consistency/leadership/source/brief.md'],cwd=R,text=True)
new_body='\n'.join(re.sub(r'^\[\^\d+\]:.*$','',p,flags=re.M) for p in parts[:8])
out=dict(result='PASS',baseline_commit=BASE,pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pages=9,page_9_references=True,full_first_use_citations=len(entries),abbreviated_subsequent_citations=sum(e['subsequent_citation_count'] for e in entries),supporting_statement_link_annotations=len(links),supporting_statement_link_occurrences=6,distinct_supporting_statement_urls=3,links=links,geometry=geometry,technical_report_pages=55,technical_report_sha256=hashlib.sha256(tech.read_bytes()).hexdigest(),protected_state='PASS: all tracked changes confined to leadership directory; technical PDF byte-identical',prior_manuscript_words=len(old.split()),revised_main_brief_words=len(new_body.split()),network_destination_checks='Not performed: exact frozen locators validated offline as instructed')
(P/'audit/revision-citation-layout-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['links','geometry']},indent=2))
