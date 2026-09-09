from pathlib import Path
import re,json,html,hashlib
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
for name,file in [('Sans','DejaVuSans.ttf'),('Sans-Bold','DejaVuSans-Bold.ttf'),('Serif','DejaVuSerif.ttf'),('Serif-Bold','DejaVuSerif-Bold.ttf'),('Serif-Italic','DejaVuSerif-Italic.ttf')]:
 import matplotlib
 font_path=Path(matplotlib.get_data_path())/'fonts/ttf'/file
 pdfmetrics.registerFont(TTFont(name,str(font_path)))
pdfmetrics.registerFontFamily('Serif',normal='Serif',bold='Serif-Bold',italic='Serif-Italic',boldItalic='Serif-Bold')
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='Sans-Bold',italic='Sans',boldItalic='Sans-Bold')
INK=colors.HexColor('#173247'); TEAL=colors.HexColor('#147c83'); GRAY=colors.HexColor('#52616c')
styles={
 'body':ParagraphStyle('body',fontName='Serif',fontSize=10.6,leading=15.0,spaceAfter=9,textColor=INK),
 'h1':ParagraphStyle('h1',fontName='Sans-Bold',fontSize=19,leading=23,spaceAfter=17,textColor=INK),
 'h2':ParagraphStyle('h2',fontName='Sans-Bold',fontSize=12.2,leading=16,spaceBefore=5,spaceAfter=10,textColor=TEAL),
 'h3':ParagraphStyle('h3',fontName='Sans-Bold',fontSize=11.4,leading=15,spaceBefore=4,spaceAfter=9,textColor=TEAL),
 'note':ParagraphStyle('note',fontName='Serif',fontSize=8.0,leading=10.6,textColor=GRAY),
 'cell':ParagraphStyle('cell',fontName='Sans',fontSize=9.4,leading=13,textColor=INK),
 'ref':ParagraphStyle('ref',fontName='Serif',fontSize=10,leading=14.5,spaceAfter=17,textColor=INK),
}
refs={x['source_id']:x for x in json.loads((REPO/'report/source/references.json').read_text())}
names={'DHS/TSA':'Transportation Security Administration','DOL/BLS':'Bureau of Labor Statistics','DOL/OSHA':'Occupational Safety and Health Administration','DHS/USCG':'U.S. Coast Guard','DOC/CENSUS':'U.S. Census Bureau'}
refs['TECH']={'authoring_entity':'Federal ICR benchmark study','year':2026,'display_title':'Benchmarking Federal ICR Burden and Cost Analysis: Best Practices for Supporting Statement Items 12-15','short_title':'Federal ICR technical benchmark','url':'','document_type':'Technical report'}
short={'SRC-0060':'Portable Fire Extinguishers','SRC-0174':'Security Plan Requirements','SRC-0099':'AIES Dress Rehearsal Findings'}
registry=[];used=[];note_count=0

def fullref(sid,link=True):
 r=refs[sid]; a=names.get(r['authoring_entity'],r['authoring_entity']); title=r.get('display_title',r['title'] if 'title' in r else '')
 st=('<i>'+html.escape(title)+'</i>. (2026). [Technical report].') if sid=='TECH' else html.escape(a)+'. ('+str(r.get('year') or 'n.d.')+'). <i>'+html.escape(title)+'</i>.'
 if r.get('omb_control_number'): st+=' (OMB Control No. '+r['omb_control_number']+').'
 if r.get('url') and link: st+=' <link href="'+html.escape(r['url'],quote=True)+'" color="#147c83">Published source</link>.'
 return st

def inline(s):
 s=html.escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'\*(.+?)\*',r'<i>\1</i>',s)
 return s

def cite_text(s,notes,page):
 global note_count
 def sub(m):
  global note_count
  sid,loc=m.group(1),m.group(2); first=sid not in used
  if first: used.append(sid)
  note_count+=1
  r=refs[sid]
  cit=fullref(sid) if first else ('<i>Federal ICR technical benchmark</i>.' if sid=='TECH' else html.escape(names.get(r['authoring_entity'],r['authoring_entity']))+', <i>'+html.escape(short.get(sid,r.get('short_title',r.get('display_title',''))))+'</i>.')
  notes.append(Paragraph(str(note_count)+'. '+cit+' '+html.escape(loc)+'.',styles['note']))
  registry.append({'footnote':note_count,'page':page,'source_id':sid,'locator':loc,'first_use':first,'url':r.get('url','')})
  return '<super>'+str(note_count)+'</super>'
 return re.sub(r'\[@([^|]+)\|([^\]]+)\]',sub,inline(s))

