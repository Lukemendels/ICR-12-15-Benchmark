from pathlib import Path
import json,re
R=Path(__file__).parent
sources={s['source_id']:s for s in map(json.loads,(R/'data/sources.jsonl').read_text().splitlines())}
p=R/'data/claims.jsonl';claims=[json.loads(x) for x in p.read_text().splitlines()]
findings=[
('001','202404-1220-001',['SRC-0008'],'Item12 recording burden and Table9; Item15','normally exempt','BLS separates already-required OSHA recording from normally exempt establishments and phases a270-hour test.','Reusable cross-control obligation and year-specific model; not a claim that all BLS costs fully reconstruct.','segmentation'),
('002','202503-3060-020',['SRC-0064'],'Item15 change explanation and burden table','2,380','FCC reports15175hours and explains a2380-hour reduction from the notice estimate.','Named baseline plus quantified driver bridge is an adoption method.','item15'),
('003','202310-0607-003',['SRC-0099'],'Printed page19/PDFpage20, burden measurement comparison','4.5','Response-analysis survey, questionnaire and paradata estimates differ in scope and magnitude.','Store sample, statistic and measurement scope; do not use median as mean.','validation'),
('004','202501-1210-006',['SRC-0102'],'Introduction and Tables1–3','PRA','EBSA publishes a method intended for regulatory impact and PRA burden calculations.','Direct counterevidence to uniqueness of downstream analytical reuse; does not identify TSA motivation.','labor'),
('005','202405-0704-002',['SRC-0164'],'89FR83177–83192 economic analysis;83211–83213 PRA tables','eMASS','CMMC exposes phased assessment labor and system costs in a final rule alongside ICR burdens.','Security-compliance comparator links PRA and regulatory analysis; maintain scope and cost-type distinctions.','method transfer'),
('006','202406-1652-001',['SRC-0038'],'Item12 checklist table and narrative; Item14 workload tables','54,658','TSA aircraft operators provides eighteen activity rows and federal workload, but checklist narrative dollars conflict with its table.','Keep activity architecture; generate narrative and tables from one model.','consistency'),
('007','202412-1652-001',['SRC-0176'],'Item12 applicant wage footnote and CHRC fee calculation','34.48','Applicant rate used34.48 differs from footnote loading; displayed CHRCfee56.55 times1042500 differs from58954925.','Occupation/compensation transformations and fee calculations require independent checks.','labor'),
('008','202504-1652-008',['SRC-0180'],'Item12 weighted wage and renewal paths; Item14','2,044,400','TWIC wage basket includes2044400truckdrivers; renewals split68%online and32%inperson.','Keep mutually exclusive pathways; national occupation mix is not automatically applicant task mix.','segmentation'),
('009','202606-1652-002',['SRC-0054'],'Item12 online renewal and in-person enrollment equations','31.2','HME online-renewal subset is added while in-person enrollment is charged to the full population.','Potential double count; preserve source formula and require an eligibility partition.','reproducibility'),
('010','202606-1652-001',['SRC-0022','SRC-0026'],'Item12 contact updates; JOLTS FAQ reference periods','13 percent','Surface cyber combines a monthly turnover proxy with annual mobility in a contact-update estimate.','Different time periods and event definitions cannot be combined without a supported transformation.','provenance'),
('011','202405-1218-005',['SRC-0060'],'Items12–13 in-house versus outsourced inspection and unit-price range','50.50','Extinguisher model separates15%noncustomary work into10%in-house and90%outsourced work.','Make-or-buy partition avoids charging purchased labor twice; price and customary shares still need current validation.','item13'),
('012','202508-1218-005',['SRC-0187'],'Item12 coverage assumptions; Table3','56,228','OSHA process safety reconciles2325294to2269066hours with activity changes totaling−56228.','Close regulatory comparator has strong Item15 and segmentation despite stale response-column values.','item15'),
('013','202408-1625-012',['SRC-0174','SRC-0181'],'Item12 appendix and Item15; revised2025 calculation supplement','980','Coast Guard removes980two-minute addendum responses, about33hours, while avoiding duplicate declarations of security.','Direct security comparator illustrates obligation-level change and overlap handling.','item15'),
('014','202401-2070-005',['SRC-0183'],'Tables3–4 and6','18 months','EPA prorates eighteen months of each four-year reporting cycle across a36-month approval period.','Reporting cycles and approval horizons require separate dates; table total typo does not erase useful method.','reproducibility'),
('015','202405-1506-005',['SRC-0185','SRC-0191'],'2024 Items8,12–15;2020 printed31605 and31611 Tables21–22','21.41','FinCEN discusses a21.41-hour large-bank survey against1.98hours and identifies coverage limitations; historical model includes declined cases.','Explicit counterevidence assessment and case-funnel modeling are transferable; rejection of a biased sample does not itself validate the retained mean.','validation'),
('016','202603-0535-001',['SRC-0189'],'Item12 embedded tables1–2; Item15 embedded change table','206,959','NASS separates196035response hours and10924nonresponse hours, totaling206959.','Model advance materials, nonresponse, testing and survey waves separately; embedded tables were visually inspected.','segmentation'),
('017','202502-2060-039',['SRC-0161','SRC-0162'],'CEMS Costs sheet life/discount inputs;2017 memo Tables2-1–4-1',None,'Historical EPA model identifies510899principal,10-year life and7%discount with72752annual recovery.','Annuity method is reproducible; old prices and labor/PRA scope prevent wholesale reuse.','item13'),
('018','202511-1545-005',['SRC-0094','SRC-0100'],'Items12–15 and change supplement','857','IRS business burden uses a calibrated model with857million hours and a quantified change bridge.','Support statistical model nodes, but publicly unavailable coefficients limit independent replication.','reproducibility'),
('019','202404-1220-001',['SRC-0008','SRC-0200'],'SOII Item12; BLS USDL23-2567 civilian sales/office row','32.91','BLS dollar32.91 is September2023 compensation, releasedDecember15; statement labels December2023.','Verified rate, incorrect reference-period label; publication and reference dates must be separate.','provenance'),
('020',None,['SRC-0024','SRC-0025'],'5CFR1320.3(b)(1)–(3);1320.8(a)(4),(a)(6),(d)','objectively supported','Regulation requires an objectively supported burden estimate; usual/customary exclusions require demonstration.','Evidence is part of the compliance floor; deterministic workbooks and full input lineage are enhanced practice.','compliance floor')]
for num,ref,sids,locator,needle,evidence,inference,dim in findings:
 anchors=[]
 if needle:
  for sid in sids:
   lp=sources[sid].get('local_path')
   if not lp:continue
   q=R/lp
   if q.suffix in ['.pdf','.docx']:q=q.with_suffix('.txt')
   if not q.exists() or q.suffix not in ['.txt','.json']:continue
   ls=q.read_text().splitlines()
   for i,line in enumerate(ls):
    if needle.lower() in line.lower():anchors.append({'source_id':sid,'path':str(q.relative_to(R)),'line':i+1,'excerpt':line[:900]});break
 cid='CLM-FINDING-'+num
 row={'claim_id':cid,'registry_type':'curated','source_ids':sids,'locator':locator,'icr_id':ref,'rubric_dimension':dim,'evidence':evidence,'interpretation':inference,'confidence':'high for reported values and source structure; qualified analytical interpretation','verification_status':'Primary source inspected; displayed arithmetic checks stored separately; anchors are navigation aids','evidence_anchors':anchors,'status':'active'}
 claims=[x for x in claims if x['claim_id']!=cid]+[row]
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims))
print('claims',len(claims),'curated',sum(x.get('registry_type')=='curated' for x in claims))
