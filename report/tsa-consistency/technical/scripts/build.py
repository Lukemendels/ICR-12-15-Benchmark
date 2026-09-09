"""Reproducible report build: python report/tsa-consistency/technical/scripts/build.py."""
from pathlib import Path
import sys, subprocess, json, re, html, collections, hashlib
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'report/tsa-consistency/technical'
subprocess.run([sys.executable,str(OUT/'scripts/prepare.py')],check=True)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
D=json.loads((OUT/'source/report-data.json').read_text());T=json.loads((OUT/'source/tables.json').read_text());R=json.loads((OUT/'source/reference-registry.json').read_text())
NAVY='#17364D';TEAL='#257D82';ORANGE='#B06430';GRAY='#64717C';LIGHT='#EDF3F6'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False})
def figsave(fig,name):
 fig.savefig(OUT/f'figures/{name}.png',dpi=180,bbox_inches='tight',facecolor='white');fig.savefig(OUT/f'figures/{name}.pdf',bbox_inches='tight',facecolor='white');plt.close(fig)
fig,ax=plt.subplots(figsize=(7.0,3.2));cats=['CONSISTENT','DIFFERENT_EXPLAINED','UNRESOLVED','NOT_COMPARABLE','POTENTIALLY_INCONSISTENT'];ys=list(range(5));a=[D['comparison_counts'].get(k,0) for k in cats];b=[D['finding_counts'].get(k,0) for k in cats]
ax.barh([y+.18 for y in ys],a,.34,color=TEAL,label='Task/method comparisons (32)');ax.barh([y-.18 for y in ys],b,.34,color=ORANGE,label='Within-ICR findings (8)')
for vals,off in [(a,.18),(b,-.18)]:
 for y,v in zip(ys,vals):ax.text(v+.15,y+off,str(v),va='center',fontsize=9)
ax.set_yticks(ys,[D['labels'][k] for k in cats]);ax.invert_yaxis();ax.set_xlim(0,18);ax.set_xticks([0,5,10,15]);ax.set_xlabel('Adjudicated records (separate denominators)');ax.tick_params(axis='y',length=0);ax.legend(loc='upper center',bbox_to_anchor=(.5,1.20),ncol=1,frameon=False,fontsize=9);figsave(fig,'classification')
B=D['bridge'];fig,ax=plt.subplots(figsize=(7,3.6));labs=['Prior','Enroll /\nrenew','Replace','In-person\npickup','Enroll\nsurvey','Appeal','Issuance\nsurvey','Current'];values=[B['baseline']]+B['component_deltas']+[B['current']];running=B['baseline']
for i,v in enumerate(values):
 if i in (0,7):bottom=0;height=v;color=NAVY;top=v
 else:bottom=min(running,running+v);height=abs(v);top=max(running,running+v);color=TEAL if v>=0 else ORANGE;running+=v
 ax.bar(i,height,bottom=bottom,width=.66,color=color);ax.text(i,top+8500,f'{v:+,}' if i not in (0,7) else f'{v:,}',ha='center',va='bottom',fontsize=8)
