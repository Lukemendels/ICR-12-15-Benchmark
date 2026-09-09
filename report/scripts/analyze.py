from pathlib import Path
import csv,json,hashlib,statistics,ast,operator,math
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
R=Path(__file__).resolve().parents[2]
def read(name): return pd.read_csv(R/'data'/name)
def out(df,name,folder='tables'):df.to_csv(R/'report'/folder/name,index=False)
I=read('icrs.csv');S=read('scores.csv');D=I.merge(S,on='icr_id',validate='one_to_one');T=D[D.agency=='DHS/TSA'];C=D[(D.agency!='DHS/TSA')&D.complexity.isin(['high','very high'])&(D.tsa_relevance=='high')]
weights=dict(reproducibility=20,provenance=15,segmentation=15,labor=10,item13=10,item14=10,item15=10,validation=5,consistency=5)
assert len(D)==73 and len(T)==10 and D.omb_control_number.nunique()==73
assert (D[list(weights)].sum(axis=1)==D.total).all()
D['item12_composite_out_of_60']=D[list(weights)[:4]].sum(axis=1)
D['excluding_13_14_rescaled']=(D.total-D.item13-D.item14)/80*100
for _,r in read('score-sensitivity.csv').iterrows():
 d=D[D.icr_id==r.icr_id].iloc[0]
 for col in ['item12_composite_out_of_60','excluding_13_14_rescaled']:assert abs(d[col]-r[col])<1e-8
for _,r in read('agency-summary.csv').iterrows():
 q=D[D.agency==r.agency].total
 for k,v in dict(n=len(q),mean=q.mean(),median=q.median(),min=q.min(),max=q.max(),population_sd=q.std(ddof=0)).items():assert abs(float(r[k])-v)<=.011
out(D.sort_values(['agency','icr_id']),'benchmark-comparison.csv')
long=D.melt(id_vars=['icr_id','agency','complexity','tsa_relevance'],value_vars=list(weights),var_name='dimension',value_name='points');long['maximum']=long.dimension.map(weights);long['fraction_of_maximum']=long.points/long.maximum
out(long,'dimension-comparison.csv')
# preserve source values, metadata and scored rationales for downstream evidence work
rows=[]
for p in sorted((R/'icrs').glob('*/extraction.json')):
 j=json.loads(p.read_text())
 for dim,score in j['score'].items():
  rows.append(dict(icr_id=j['icr_id'],dimension=dim,points=score,maximum=weights[dim],rationale=j['score_rationale'][dim],source_ids=';'.join(j['source_ids']),locator=j.get('score_locators',{}).get(dim,{}).get('section','Items 12-15'),evidence_version='M1-1.0.0'))
out(pd.DataFrame(rows),'scoring-rationale.csv')
checks=read('calculation-checks.csv')
allowed={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow,ast.USub:operator.neg,ast.UAdd:operator.pos}
def calc(n):
 if isinstance(n,ast.Expression):return calc(n.body)
 if isinstance(n,(ast.List,ast.Tuple)):return [calc(x) for x in n.elts]
 if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id in ('sum','round') and not n.keywords:return {'sum':sum,'round':round}[n.func.id](*[calc(x) for x in n.args])
 if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)):return n.value
 if isinstance(n,ast.BinOp) and type(n.op) in allowed:return allowed[type(n.op)](calc(n.left),calc(n.right))
 if isinstance(n,ast.UnaryOp) and type(n.op) in allowed:return allowed[type(n.op)](calc(n.operand))
 raise ValueError(ast.dump(n))
for _,r in checks.iterrows():
 v=calc(ast.parse(r.formula,mode='eval'));assert math.isclose(v,float(r.calculated),rel_tol=1e-10,abs_tol=1e-7),(r.label,v)
 assert math.isclose(v-float(r.reported),float(r.difference),rel_tol=1e-9,abs_tol=1e-6)
out(checks.groupby(['agency','arithmetic_status']).size().unstack(fill_value=0).reset_index() if False else checks.groupby('arithmetic_status').size().rename('expressions').reset_index(),'check-status-counts.csv')
# explicit figure membership
plot=D[D.icr_id.isin(set(T.icr_id)|set(C.icr_id))][['icr_id','agency','title','complexity','tsa_relevance','total']].copy();plot['group']=np.where(plot.agency=='DHS/TSA','TSA','Other high-relevance complex ICRs');out(plot,'score-observations.csv','figure-data')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.labelcolor':'#243746','text.color':'#243746','xtick.color':'#243746','ytick.color':'#243746','pdf.fonttype':42})
fig,ax=plt.subplots(figsize=(8,3.4))
for yi,(label,q,color) in enumerate([('TSA',T,'#007f86'),('Other high-relevance\ncomplex ICRs',C,'#697e95')]):
 seen={}
 for _,r in q.sort_values(['total','icr_id']).iterrows():
  seen[r.total]=seen.get(r.total,0)+1
  count=(q.total==r.total).sum();off=(seen[r.total]-(count+1)/2)*.085
  ax.scatter(r.total,yi+off,s=44,c=color,edgecolors='white',linewidth=.4,zorder=3)
 ax.text(101,yi,f'n = {len(q)}',ha='left',va='center',fontsize=9)
