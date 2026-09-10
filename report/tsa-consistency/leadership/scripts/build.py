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
styles={k:ParagraphStyle(k,fontName='Body',fontSize=sz,leading=lead,spaceAfter=after,textColor=navy) for k,sz,lead,after in [('body',10.5,15,10),('note',8.3,11.4,6),('cell',9.5,13,0),('ref',10,15,20)]}
styles['title']=ParagraphStyle('title',fontName='Bold',fontSize=25,leading=30,spaceAfter=20,textColor=navy,keepWithNext=True)
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
    c.drawString(48,762,'ECONOMIC ANALYSIS BRANCH  |  LEADERSHIP DECISION BRIEF')
    c.drawString(48,30,'TSA ICR Items 12–15  |  September 10, 2026');c.drawRightString(564,30,str(d.page))
parts=(P/'source/brief.md').read_text().split('\n---\n');story=[];tn=0
for pn,part in enumerate(parts):
    if pn:story.append(PageBreak())
    lines=part.strip().splitlines();i=0;notes=[]
    while i<len(lines):
        line=lines[i].strip();i+=1
        if not line:continue
        if re.match(r'\[\^\d+\]:',line):
            notes.append(para(re.sub(r'\[\^(\d+)\]:',r'\1.',line),'note'));continue
        if line.startswith('|'):
            rows=[];i-=1
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=[x.strip() for x in lines[i].strip().strip('|').split('|')];i+=1
                if not all(re.fullmatch(r'[:\- ]+',x) for x in row):rows.append(row)
            tn+=1
            with (P/f'tables/table-{tn:02d}.csv').open('w') as f:csv.writer(f,lineterminator='\n').writerows(rows)
            widths=[170,346] if len(rows[0])==2 else [220,148,148]
            if pn==4:widths=[340,176]
            t=Table([[para(x,'head' if j==0 else 'cell') for x in row] for j,row in enumerate(rows)],colWidths=widths,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('ROWBACKGROUNDS',(0,1),(-1,-1),[pale,colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
            story.extend([t,Spacer(1,14)]);continue
        if line.startswith('Sources →'):
            labels=['Sources','Reviewed inputs','Explicit assumptions','Calculations','Validation','Tables','Items 12–15 narrative']
            cells=[]
            for j,label in enumerate(labels):
                if j:cells.append(para('→','cell'))
                cells.append(para(label,'cell'))
            t=Table([cells],colWidths=[66 if j%2==0 else 9 for j in range(13)])
            rules=[('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]
            rules += [('BACKGROUND',(j,0),(j,0),pale) for j in range(0,13,2)]
            t.setStyle(TableStyle(rules));story.extend([t,Spacer(1,16)])
            i+=2
        elif line.startswith('# '):story.append(para(line[2:],'title'))
        elif line.startswith('### '):story.append(para(line[4:],'sub'))
        elif line.startswith('> '):
            t=Table([[para(line[2:],'callout')]],colWidths=[516]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),pale),('BOX',(0,0),(-1,-1),.6,teal),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),12)]));story.extend([Spacer(1,6),t,Spacer(1,8)])
        else:
            if line.startswith('- '):line='• '+line[2:]
            story.append(para(line,'ref' if pn==8 else 'note' if line.startswith('TSA ICR Items') else 'body'))
    if notes:story.extend([Spacer(1,16),KeepTogether(notes)])
pdf=P/'final/TSA-ICR-Consistency-and-Analytical-Controls-EAB-Brief.pdf'
SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=59,bottomMargin=48,title='TSA ICR Items 12–15: EAB Decision Brief',author='',invariant=1).build(story,onFirstPage=footer,onLaterPages=footer)
import pymupdf as fitz
D=fitz.open(pdf);out=Path('/tmp/eab-brief-render');out.mkdir(exist_ok=True)
for i,page in enumerate(D):
    page.get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(out/f'page-{i+1:02d}.png')
print('PAGES',len(D))
for i,page in enumerate(D):print(i+1,len(page.get_text()),len(page.get_links()))