ax.set_xticks(range(8),labs,fontsize=8);ax.set_ylim(0,665000);ax.set_ylabel('Annualized hours');ax.set_yticks([0,200000,400000,600000],['0','200,000','400,000','600,000']);ax.grid(axis='y',alpha=.15);ax.set_axisbelow(True);figsave(fig,'twic')
ac=sorted(D['assumption_counts'].items(),key=lambda x:(-x[1],x[0]));fig,ax=plt.subplots(figsize=(7,4.8));ax.barh(range(len(ac)),[v for k,v in ac],color=TEAL);ax.set_yticks(range(len(ac)),[k.replace('_',' ').capitalize() for k,v in ac],fontsize=9);ax.invert_yaxis();ax.set_xlim(0,66);ax.set_xlabel('Reviewed observations (162 total; not independent defaults)');ax.tick_params(axis='y',length=0)
for y,(k,v) in enumerate(ac):ax.text(v+.7,y,str(v),va='center',fontsize=9)
figsave(fig,'assumptions')
fig,ax=plt.subplots(figsize=(7,5.2));ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,10)
stages=[('Sources','Document, locator, original value'),('Structured inputs','Actor, population, unit, period'),('Assumptions','Rationale, applicability, review status'),('Calculations','Formulas and full precision'),('Validation','Rules, tolerances, dispositions'),('Output tables','Approved results and inherited labels'),('Items 12–15 narrative','Bound numbers and reviewed explanation')]
for i,(title,sub) in enumerate(stages):
 y=9-i*1.3;ax.add_patch(FancyBboxPatch((.15,y-.72),6.05,.98,boxstyle='round,pad=.08',facecolor=LIGHT if i!=4 else '#D9ECEB',edgecolor=TEAL if i==4 else '#B7C8D2'))
 ax.text(.4,y-.01,title,fontsize=11,color=NAVY,weight='bold',va='center');ax.text(.4,y-.4,sub,fontsize=9,color=GRAY,va='center')
 if i<6:ax.annotate('',xy=(3.2,y-1.02),xytext=(3.2,y-.79),arrowprops={'arrowstyle':'->','color':NAVY,'lw':1.2})
ax.add_patch(FancyBboxPatch((6.8,2),2.8,6.5,boxstyle='round,pad=.1',facecolor='#F7F1E9',edgecolor=ORANGE));ax.text(8.2,7.8,'Human\nanalytical review',ha='center',va='center',weight='bold',fontsize=11,color=NAVY)
ax.text(8.2,5.3,'Task and proxy fit\n\nScope exceptions\n\nUnresolved evidence\n\nPublication decision',ha='center',va='center',fontsize=10,color=NAVY)
ax.annotate('',xy=(6.24,3.8),xytext=(6.74,3.8),arrowprops={'arrowstyle':'<->','color':ORANGE,'lw':1.2});ax.text(8.2,2.55,'Judgment is retained\nthroughout the chain.',ha='center',fontsize=9,color=GRAY);figsave(fig,'architecture')
FIGNOTES={
 'classification':('Where do the retained concerns occur?','Source: adjudicated registers. Counts describe selected tests, not portfolio rates. The task/method register includes lineage and within-package component comparisons.'),
 'twic':('How do TWIC component changes reach the current total?','Source: annualized TWIC component bridge; all values are hours. Component changes sum to +80,154 with zero residual. No causal driver attribution. [[BASELINE-TWIC-2025]]'),
 'assumptions':('Which assumption families dominate the reviewed evidence?','Source: reviewed assumption register, including 93 formula-header coefficients. Extraction depth and serial versions affect counts. Item 15 is represented separately.'),
 'architecture':('How can the quantitative model remain connected to its outputs?','Source: proposed analytical architecture derived from the documented TSA risks and prior canonical model. This is a recommendation, not a diagram of current TSA procedures. [[CANONICAL]]')}
