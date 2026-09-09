import pathlib,json
ROOT=pathlib.Path(__file__).resolve().parents[2]
s=json.load(open(ROOT/'evidence-graph/schema.json'));errors=[]
for k in ['entity_types','edge_types','epistemic_statuses','classifications','node_required','edge_required','provenance_required']:
 if not s.get(k) or len(s[k])!=len(set(s[k])):errors.append(k)
for k in ['PUBLISHED','CALCULATED','NORMALIZED','INFERRED','UNRESOLVED']:
 if k not in s['epistemic_statuses']:errors.append(k)
for name in ['normalization-rules','similarity-rules','shape-taxonomy']:
 if not (ROOT/'evidence-graph'/f'{name}.md').is_file():errors.append(name)
out={'schema_version':s['schema_version'],'result':'FAIL' if errors else 'PASS','errors':errors,'scope':'Ontology enums, required record/provenance fields and protocol presence. Populated graph validation is a later gate.','decisions':['Preserve committed ontology without rebuilding architecture.','Unknown shape dimensions remain null with reasons.','Similarity strength is separate from consistency classification and epistemic status.','Activity scope and period are mandatory comparison predicates; administrative inventory is not burden evidence.','Freeze requires source-locator validation, deterministic replay, challenge and extraction coverage; enum checks alone are insufficient.']}
p=ROOT/'mission-3/validation';p.mkdir(exist_ok=True);(p/'schema-validation.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
