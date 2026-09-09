"""Normalize reusable M1 TSA evidence by reference; never modify frozen inputs."""
import pathlib,json,hashlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
FAMILIES={'labor':'labor_compensation','item13':'nonlabor_cost','item14':'federal_cost','item15':'change_baseline','assumptions':'estimation_basis'}
def ident(*parts):return hashlib.sha256('|'.join(map(str,parts)).encode()).hexdigest()[:18]
def run(refs,batch):
 activities=[];parameters=[];reviews=[]
 for ref in refs:
  path=f'icrs/{ref}/extraction.json';d=json.load(open(ROOT/path));sid=d['source_ids'][-1]
  def prov(pointer,original):return {'source_id':sid,'document_id':ref,'locator':path+'#'+pointer,'original':json.dumps(original,ensure_ascii=False),'extraction_method':'Reviewed frozen M1 structured evidence reused by exact JSON pointer','transformation':'M3 semantic normalization; M1 values and interpretation preserved','status':'NORMALIZED'}
  for i,row in enumerate(d['model'].get('activities',[])):
   x=dict(zip(d['model']['activity_columns'],row));x['id']='ACT-'+ident(ref,'m1',i);x['ref']=ref;x['control']=d['omb_control_number'];x['batch']=batch;x['epistemic_status']='NORMALIZED';x['provenance']=prov('/model/activities/'+str(i),row);h=x.get('hours_per_response');x['minutes_per_response']=h*60 if h is not None else None;x['unit']='response';x['period']='annual';x['measurement_basis']='See frozen statement and assumption evidence; unknown active versus elapsed';x['actor']='respondent';x['lifecycle']=None;x['unknown_reason']='Source-specific actor/role, recurrence and lifecycle require linked source context; no default equivalence';x['scope_note']='M1 selected model activity or explicitly aggregated activity family; not a complete internal model replica'
   activities.append(x)
  def leaves(v,pointer,family):
   if isinstance(v,dict):
    for k,w in v.items():leaves(w,pointer+'/'+k,family)
   elif isinstance(v,list) and any(isinstance(w,(list,dict)) for w in v):
    for i,w in enumerate(v):leaves(w,pointer+'/'+str(i),family)
   else:parameters.append({'id':'PAR-'+ident(ref,pointer),'ref':ref,'control':d['omb_control_number'],'batch':batch,'family':family,'name':pointer,'value':v,'unit':None,'period':None,'vintage':None,'scope':'Frozen M1 extracted field; units and period as named/contextualized in original model; null is not zero','epistemic_status':'NORMALIZED','provenance':prov(pointer,v)})
  for key,family in FAMILIES.items():leaves(d['model'].get(key),'/model/'+key,family)
  reviews.append({'ref':ref,'batch':batch,'basis':'REUSED_FROZEN_M1','review_scope':'All M1 structured model activities, labor, Items13–15 and assumption fields; raw statement retained by reference; M3 cross-comparisons and challenge not yet complete','source_paths':[path,f'icrs/{ref}/raw/supporting-statement-a-1.txt'],'issues_preserved':d['reconstruction_issues']})
 out=ROOT/'mission-3/extractions';out.mkdir(exist_ok=True)
 for name,data in [('activities',activities),('parameters',parameters),('reviews',reviews)]:
  (out/f'{batch}-{name}.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data))
 print(batch,len(activities),len(parameters),len(reviews))
if __name__=='__main__':run(sys.argv[2:],sys.argv[1])