class Architecture:
 def wrap(self,w,h): return w,160
 def drawOn(self,c,x,y):
  c.saveState(); w=504; mid=x+w/2
  boxes=[('SOURCES + ASSUMPTIONS','Unit, period, population, transformation'),('STRUCTURED QUANTITATIVE MODEL','Activities, labor, purchases, Federal resources, baseline'),('AUTOMATED VALIDATION','Arithmetic, units, pathways, periods, sources'),('GENERATED OUTPUTS','Excel model + Items 12-15 tables, footnotes and narrative'),('HUMAN ANALYTICAL REVIEW','Resolve assumptions and approve the analytical record')]
  for i,(a,b) in enumerate(boxes):
   yy=y+160-(i+1)*30
   c.setFillColor(colors.HexColor('#eaf3f4') if i!=3 else colors.HexColor('#d9eceb'));c.roundRect(x,yy,w,26,4,fill=1,stroke=0)
   c.setFillColor(INK);c.setFont('Sans-Bold',8.5);c.drawCentredString(mid,yy+15,a);c.setFont('Sans',7.8);c.drawCentredString(mid,yy+5,b)
   if i<4:
    c.setStrokeColor(TEAL);c.line(mid,yy,mid,yy-4); c.line(mid,yy-4,mid-2,yy-2); c.line(mid,yy-4,mid+2,yy-2)
  c.restoreState()

def blocks(text,notes,page):
 out=[];ls=text.strip().split('\n');i=0
 while i<len(ls):
  line=ls[i].strip()
  if not line:i+=1;continue
  if line=='[ARCHITECTURE]':out.append(Architecture());i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(ls) and ls[i].startswith('|'):
    vals=ls[i].strip().strip('|').split('|')
    # citation tokens contain |; split only table separators with surrounding spaces
    vals=re.split(r' \| ',ls[i].strip()[2:-2])
    rows.append([Paragraph(cite_text(v,notes,page),styles['cell']) for v in vals]);i+=1
   widths=[92,170,242] if len(rows[0])==3 else [92,412]
   t=Table(rows,colWidths=widths,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e0eeef')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,0),(-1,-1),0.35,colors.HexColor('#c6d4da'))]));out.append(t);continue
  st='body'
  for prefix,key in [('### ','h3'),('## ','h2'),('# ','h1')]:
   if line.startswith(prefix):st=key;line=line[len(prefix):];break
  out.append(Paragraph(cite_text(line,notes,page),styles[st]));i+=1
 return out

OUT=ROOT/'final/Federal-ICR-12-15-Benchmark-Findings-and-Recommendations.pdf'
c=canvas.Canvas(str(OUT),pagesize=(612,792),pageCompression=1)
c.setTitle('Federal ICR Items 12-15 Benchmark: Findings and Recommendations for TSA Economic Analysis')
c.setAuthor('');c.setSubject('Leadership analytical brief: findings, quality controls and recommendations')
metrics=[]
def page_frame(n):
 c.setFillColor(TEAL);c.rect(54,746,34,3,stroke=0,fill=1)
 c.setFont('Sans',8);c.setFillColor(GRAY);c.drawString(98,744,'FEDERAL ICR ITEMS 12-15 BENCHMARK')
 c.setStrokeColor(colors.HexColor('#ccd7dc'));c.line(54,45,558,45)
 c.setFont('Sans',8);c.drawString(54,31,'Findings and Recommendations for TSA Economic Analysis');c.drawRightString(558,31,str(n))
def draw_page(items,notes,n):
 page_frame(n); nh=sum(p.wrap(504,800)[1]+4 for p in notes)
 y=718
 for p in items:
  y-=getattr(p,'spaceBefore',0)
  w,h=p.wrap(504,800);p.drawOn(c,54,y-h);y-=h+getattr(p,'spaceAfter',10)
 bottom=61+nh
 if notes:
  c.setStrokeColor(GRAY);c.line(54,bottom+7,190,bottom+7)
  fy=bottom
  for p in notes:
   w,h=p.wrap(504,800);p.drawOn(c,54,fy-h);fy-=h+4
 gap=y-bottom-14 if notes else y-61
 metrics.append({'page':n,'body_bottom':round(y,1),'footnote_top':round(bottom,1),'gap':round(gap,1),'notes':len(notes)})
 if gap<0: print('OVERFLOW',metrics[-1])
 c.showPage()

pages=(ROOT/'source/brief.md').read_text().split('<!-- PAGE -->')
for n,p in enumerate(pages,1):
 notes=[]; items=blocks(p,notes,n);draw_page(items,notes,n)
# references, full citations only for actually cited sources; natural page breaks
items=[Paragraph('References',styles['h1'])];height=40;n=len(pages)+1
for sid in sorted(used,key=lambda sid:(names.get(refs[sid]['authoring_entity'],refs[sid]['authoring_entity']),refs[sid].get('display_title',''))):
 p=Paragraph(fullref(sid),styles['ref']);h=p.wrap(504,800)[1]+17
 if height+h>620:
  draw_page(items,[],n);n+=1;items=[Paragraph('References',styles['h1'])];height=40
 items.append(p);height+=h
if len(items)>1:draw_page(items,[],n)
c.save()
(ROOT/'source/citation-registry.json').write_text(json.dumps(registry,indent=2))
(ROOT/'source/references.json').write_text(json.dumps([refs[x] for x in used],indent=2))
(ROOT/'source/references.md').write_text('# References\n\n'+'\n\n'.join(re.sub('<[^>]*>','',fullref(x))+' '+refs[x].get('url','') for x in used))
(ROOT/'audit/layout-metrics.json').write_text(json.dumps(metrics,indent=2))
print(json.dumps(metrics)); print('PDF',OUT)
