/** Diagnostic harness: imports baseline code; extracts page functions unchanged.
 * Host dialogs/files and SQL IPC are replaced only at the I/O boundary.
 * Run: node integration/icr-tool-validation/reproduce.mjs /home/luke/Projects/icr-tool
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const target=path.resolve(process.argv[2]);
const out=path.dirname(new URL(import.meta.url).pathname);
const app=path.join(target,'app');
const require=createRequire(path.join(app,'package.json'));
const esbuild=require('esbuild'),ts=require('typescript');
const temp=fs.mkdtempSync(path.join(os.tmpdir(),'icr-reproduce-'));
function functions(file,names){
 const text=fs.readFileSync(file,'utf8').replace(/^<script lang="ts">/,'').split('</script>')[0];
 const tree=ts.createSourceFile(file+'.ts',text,ts.ScriptTarget.Latest,true);
 const found=tree.statements.filter(n=>ts.isFunctionDeclaration(n)&&names.includes(n.name?.text));
 if(found.length!==names.length)throw Error('Missing function '+file);
 return found.map(n=>n.getText(tree)).join('\n');
}
const draftFns=functions(path.join(app,'src/routes/draft/+page.svelte'),['blank','blankGov','sv','buildProject','loadProject','saveProject','pickWage','pickLoadFactor','checkPropagation','applyPrompt','doExportMarkdown','doExportXlsx']);
const reviewFns=functions(path.join(app,'src/routes/review/+page.svelte'),['runReview','persistRun']);
const gateText=fs.readFileSync(path.join(app,'src/lib/review/gate4.test.ts'),'utf8');
const gateTree=ts.createSourceFile('gate.ts',gateText,ts.ScriptTarget.Latest,true);
const gateDeclarations=gateTree.statements.filter(n=>ts.isVariableStatement(n)||ts.isFunctionDeclaration(n)).map(n=>n.getText(gateTree)).join('\n');
const source=`
import fs from 'node:fs';
import {DatabaseSync} from 'node:sqlite';
import {parseDraft,SCHEMA_VERSION,sourcedValue} from './src/lib/model/draft';
import {exportDraft} from './src/lib/export/markdown';
import {exportXlsx} from './src/lib/export/xlsx';
import {projectPopulation,threeYearAverage} from './src/lib/calc/annualize';
import {toDollarYear} from './src/lib/calc/dollars';
import {activityBurden} from './src/lib/calc/burden';
import {reviewDocument,allRules} from './src/lib/review';
import {MINI_SS} from './src/lib/review/fixture';
import {parseSupportingStatement} from './src/lib/review/parse/parse';
import {parseOewsXlsx,parseEcecXlsx} from './src/lib/import/xlsximport';
import * as DB from './src/lib/db/db';
import ExcelJS from 'exceljs';
const {latestSeriesFor,sourcesById,burdenFor,getDb,saveReviewRun}=DB;
const target=${JSON.stringify(target)},temp=${JSON.stringify(temp)},out=${JSON.stringify(out)};
let sqlite;
function connect(name){sqlite?.close();sqlite=new DatabaseSync(name);}
function stmt(sql,params=[]){const s=sqlite.prepare(sql);return [s,Object.fromEntries(params.map((v,i)=>['$'+(i+1),v]))];}
globalThis.__sql={select:async(sql,params=[])=>{let[s,p]=stmt(sql,params);return s.all(p)},execute:async(sql,params=[])=>{let[s,p]=stmt(sql,params);let r=s.run(p);return {lastInsertId:Number(r.lastInsertRowid),rowsAffected:Number(r.changes)}}};
const facts={};
const raw=new DatabaseSync(target+'/data/icr.db',{readOnly:true});
facts.database={integrity:raw.prepare('PRAGMA integrity_check').all(),foreignKeys:raw.prepare('PRAGMA foreign_key_check').all(),version:raw.prepare('PRAGMA user_version').get(),tables:raw.prepare("SELECT name,sql FROM sqlite_master WHERE type IN ('table','index') ORDER BY type,name").all(),counts:{},series:raw.prepare('SELECT series_kind,year,count(*) n FROM reference_series GROUP BY series_kind,year').all()};
for(const {name} of raw.prepare("SELECT name FROM sqlite_master WHERE type='table'").all())facts.database.counts[name]=raw.prepare('SELECT count(*) n FROM "'+name+'"').get().n;
raw.close();
fs.copyFileSync(target+'/data/icr.db',temp+'/local-a.db');connect(temp+'/local-a.db');
facts.search={icrs:(await DB.listIcrs()).length,sources:(await DB.listSources()).length,sourceSearch:(await DB.searchSources('wage')).map(x=>({id:x.id,name:x.name})),sections:(await DB.searchSections('burden')).length,series:(await DB.listSeries()).length,active:(await DB.searchActiveSeries('oews_wage','11-0000')).slice(0,2)};
const v=n=>({value:n,sourceId:1,locator:'Table X row Y',rawQuote:'Fixture supporting quote'});
const base=parseDraft({schemaVersion:1,meta:{title:'Validation fixture',controlNumber:'1652-0001',baseYear:2026,dollarYear:2026,analysisYears:[2026,2027,2028],createdDate:'2024-01-02'},activities:[{id:'a1',name:'Reporting',respondents:v(100),responsesPerRespondent:v(2),minutesPerResponse:v(30),wage:{socCode:'11-0000',base:v(20),loadFactor:v(1.5),baseSeries:{seriesKind:'other',key1:'fixture',vintage:'2026',year:2026}},otherCostPerRespondent:v(5),growth:{kind:'fixedPct',annualPct:v(10)},notes:'Keep activity note'}],frozenParameters:[{id:'p1',name:'Parameter',value:v(7),propagatesTo:['Q12']}],capitalCosts:[{id:'c1',name:'Setup',kind:'startup',annualCost:v(200)},{id:'c2',name:'Maintenance',kind:'om',annualCost:v(100)}],governmentCosts:[{kind:'fixed',id:'g1',name:'Federal fixed',annualCost:v(1000)},{kind:'labor',id:'g2',name:'Federal labor',annualHours:v(10),hourlyWage:v(40)}],narrativeOverrides:{q12:'KEEP Q12',q13:'KEEP Q13',q14:'KEEP Q14'}});
let title='',controlNumber='',dollarYear=2026,baseYear=2026,yearsText='',roundingMode='roundLast',activities=[],govCosts=[],notice='',error='',counter=0,prompts=[];
let inputPath=temp+'/input.icrdraft.json',outputPath=temp+'/saved.icrdraft.json';
const open=async()=>inputPath,save=async()=>outputPath,readTextFile=async p=>fs.readFileSync(p,'utf8'),writeTextFile=async(p,s)=>fs.writeFileSync(p,s),writeFile=async(p,s)=>fs.writeFileSync(p,s);
// Svelte's derived analysisYears evaluated on demand by the harness getter.
${draftFns.replace('dollarYear, baseYear, analysisYears,','dollarYear, baseYear, analysisYears: yearsText.split(/[,\\s]+/).filter(Boolean).map(Number).filter(n => !Number.isNaN(n)),')}
function diffs(a,b,p=''){let r=[];if(a&&b&&typeof a==='object'&&typeof b==='object'){for(let k of new Set([...Object.keys(a),...Object.keys(b)]))r.push(...diffs(a[k],b[k],p+'/'+k));}else if(JSON.stringify(a)!==JSON.stringify(b))r.push({path:p,before:a??null,after:b??null});return r;}
fs.writeFileSync(inputPath,JSON.stringify(base));await loadProject();await saveProject();
const saved=parseDraft(JSON.parse(fs.readFileSync(outputPath,'utf8')));
facts.roundtrip={loadNotice:notice,error,differences:diffs(base,saved),jsonOnlyLossless:JSON.stringify(parseDraft(JSON.parse(JSON.stringify(base))))===JSON.stringify(base)};
fs.writeFileSync(out+'/fixture.icrdraft.json',JSON.stringify(base,null,2)+'\\n');
const per=parseDraft({...base,governmentCosts:[{kind:'perResponse',id:'g3',name:'Federal responses',responses:v(100),minutesPerResponse:v(6),hourlyWage:v(40)}]});
fs.writeFileSync(inputPath,JSON.stringify(per));await loadProject();facts.perResponse={form:structuredClone(govCosts),rebuilt:buildProject(),error};
const sources=await sourcesById();
const md=exportDraft(base,sources);fs.writeFileSync(out+'/fixture-export.md',md.markdown);
const pops=projectPopulation(v(100),2026,[2026,2027,2028],base.activities[0].growth,'roundLast');
facts.projection={populations:pops.map(x=>x.value),expectedHoursAverage:threeYearAverage(pops.map(x=>x.value),'roundLast'),observedAnnualization:md.markdown.split('## Annualization')[1].split('---')[0],twoYearAverage:threeYearAverage([100,200],'roundLast'),dollarHelper:toDollarYear(3000,2026,2028,{2026:v(100),2028:v(120)},'roundLast')};
const changed=parseDraft({...base,meta:{...base.meta,dollarYear:2028}});
facts.projection.dollarYearOnlyChangesLabel=exportDraft(changed,sources).markdown.replace('**Dollar year:** 2028','**Dollar year:** 2026')===md.markdown;
const bytes=await exportXlsx(base,sources);fs.writeFileSync(temp+'/fixture.xlsx',bytes);const wb=new ExcelJS.Workbook();await wb.xlsx.load(bytes);
facts.xlsx=Object.fromEntries(wb.worksheets.map(w=>[w.name,w.getSheetValues()]));
facts.item13={emptyCapitalStatement:exportDraft(parseDraft({...base,capitalCosts:[]}),sources).markdown.split('## 13.')[1].split('## 14.')[0],baseBurden:activityBurden(base.activities[0],'roundLast')};
const idOnly=parseDraft({...base,activities:[{...base.activities[0],respondents:{value:100,sourceId:1}}]});
facts.sourceProof={idOnlyAccepted:sourcedValue.safeParse({value:100,sourceId:1}).success,unverifiedCount:exportDraft(idOnly,sources).unverifiedCount,locatorInMarkdown:md.markdown.includes('Table X row Y'),quoteInMarkdown:md.markdown.includes('Fixture supporting quote'),sourcesSheet:facts.xlsx.Sources};
const localSource={name:'Context A source',type:'fixture',tier:3,status:'VERIFIED'};
const idA=await DB.insertSource(localSource,'Validation fixture');
fs.copyFileSync(target+'/data/icr.db',temp+'/local-b.db');connect(temp+'/local-b.db');const idB=await DB.insertSource({...localSource,name:'Context B source'},'Validation fixture');
facts.portability={idA,idB,nameB:(await sourcesById()).get(idB).name};connect(temp+'/local-a.db');facts.portability.nameA=(await sourcesById()).get(idA).name;
const portable=parseDraft({...base,activities:[{...base.activities[0],respondents:{value:100,sourceId:idA}}]});facts.portability.exportA=exportDraft(portable,await sourcesById()).markdown.split('---').at(-1);connect(temp+'/local-b.db');facts.portability.exportB=exportDraft(portable,await sourcesById()).markdown.split('---').at(-1);connect(temp+'/local-a.db');
await DB.insertSeriesVintage({series_kind:'other',key1:'fixture',year:2026,vintage:'2026',value:20,source_id:idA,raw_quote:'old quote'},'Validation');
await DB.importSeriesVintages([{series_kind:'other',key1:'fixture',year:2027,vintage:'2027',value:25,source_id:idA,raw_quote:'new supporting quote'}],'Validation');
fs.writeFileSync(inputPath,JSON.stringify(base));await loadProject();facts.vintage={rows:await DB.listSeries('other'),prompts:structuredClone(prompts),before:buildProject().activities[0].wage};applyPrompt(prompts[0]);facts.vintage.after=buildProject().activities[0].wage;
outputPath=temp+'/workflow.icrdraft.json';await saveProject();inputPath=outputPath;await loadProject();outputPath=temp+'/workflow.md';await doExportMarkdown();facts.workflow={savedReloaded:!error,markdownWritten:fs.existsSync(outputPath),error};outputPath=temp+'/workflow.xlsx';await doExportXlsx();facts.workflow.xlsxWritten=fs.existsSync(outputPath);facts.workflow.xlsxError=error;
let filePath=temp+'/review.md',docDate='2026-08-31',result=null,busy=false;
${reviewFns}
fs.writeFileSync(filePath,MINI_SS);controlNumber='';await runReview();facts.review={score:result.score,verdict:result.verdict,autoFail:result.autoFail,findings:result.findings,passports:result.passports.length};await persistRun();facts.review.saved=sqlite.prepare('SELECT * FROM review_runs').all();facts.review.savedFindings=sqlite.prepare('SELECT count(*) n FROM review_findings').get();
facts.xcomp={ui301:result.findings.filter(f=>f.ruleId==='XCOMP-301'),ui302:result.findings.filter(f=>f.ruleId==='XCOMP-302'),absent:reviewDocument(MINI_SS).findings.filter(f=>f.ruleId.startsWith('XCOMP-30')&&f.ruleId!=='XCOMP-303'),provided:reviewDocument(MINI_SS,{corpusStats:{ececFactorMode:1.42,wageSeriesCounts:{'99-9999':1}}}).findings.filter(f=>f.ruleId==='XCOMP-301'||f.ruleId==='XCOMP-302')};
const bridge='15. ***Explain the reasons for any program changes or adjustments.***\\nPrior baseline: 100 hours. Program change: 20 hours. Adjustment: -10 hours. New burden: 999 hours.\\n';
const bridgeMd=MINI_SS.slice(0,MINI_SS.indexOf('15. ***'))+bridge+'\\n'+MINI_SS.slice(MINI_SS.indexOf('[^1]:'));
if(!bridgeMd.includes('New burden: 999'))throw Error('Item 15 fixture injection failed');
const item15=reviewDocument(bridgeMd);facts.item15={section:parseSupportingStatement(bridgeMd).sections.find(s=>s.questionNo===15),findings:item15.findings.filter(f=>f.location.startsWith('Q15')),exportHas15:md.markdown.includes('## 15.'),schemaRetainsBaseline:'priorBaseline' in parseDraft({...base,priorBaseline:100,componentChanges:[20,-10],newBurden:999}),ruleCount:allRules.length};
const iw=new ExcelJS.Workbook();iw.addWorksheet('OEWS').addRows([['OCC_CODE','OCC_TITLE','H_MEAN'],['11-0000','Management',68.15]]);facts.import={oews:await parseOewsXlsx(await iw.xlsx.writeBuffer())};const ew=new ExcelJS.Workbook();ew.addWorksheet('Table 4 Estimates').addRows([['[June 2026]'],['Private industry workers',46.60,null,32.60]]);facts.import.ecec=await parseEcecXlsx(await ew.xlsx.writeBuffer());try{await parseOewsXlsx(await ew.xlsx.writeBuffer());}catch(e){facts.import.invalidRejected=String(e)}
// Additional export provenance counter-check: government-only and other-cost-only IDs.
const unique=parseDraft({...base,activities:[{...base.activities[0],otherCostPerRespondent:{value:5,sourceId:idA}}],governmentCosts:[{kind:'fixed',id:'g',name:'Federal unique',annualCost:{value:1000,sourceId:idA}}]});
const uw=new ExcelJS.Workbook();await uw.xlsx.load(await exportXlsx(unique,await sourcesById()));facts.xlsxMissingSources={usedId:idA,sourcesRows:uw.getWorksheet('Sources').getSheetValues()};
{
${gateDeclarations}
const defective=reviewDocument(inject(GATE4_BASE,DEFECTS.map(d=>d.edit)),CTX);
const firing=new Set(defective.findings.filter(f=>f.status==='FAIL'||f.status==='STALE').map(f=>f.ruleId));
facts.seeded={detected:DEFECTS.filter(d=>firing.has(d.rule)).map(d=>d.rule),missed:DEFECTS.filter(d=>!firing.has(d.rule)).map(d=>d.rule),score:defective.score,autoFail:defective.autoFail};
}
const corpusMd=(await DB.sectionsFor('1652-0001')).map(s=>s.md_text).join('\\n\\n');const corpusReview=reviewDocument(corpusMd,{docDate:'2024-11-25',burdenRecord:{totalResponses:865,burdenHours:3012,burdenCost:108489,annualFederalCost:200000}});
facts.corpusReview={input:'SQLite sectionsFor(1652-0001), not the absent external golden file',sections:corpusReview.doc.sections.length,score:corpusReview.score,autoFail:corpusReview.autoFail,findings:corpusReview.findings.length,passports:corpusReview.passports.length};
facts.workflow.markdownFigures=fs.readFileSync(temp+'/workflow.md','utf8').includes('$3,750.00');
const check=(ok,label)=>{if(!ok)throw Error('Diagnostic expectation failed: '+label)};
check(facts.roundtrip.differences.length===23,'rich form loss');check(facts.perResponse.rebuilt===null,'perResponse rejected on rebuild');check(facts.portability.idA===facts.portability.idB,'source collision');check(facts.xlsx['Q12 Hour Burden'][2][6]===100,'100 hours');check(facts.xlsx['Q14 Federal Cost'][4][2]===1400,'1400 Federal cost');check(facts.item15.section.mdText.includes('999'),'bridge injection');check(facts.workflow.markdownFigures,'updated wage labor 3750');
fs.writeFileSync(out+'/reproduction-results.json',JSON.stringify(facts,null,2)+'\\n');sqlite.close();console.log(JSON.stringify({output:out+'/reproduction-results.json',temp,roundtripDifferences:facts.roundtrip.differences,perResponse:facts.perResponse,error,workflow:facts.workflow,review:{score:facts.review.score,verdict:facts.review.verdict},item15:facts.item15},null,2));
`;
await esbuild.build({stdin:{contents:source,loader:'ts',resolveDir:app},outfile:temp+'/run.mjs',bundle:true,platform:'node',format:'esm',packages:'external',plugins:[{name:'sql-boundary',setup(b){b.onResolve({filter:/^@tauri-apps\/plugin-sql$/},()=>({path:'sql',namespace:'mock'}));b.onLoad({filter:/.*/,namespace:'mock'},()=>({contents:'export default {load:async()=>globalThis.__sql}'}));}}]});
// package resolution from temporary bundle without installing anything.
fs.symlinkSync(path.join(app,'node_modules'),temp+'/node_modules','dir');
await import(pathToFileURL(temp+'/run.mjs'));
