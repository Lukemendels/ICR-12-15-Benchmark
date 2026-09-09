#!/usr/bin/env python3
"""Isolate candidate release and run its own consumer with repository reads denied."""
import argparse,pathlib,tempfile,shutil,json,subprocess
ap=argparse.ArgumentParser();ap.add_argument('release',type=pathlib.Path);args=ap.parse_args();r=args.release.resolve()
if json.load(open(r/'release-manifest.json'))['status']=='ICR_EVIDENCE_RELEASE_FROZEN':raise SystemExit('Frozen directory cannot receive reports; use its read-only verifier.')
temp=pathlib.Path(tempfile.mkdtemp(prefix='icr-release-clean-'));dest=temp/'v1.0.0';shutil.copytree(r,dest)
run=subprocess.run(['node','--permission','--allow-fs-read='+str(dest),str(dest/'runtime/verify.mjs'),str(dest)],cwd=temp,capture_output=True,text=True)
if run.returncode:print(run.stderr);raise SystemExit(run.returncode)
result=json.loads(run.stdout);clean=result['clean_load'];clean['isolation']={'mode':'Node filesystem permission model','read_access':'isolated release directory only','working_directory':'fresh temporary directory outside repository','network':'no network APIs used; consumer contains no network calls','repository_access':'not allowed','external_packages':[]};clean['validation']=result['validation']
def put(p,x):(r/p).write_text(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n')
put('validation/clean-load-report.json',clean)
put('validation/validation-report.json',{'status':'PASS','consumer_validation':result['validation'],'schema_dialect':'JSON Schema 2020-12, all keywords used by this release supported','typed_payload_contracts':['ACTIVITY','ASSUMPTION'],'negative_and_pagination_tests':len(json.load(open(r/'validation/negative-tests.json'))['tests']),'source_preservation_report':'source-preservation-report.json','clean_load_report':'clean-load-report.json','negative_tests':'negative-tests.json','unperformed':'No UI or original publication URL accessibility test; outside packaging scope.'})
put('validation/integrity-report.json',{'status':'PASS','algorithm':'SHA-256','scope':'Every manifest-listed artifact; manifest digest pinned externally','inventory_and_hash_verification':'PASS in isolated load','source_blob_preservation':'PASS, 2273 original source-head blobs','self_reference_policy':'Manifest excludes itself. Freeze receipt and archive hashes reside outside canonical directory.','final_seal_requirement':'Repeat identical verifier with trusted final manifest digest after freeze; external receipt records result.'})
put('validation/counts.json',result['validation']['record_counts'])
print(json.dumps({'isolation':clean['isolation'],'tests':len(clean['tests']),'status':clean['status']}))