# ReportLab supports searchable text, repeatable tables and embedded fonts.
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate,PageTemplate,Frame,Paragraph,Spacer,PageBreak,LongTable,TableStyle,Image,KeepTogether,CondPageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
fontroot=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Body','DejaVuSerif.ttf'),('BodyB','DejaVuSerif-Bold.ttf'),('BodyI','DejaVuSerif.ttf'),('UI','DejaVuSans.ttf'),('UIB','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fontroot/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyB',italic='BodyI',boldItalic='BodyB');pdfmetrics.registerFontFamily('UI',normal='UI',bold='UIB',italic='UI',boldItalic='UIB')
W,H=612,792;MARGIN=51;WIDTH=W-2*MARGIN
styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.2,leading=14.8,spaceAfter=8,textColor=colors.HexColor('#243544'),allowWidows=0,allowOrphans=0),
 'h1':ParagraphStyle('h1',fontName='UIB',fontSize=17,leading=22,spaceBefore=3,spaceAfter=14,textColor=colors.HexColor(NAVY),keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='UIB',fontSize=11.7,leading=16,spaceBefore=13,spaceAfter=7,textColor=colors.HexColor(NAVY),keepWithNext=True),
 'caption':ParagraphStyle('caption',fontName='UIB',fontSize=10.1,leading=13.5,spaceBefore=10,spaceAfter=7,textColor=colors.HexColor(NAVY),keepWithNext=True),
 'note':ParagraphStyle('note',fontName='UI',fontSize=8.2,leading=11.4,spaceAfter=12,textColor=colors.HexColor(GRAY)),
 'cell':ParagraphStyle('cell',fontName='UI',fontSize=8.9,leading=12.1,textColor=colors.HexColor('#243544'),spaceAfter=0),
 'headcell':ParagraphStyle('headcell',fontName='UIB',fontSize=8.8,leading=11.8,textColor=colors.white),
 'ref':ParagraphStyle('ref',fontName='Body',fontSize=9.3,leading=13.3,spaceAfter=9,leftIndent=24,firstLineIndent=-24),
 'quote':ParagraphStyle('quote',fontName='UI',fontSize=11,leading=16,backColor=colors.HexColor(LIGHT),borderPadding=12,leftIndent=12,rightIndent=12,spaceBefore=7,spaceAfter=13),
}
# Resolve citation order over the full manuscript including embedded tables and figures.
reforder=[];key_usage=collections.Counter();claimmap=[]
def citations(s,where=''):
 def sub(m):
  keys=[x.strip() for x in m.group(1).split(',')];nums=[]
  for k in keys:
   if k not in R['key_sources']:raise ValueError('Unknown citation '+k)
   key_usage[k]+=1
   for u in R['key_sources'][k]:
    if u not in reforder:reforder.append(u)
    n=reforder.index(u)+1
    if n not in nums:nums.append(n)
  claimmap.append({'location':where,'text':s,'evidence_records':keys,'reference_numbers':nums})
  nums=sorted(nums); groups=[]; start=prev=nums[0]
  for n in nums[1:]+[None]:
   if n is not None and n==prev+1: prev=n;continue
   groups.append(str(start)+'-'+str(prev) if prev-start>=2 else ', '.join(str(x) for x in range(start,prev+1)))
   start=prev=n
  return '['+', '.join(groups)+']'
 return re.sub(r'\[\[([^]]+)\]\]',sub,s)
def clean(s):return str(s).replace('\u2013','-').replace('\u2014','-').replace('\u2011','-').replace('\u00a0',' ')
def inline(s,where=''):
 s=html.escape(clean(citations(s,where)));s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s);s=s.replace('\n','<br/>');return s
story=[];resolved=[];tablecount=figurecount=0;heading_records=[]
def p(s,style='body',where=''):
 v=inline(s,where);story.append(Paragraph(v,styles[style]));resolved.append(citations(s) if '[[' in s else s)