ax.set_yticks([0,1],['TSA','Other high-relevance\ncomplex ICRs']);ax.set_ylim(-.5,1.5);ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xticks(range(0,101,20));ax.set_xlabel('Observable reconstruction score (0-100 points)');ax.grid(axis='x',color='#e5e9ed');ax.tick_params(axis='y',length=0)
fig.tight_layout();fig.savefig(R/'report/figures/tsa-comparators.pdf',bbox_inches='tight');fig.savefig(R/'report/figures/tsa-comparators.png',dpi=180,bbox_inches='tight');plt.close(fig)
ids=['202404-1220-001','202310-1220-004','202310-0607-003','202503-3060-020','202508-1218-005','202408-1625-012','202405-0704-002','202405-1652-001','202406-1652-001','202504-1652-008']
labels=['BLS SOII [H; technique]','BLS NCS [H; technique]','Census AIES [VH; technique]','FCC IPCS [H; high]','OSHA process safety [VH; high]','USCG security [H; high]','DOD CMMC [VH; high]','TSA flight training [H; high]','TSA aircraft operators [H; high]','TSA TWIC [H; high]']
H=D.set_index('icr_id').loc[ids];out(H.reset_index()[['icr_id','agency','complexity','tsa_relevance']+list(weights)],'dimension-profile.csv','figure-data')
# use actual metadata for labels
names=['BLS SOII','BLS NCS','Census AIES','FCC IPCS','OSHA process safety','USCG security','DOD CMMC','TSA flight training','TSA aircraft operators','TSA TWIC']
labels=[f"{name} [{dict(low='L',medium='M',high='H',**{'very high':'VH'})[r.complexity]}; {r.tsa_relevance}]" for name,(_,r) in zip(names,H.iterrows())]
fig,ax=plt.subplots(figsize=(8.5,5.5));a=H[list(weights)].to_numpy();im=ax.imshow(a/np.array(list(weights.values())),vmin=0,vmax=1,cmap='YlGnBu',aspect='auto')
for i in range(a.shape[0]):
 for j in range(a.shape[1]):ax.text(j,i,str(a[i,j]),ha='center',va='center',color='white' if a[i,j]/list(weights.values())[j]>.63 else '#243746',fontsize=10)
ax.set_yticks(range(len(H)),labels);ax.set_xticks(range(9),['Calc.\n/20','Source\n/15','Segm.\n/15','Labor\n/10','13\n/10','14\n/10','15\n/10','Valid.\n/5','Cons.\n/5']);ax.tick_params(length=0);fig.colorbar(im,ax=ax,shrink=.6,label='Fraction of dimension maximum');fig.tight_layout();fig.savefig(R/'report/figures/dimension-profile.pdf',bbox_inches='tight');fig.savefig(R/'report/figures/dimension-profile.png',dpi=180,bbox_inches='tight');plt.close(fig)
fcc=json.loads((R/'icrs/202503-3060-020/extraction.json').read_text())['model']['item15']
v=[fcc[x] for x in ['old_hours','new_rules','revised_rules','expanded_population','new_hours']];start=[0,v[0],sum(v[:2]),sum(v[:3]),0]
F=pd.DataFrame({'stage':['Prior baseline','New rules','Revised rules','Expanded population','New estimate'],'annual_hours':v,'bar_start':start,'source_id':'SRC-0064','locator':'Item 15','icr_id':'202503-3060-020'});out(F,'fcc-change-bridge.csv','figure-data');assert sum(v[:4])==v[4]
fig,ax=plt.subplots(figsize=(8,3.8));ax.bar(range(5),v,bottom=start,color=['#243746','#008b8b','#008b8b','#008b8b','#243746'],width=.65)
for i,(value,b) in enumerate(zip(v,start)):ax.text(i,b+value+350,('+' if i in [1,2,3] else '')+f'{value:,}',ha='center',fontsize=11)
ax.set_xticks(range(5),['Prior\nbaseline','New\nrules','Revised\nrules','Expanded\npopulation','New\nestimate']);ax.set_ylabel('Annual burden hours');ax.set_ylim(0,18000);ax.grid(axis='y',color='#e5e9ed');ax.set_axisbelow(True);fig.tight_layout();fig.savefig(R/'report/figures/fcc-change-bridge.pdf',bbox_inches='tight');fig.savefig(R/'report/figures/fcc-change-bridge.png',dpi=180,bbox_inches='tight');plt.close(fig)
stats={'n':len(D),'components':D.agency.nunique(),'tsa_n':len(T),'tsa_mean':T.total.mean(),'tsa_range':[int(T.total.min()),int(T.total.max())],'comparator_n':len(C),'tsa_item12_mean':D[D.agency=='DHS/TSA'].item12_composite_out_of_60.mean(),'tsa_sensitivity_mean':D[D.agency=='DHS/TSA'].excluding_13_14_rescaled.mean(),'checks':len(checks),'status_counts':checks.arithmetic_status.value_counts().to_dict(),'score_sums_pass':True,'sensitivity_recomputed':True,'agency_summaries_recomputed':True,'arithmetic_replay_pass':True,'scoring_rationale_rows':len(rows)}
(R/'report/audit/quantitative-audit.json').write_text(json.dumps(stats,indent=2)+'\n');print(json.dumps(stats,indent=2))
