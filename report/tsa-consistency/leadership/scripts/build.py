from pathlib import Path
import re,html,csv,json
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
P=Path(__file__).resolve().parents[1]
for name,f in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+f))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
navy=colors.HexColor('#17364D');teal=colors.HexColor('#257D82')
styles={
'body':ParagraphStyle('body',fontName='Body',fontSize=10,leading=13.5,spaceAfter=8,textColor=navy),
'h1':ParagraphStyle('h1',fontName='Bold',fontSize=24,leading=29,spaceAfter=10,textColor=navy),
'h2':ParagraphStyle('h2',fontName='Bold',fontSize=17,leading=22,spaceAfter=12,textColor=navy,keepWithNext=True),
'h3':ParagraphStyle('h3',fontName='Bold',fontSize=11.5,leading=16,spaceBefore=7,spaceAfter=7,textColor=teal,keepWithNext=True),
'cell':ParagraphStyle('cell',fontName='Body',fontSize=9,leading=11.8,textColor=navy),
'head':ParagraphStyle('head',fontName='Bold',fontSize=9,leading=11.8,textColor=colors.white),
'note':ParagraphStyle('note',fontName='Body',fontSize=8.2,leading=10,spaceAfter=1,textColor=navy)}
def para(t,style='body'):
 t=html.escape(t.replace('–','-').replace('—','-'))
 t=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',t);t=re.sub(r'\*(.*?)\*',r'<i>\1</i>',t)
 return Paragraph(t,styles[style])
def footer(c,d):
 c.setStrokeColor(teal);c.setLineWidth(1);c.line(48,751,564,751)
 c.setFont('Body',8);c.setFillColor(navy);c.drawString(48,762,'ECONOMIC ANALYSIS BRANCH  |  LEADERSHIP BRIEF')
 c.drawString(48,30,'TSA ICR Items 12-15  |  September 9, 2026');c.drawRightString(564,30,str(d.page))
source=(P/'source/brief.md').read_text();parts=source.split('\n---\n');story=[];tn=0
for pn,part in enumerate(parts):
 if pn:story.append(PageBreak())
 lines=part.strip().splitlines();i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    row=[x.strip() for x in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r'[:\- ]+',x) for x in row):rows.append(row)
    i+=1
   tn+=1
   with (P/f'tables/table-{tn:02d}.csv').open('w') as f:csv.writer(f).writerows(rows)
   n=len(rows[0]); widths=([265,251] if n==2 else [146,62,308])
   if pn==5:widths=[89,230,197]
   if pn==2:widths=[199,317]
   data=[[para(x,'head' if r==0 else 'cell') for x in row] for r,row in enumerate(rows)]
   t=Table(data,colWidths=widths,hAlign='LEFT',repeatRows=1)
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#EDF3F6'),colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,-1),(-1,-1),.5,teal)]))
   if tn==2:
    # Keep both analytical denominators visible in separate compact panels.
    pending_rows=rows
    continue
   if tn==3:
    def panel(rr):
     q=Table([[para(x,'head' if j==0 else 'cell') for x in row] for j,row in enumerate(rr)],colWidths=[202,48])
     q.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#EDF3F6'),colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
     return q
    t=Table([[panel(pending_rows),panel(rows)]],colWidths=[258,258]);t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0)]))
   story.extend([t,Spacer(1,10)]);continue
  if line.startswith('# '):story.append(para(line[2:],'h1'))
  elif line.startswith('## '):story.append(para(line[3:],'h2'))
  elif line.startswith('### '):story.append(para(line[4:],'h3'))
  else:
   if line.startswith('- '):line='• '+line[2:]
   style='note' if re.match(r'^\[\d\]',line) or line.startswith('Economic Analysis Branch leadership') else 'body'
   story.append(para(line,style))
  i+=1
pdf=P/'final/TSA-ICR-Consistency-and-Analytical-Controls-EAB-Brief.pdf'
SimpleDocTemplate(str(pdf),pagesize=(612,792),rightMargin=48,leftMargin=48,topMargin=57,bottomMargin=48,title='TSA ICR Items 12-15: Consistency, Analytical Controls, and Opportunities for Economic Analysis',author='Economic Analysis Branch leadership brief').build(story,onFirstPage=footer,onLaterPages=footer)
import fitz
D=fitz.open(pdf);out=Path('/workspace/scratch/7769d7b6cc95/brief-render');out.mkdir(exist_ok=True)
for i,page in enumerate(D):page.get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(out/f'page-{i+1:02d}.png')
print('PAGES',len(D))
for i,page in enumerate(D):print(i+1,len(page.get_text()),page.get_text().splitlines()[2:4])
# Export the five exact vector exhibits from the reviewed page layout.
for name,pn,rect in [('classification',1,(45,490,565,635)),('pipeline',3,(48,165,570,280)),('twic',4,(48,358,570,495)),('recommendations',5,(48,202,570,475)),('architecture',6,(48,142,570,394))]:
 out=fitz.open();r=fitz.Rect(rect);page=out.new_page(width=r.width,height=r.height);page.show_pdf_page(page.rect,D,pn,clip=r);out.save(P/f'figures/{name}.pdf')