# Cover page without numbering.
story+=[Spacer(1,72),Paragraph('TSA INFORMATION COLLECTIONS',ParagraphStyle('kicker',fontName='UIB',fontSize=10,leading=14,textColor=colors.HexColor(TEAL),spaceAfter=24)),Paragraph('Consistency and Defensibility<br/>of Burden and Cost Estimation<br/>Across TSA Information Collections',ParagraphStyle('title',fontName='UIB',fontSize=26,leading=34,textColor=colors.HexColor(NAVY),spaceAfter=24)),Paragraph('Comprehensive technical analytical report',ParagraphStyle('subtitle',fontName='UI',fontSize=13,leading=19,textColor=colors.HexColor(GRAY))),Spacer(1,34),Paragraph('Public evidence through September 9, 2026',styles['body']),Spacer(1,40),Paragraph('Comparable methods show substantial coherence.<br/>The principal observed control risks concern reconciliation<br/>within individual published Supporting Statements.',ParagraphStyle('coverfinding',fontName='Body',fontSize=12.3,leading=19,textColor=colors.HexColor(NAVY))),Spacer(1,35),Paragraph('An empirical analysis for economic analysts, program and policy partners, Paperwork Reduction Act (PRA) practitioners, and analytical reviewers.',styles['note']),PageBreak()]
# Contents is generated from section headings, not hard-coded page numbers.
story.append(Paragraph('Contents',styles['h1']));toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName='UI',fontSize=10,leading=14.5,spaceBefore=7,leftIndent=0,firstLineIndent=0,textColor=colors.HexColor(NAVY))];story.append(toc);story.append(PageBreak())
def add_table(key):
 global tablecount
 tablecount+=1;t=T[key];p(f"Table {tablecount}. {t['title']}",'caption',key)
 data=[[Paragraph(inline(x,f'table:{key}:header'),styles['headcell']) for x in t['headers']]]
 for i,row in enumerate(t['rows']):data.append([Paragraph(inline(v,f'table:{key}:row:{i}'),styles['cell']) for v in row])
 tbl=LongTable(data,colWidths=[w*WIDTH for w in t['widths']],repeatRows=1,hAlign='LEFT',splitByRow=1)
 tbl.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor(NAVY)),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F2F6F8')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),.7,colors.HexColor(TEAL)),('LINEBELOW',(0,-1),(-1,-1),.5,colors.HexColor('#C7D3DA'))]))
 story.append(tbl);p(t['note'],'note',f'table:{key}:note')
def add_figure(key):
 global figurecount
 figurecount+=1;title,note=FIGNOTES[key];im=Image(str(OUT/f'figures/{key}.png'));h=WIDTH*im.imageHeight/im.imageWidth
 content=[Paragraph(inline(f'Figure {figurecount}. {title}'),styles['caption']),Image(str(OUT/f'figures/{key}.png'),width=WIDTH,height=h),Spacer(1,5),Paragraph(inline(note,f'figure:{key}'),styles['note'])]
 story.append(KeepTogether(content));resolved.append(f'Figure {figurecount}: {title}. '+citations(note))
for filename in ['report.md','appendices.md']:
 entry_start=None
 text=(OUT/f'source/{filename}').read_text();blocks=re.split(r'\n\s*\n',text.strip())
 for i,b in enumerate(blocks):
  b=b.strip();where=f'{filename}:paragraph:{i+1}'
  if b.startswith('# ') or b.startswith('Technical analytical report'):continue
  if b.startswith('## '):
   if entry_start is not None:
    story[entry_start:]=[KeepTogether(story[entry_start:])];entry_start=None
   title=b[3:];story.append(PageBreak() if title.startswith(('1. Purpose','7. Within','14. Conclusion','Appendix ')) else CondPageBreak(135));p(title,'h1',where);continue
  if b.startswith('### '):
   if filename=='appendices.md':
    if entry_start is not None:story[entry_start:]=[KeepTogether(story[entry_start:])]
    entry_start=len(story)
   story.append(CondPageBreak(75));p(b[4:],'h2',where);continue
  if b.startswith('@table '):add_table(b.split()[1]);continue
  if b.startswith('@figure '):add_figure(b.split()[1]);continue
  if b.startswith('> '):p(b[2:],'quote',where);continue
  p(b,'body',where)
 if entry_start is not None:story[entry_start:]=[KeepTogether(story[entry_start:])]
