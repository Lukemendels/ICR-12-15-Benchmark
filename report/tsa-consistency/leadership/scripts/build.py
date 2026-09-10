"""Build the decision brief from Markdown, preserving same-page notes and URLs."""
from pathlib import Path
import re, html, csv
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
P=Path(__file__).resolve().parents[1]
for name,f in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Italic','../noto/NotoSans-Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+f))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
navy=colors.HexColor('#17364D');teal=colors.HexColor('#257D82');pale=colors.HexColor('#EDF3F6')
styles={k:ParagraphStyle(k,fontName='Body',fontSize=sz,leading=lead,spaceAfter=after,textColor=navy) for k,sz,lead,after in [('body',10.5,14.5,6),('note',8.5,11.5,6),('cell',9.5,12.5,0),('ref',10,15,20)]}
for st in styles.values():st.allowWidows=0;st.allowOrphans=0;st.splitLongWords=0
styles['title']=ParagraphStyle('title',fontName='Bold',fontSize=23,leading=28,spaceAfter=16,textColor=navy,keepWithNext=True)
styles['sub']=ParagraphStyle('sub',fontName='Bold',fontSize=12,leading=16,spaceBefore=6,spaceAfter=6,textColor=teal,keepWithNext=True)
styles['head']=ParagraphStyle('head',parent=styles['cell'],fontName='Bold',textColor=colors.white)
styles['callout']=ParagraphStyle('callout',parent=styles['body'],fontName='Bold',spaceAfter=0)
def para(t,style='body'):
    t=html.escape(t)
    t=re.sub(r'\[([^\]]+)\]\((https://[^)]+)\)',r'<link href="\2" color="#257D82"><u>\1</u></link>',t)
    t=re.sub(r'\[\^(\d+)\]',r'<super>\1</super>',t)
    t=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'\*(.*?)\*',r'<i>\1</i>',t)
    return Paragraph(t,styles[style])
def footer(c,d):
    c.setStrokeColor(teal);c.line(48,751,564,751)
    c.setFont('Body',8);c.setFillColor(navy)
    c.drawString(48,762,'ECONOMIC ANALYSIS BRANCH  |  LEADERSHIP BRIEF')
    c.drawString(48,30,'TSA ICR Items 12–15  |  September 2026');c.drawRightString(564,30,str(d.page))
parts=(P/'source/brief.md').read_text().split('\n---\n');story=[];tn=0
for pn,part in enumerate(parts):
    if pn:story.append(PageBreak())
    lines=part.strip().splitlines();i=0;notes=[]
    while i<len(lines):
        line=lines[i].strip();i+=1
        if not line:continue
        if line in ['## What I found','## 2. Do the pieces inside a Supporting Statement reconcile with each other?','## 3. Stop maintaining the same number in several independent places','## Future','## What I would want to learn from the pilot']:
            story.append(PageBreak())
        if re.match(r'\[\^\d+\]:',line):
            notes.append(para(re.sub(r'\[\^(\d+)\]:',r'\1.',line),'note'));continue
        if line.startswith('|'):
            rows=[];i-=1
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=[x.strip() for x in lines[i].strip().strip('|').split('|')];i+=1
                if not all(re.fullmatch(r'[:\- ]+',x) for x in row):rows.append(row)
            tn+=1
            with (P/f'tables/table-{tn:02d}.csv').open('w') as f:csv.writer(f,lineterminator='\n').writerows(rows)
            if pn==1:
                story.append(para('What the map captures — why it matters','sub'))
                for row in rows[1:]:
                    q=para(row[0]+': '+row[1],'cell')
                    story.extend([q,Spacer(1,5)])
                story.append(Spacer(1,7));continue
            if pn==4:
                story.append(para('Reconciliation step • Annualized burden hours','cell'))
                t=Table([[para(r[0],'head') for r in rows[1:]],[para(r[1],'callout') for r in rows[1:]]],colWidths=[129]*4,hAlign='LEFT')
                t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('BACKGROUND',(0,1),(-1,1),pale),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
                story.extend([Spacer(1,6),t,Spacer(1,10)]);continue
            widths=[150,366] if pn in [1,2] else [310,206]
            t=Table([[para(x,'head' if j==0 else 'cell') for x in row] for j,row in enumerate(rows)],colWidths=widths,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('ROWBACKGROUNDS',(0,1),(-1,-1),[pale,colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
            story.extend([t,Spacer(1,14)]);continue
        if '→' in line or (i<len(lines) and lines[i].strip()=='↓'):
            if '→' in line:
                labels=[x.strip().strip('*') for x in line.split('→')]
            else:
                labels=[line.strip('*')]
                while i<len(lines) and lines[i].strip()=='↓':
                    i+=1;labels.append(lines[i].strip().strip('*'));i+=1
            flow=[]
            for j,label in enumerate(labels):
                flow.append([para(str(j+1),'head'),para(label,'cell')])
            t=Table(flow,colWidths=[28,488],hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,-1),teal),('BACKGROUND',(1,0),(1,-1),pale),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,-2),2,colors.white)]))
            story.extend([KeepTogether([t]),Spacer(1,14)])
        elif line.startswith('# '):story.append(para(line[2:],'title'))
        elif line.startswith('## '):story.append(para(line[3:],'sub'))
        elif line.startswith('### '):story.append(para(line[4:],'sub'))
        elif line.startswith('> '):
            t=Table([[para(line[2:],'callout')]],colWidths=[516]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),pale),('BOX',(0,0),(-1,-1),.6,teal),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),12)]));story.extend([Spacer(1,6),t,Spacer(1,8)])
        else:
            if line.startswith('- '):line='• '+line[2:]
            if re.match(r'^\d+\. ',line) and i<len(lines) and lines[i].startswith('   '):
                line+=' '+lines[i].strip();i+=1
            story.append(para(line,'ref' if pn==8 else 'note' if line.startswith('**TSA ICR Items') else 'body'))
    if notes:story.extend([Spacer(1,4),KeepTogether(notes)])
pdf=P/'final/TSA-ICR-Consistency-and-Analytical-Controls-EAB-Brief.pdf'
SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=59,bottomMargin=48,title='What the TSA ICR Review Shows — and How We Can Use It',author='',invariant=1).build(story,onFirstPage=footer,onLaterPages=footer)
import pymupdf as fitz
D=fitz.open(pdf);out=Path('/tmp/eab-brief-render');out.mkdir(exist_ok=True)
for i,page in enumerate(D):
    page.get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(out/f'page-{i+1:02d}.png')
print('PAGES',len(D))
for i,page in enumerate(D):print(i+1,len(page.get_text()),len(page.get_links()))