# Source notes and numbered scholarly references.
story.append(PageBreak());p('References','h1')
p('Numbered citations identify the Supporting Statements and prior analytical sources used in the text, tables, and appendices. Package receipt dates identify the administrative version and do not necessarily equal document upload dates. The linked source document and package record provide the public retrieval route; the accompanying citation data retain exact archived locators. No new source search was conducted for this report.','note')
refdata=[]
for i,u in enumerate(reforder,1):
 r=R['references'][u];s=f'[{i}] '+clean(r['text']);v=html.escape(s)
 if r.get('url'):v+=f' <link href="{html.escape(r["url"],quote=True)}" color="{TEAL}">Source document / inventory</link>.'
 if r.get('record_url'):v+=f' <link href="{html.escape(r["record_url"],quote=True)}" color="{TEAL}">Package record</link>.'
 story.append(KeepTogether([Paragraph(v,styles['ref'])]));refdata.append({'number':i,**r});resolved.append(s)
class Doc(BaseDocTemplate):
 def __init__(self,*a,**kw):super().__init__(*a,**kw);self.section='';self.headings=[]
 def beforeDocument(self):self.section='';self.headings=[]
 def afterFlowable(self,flowable):
  if isinstance(flowable,Paragraph) and flowable.style.name=='h1' and flowable.getPlainText()!='Contents':
   txt=flowable.getPlainText();self.section=txt;key='sec'+str(len(self.headings));self.canv.bookmarkPage(key);self.canv.addOutlineEntry(txt,key,level=0,closed=False);self.notify('TOCEntry',(0,txt,self.page-1,key));self.headings.append({'title':txt,'pdf_page':self.page,'printed_page':self.page-1})
def page(canvas,doc):
 if doc.page==1:return
 canvas.saveState();canvas.setStrokeColor(colors.HexColor('#BCD0DA'));canvas.setLineWidth(.5);canvas.line(MARGIN,H-37,W-MARGIN,H-37);canvas.setFont('UI',8);canvas.setFillColor(colors.HexColor(GRAY));canvas.drawString(MARGIN,H-29,'TSA ICR CONSISTENCY AND DEFENSIBILITY');canvas.drawRightString(W-MARGIN,H-29,'Technical report | September 2026');canvas.line(MARGIN,38,W-MARGIN,38);canvas.drawString(MARGIN,25,'Public estimation evidence | Component-specific findings');canvas.drawRightString(W-MARGIN,25,str(doc.page-1));canvas.restoreState()
pdf=OUT/'final/TSA-ICR-Consistency-and-Defensibility-Report.pdf'
doc=Doc(str(pdf),pagesize=(W,H),leftMargin=MARGIN,rightMargin=MARGIN,topMargin=55,bottomMargin=53,title='Consistency and Defensibility of Burden and Cost Estimation Across TSA Information Collections',author='Technical analytical report',pageCompression=1)
doc.addPageTemplates([PageTemplate(id='normal',frames=[Frame(MARGIN,53,WIDTH,H-108,id='main',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page)])
doc.multiBuild(story)
(OUT/'source/report-resolved.txt').write_text('\n\n'.join(resolved)+'\n')
(OUT/'source/references.json').write_text(json.dumps(refdata,indent=2,ensure_ascii=False)+'\n')
(OUT/'source/references.md').write_text('\n\n'.join(f"[{r['number']}] {r['text']}"+(f" [Source]({r['url']})." if r.get('url') else '') for r in refdata)+'\n')
(OUT/'audit/citation-use.json').write_text(json.dumps(claimmap,indent=2,ensure_ascii=False)+'\n')
(OUT/'audit/document-structure.json').write_text(json.dumps(doc.headings,indent=2)+'\n')
(OUT/'audit/build-summary.json').write_text(json.dumps({'pdf':str(pdf.relative_to(ROOT)),'page_count':doc.page,'tables':tablecount,'figures':figurecount,'references':len(refdata),'citation_keys':dict(key_usage),'build_command':'python report/tsa-consistency/technical/scripts/build.py','pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()},indent=2)+'\n')
print('Built',doc.page,'pages;',tablecount,'tables;',figurecount,'figures;',len(refdata),'references.')
