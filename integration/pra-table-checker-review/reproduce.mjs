// Review harness only: reads authoritative code; bundles Jay modules into /tmp.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import os from 'node:os';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';
const root = process.cwd();
const jayRoot = process.argv[2] || '/home/luke/Projects/icr-tool';
const out = process.argv[3] || path.join(root, 'integration/pra-table-checker-review/execution-results.json');
const sha = dir => execFileSync('git', ['-C',dir,'rev-parse','HEAD'], {encoding:'utf8'}).trim();
assert.equal(sha(jayRoot), 'e72fae4b1d2a37d7a22aeb8ab5b3555f423af79e');
const html = fs.readFileSync('pra-q12-15-table-checker.html','utf8');
const script = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)].at(-1)[1];
const nodes = new Map();
const getNode = id => {
  if (!nodes.has(id)) nodes.set(id,{value:id==='sectionFilter'?'all':'',textContent:'',innerHTML:'',style:{},addEventListener(type,fn){this[type]=fn;}});
  return nodes.get(id);
};
let clipboard = '', fallback = '';
const context = vm.createContext({document:{readyState:'complete',getElementById:getNode},navigator:{clipboard:{writeText:async t=>{clipboard=t;}}},window:{prompt:(_p,t)=>{fallback=t;}},setTimeout:fn=>fn()});
vm.runInContext(script,context,{filename:'authoritative-checker.js'});
const evaluate = expr => vm.runInContext(expr,context);
const snapshot = x => JSON.parse(JSON.stringify(x,(_k,v)=>typeof v==='number'&&!Number.isFinite(v)?String(v):v));
const cases=[];
function run(id,input,note){
  getNode('sourceText').value=input;
  evaluate('runChecks()');
  const result=snapshot(evaluate('({counts:counts(),tables:state.tables,checks:state.checks,report:state.lastReportText})'));
  result.conclusion=getNode('numericConclusion').textContent;
  const row={id,note,input,...result}; cases.push(row); return row;
}
const sample=evaluate('SAMPLE_TEXT');
const sampleRun=run('sample',sample,'Exact embedded prototype sample, not separately verified frozen evidence.');
assert.equal(sampleRun.checks.filter(x=>x.category==='calculation').length,38);
assert.equal(sampleRun.checks.filter(x=>x.category==='crossTable').length,12);
run('empty','','Empty input branch.');
const unsupported=run('unrelated','No quantitative tables here.','Out-of-scope handling.');
assert.equal(unsupported.counts.tables,6); // Defect: "not found" ends with "found".
assert.equal(Object.values(unsupported.tables).filter(t=>t.rows.length).length,0);
run('narrative-literals',sample+'\n1.6265 and 1.6266\nTable 4 summarizes these calculations','Both hard-coded narrative predicates.');
run('narrative-unrelated',sample+'\nHistorical factor: 1.62650; unrelated identifier: 11.62660','Substring false positive, no semantic relation.');
run('narrative-other-factors',sample+'\nCurrent compensation factor is 1.5. Current compensation factor is 1.6.','Other inconsistent factors ignored.');
run('renamed-captions',sample.replaceAll('Table ', 'TABLE '),'Case-sensitive captions fail.');
run('changed-headers',sample.replace('Year | % Increase | LEOs Flying Armed | % Using 413A | Number of 413A Responses','Label | Wage | Minutes | Dollars | Cost'),'Headers ignored; same arithmetic despite changed meaning.');
run('calendar-years',sample.replace(/^([123]) \|/gm,(_,n)=>(2025+Number(n))+' |'),'Year labels outside 1/2/3 ignored.');
run('reordered-one-table',sample.replace('1 | 50% | 104,686 | 52,343\n2 | 95% | 120,389 | 114,370','2 | 95% | 120,389 | 114,370\n1 | 50% | 104,686 | 52,343'),'Same year values, different order creates false cross-links.');
run('fourth-year',sample.replace('Average | 119,168 | 21,661','4 | 0% | 999 | 100% | 999\nAverage | 119,168 | 21,661'),'Fourth year silently discarded.');
run('missing-average-term',sample.replace('120,389 | 5%','n/a | 5%'),'Finite-only mean omits missing term.');
run('padded-average',sample.replace('Average | 119,168 | 21,661','Average | | 119,168 | | 21,661'),'Ordinary full-width average misaligned to compact fixed layout.');
run('unchecked-averages',sample.replace('Average | 21,661 | 1,444.8 | $90,098','Average | 1 | 1 | $1'),'Table 2 average not checked.');
run('unchecked-federal-link',sample.replace('1 | 52,343 | 0.0250 | 1,309 | $92,088','1 | 100 | 0.0250 | 2.5 | $176'),'Federal responses not linked to Table 1.');
run('changed-prose-rate',sample+'\nThe hourly compensation rate is $100.00; prior population is 90,000.','Hard-coded $62.36 and 83749 unchanged.');
run('aligned-pipes',sample.split('\n').flatMap(l=>l.startsWith('Year |')?['| '+l+' |','| '+l.split('|').map(()=> '---').join(' | ')+' |']:l.includes('|')?['| '+l+' |']:[l]).join('\n'),'Optional outer pipes and Markdown alignment accepted.');
run('blank-mid-table',sample.replace('2 | 15%', '\n2 | 15%'),'Blank line terminates populated table.');
run('caption-only', 'Table 1: Form 413A Responses','Presence pass with no parsed rows.');
// Independently constructed, fully coherent fixture uses the checker's declared constants.
const tables={
 table1:[['Year','Increase','LEOs','Share','Responses'],['1','0%','83749','100%','83749'],['2','0%','83749','100%','83749'],['3','0%','83749','100%','83749'],['Average','83749','83749']],
 table2:[['Year','Responses','Time','Hours','Cost'],...['1','2','3'].map(y=>[y,'83749','1','83749',String(83749*62.36)])],
 table3:[['Year','Share','LEOs','Occurrences'],...['1','2','3'].map(y=>[y,'100%','83749','83749'])],
 table4:[['Year','Occurrences','Share','Registrations'],...['1','2','3'].map(y=>[y,'83749','100%','83749'])],
 table5:[['Year','Registrations','Hours','Cost','Occurrences','Hours','Cost'],...['1','2','3'].map(y=>[y,'83749',String(83749*.0833),String(83749*.0833*62.36),'83749',String(83749*.0333),String(83749*.0333*62.36)])],
 federal:[['Year','Responses','Time','Hours','Cost'],...['1','2','3'].map(y=>[y,'83749','1','83749',String(83749*70.35)])]
};
const captions=snapshot(evaluate('TABLE_CONFIG'));
const serialize=t=>Object.entries(t).map(([k,rows])=>captions[k].caption+'\n'+rows.map(r=>r.join(' | ')).join('\n')).join('\n');
const coherent=run('coherent',serialize(tables),'Independent arithmetic control; duplicate numbering remains a warning.');
assert.equal(coherent.counts.calcIssues,0); assert.equal(coherent.counts.crossIssues,0); assert.equal(coherent.counts.numericPasses,50);
// Exercise each of the 14 internal comparison sites with a large target perturbation.
for(const [key,row,col] of [['table1',1,2],['table1',1,4],['table1',4,1],['table1',4,2],['table2',1,3],['table2',1,4],['table3',1,3],['table4',1,3],['table5',1,2],['table5',1,3],['table5',1,5],['table5',1,6],['federal',1,3],['federal',1,4]]){
 const t=structuredClone(tables); t[key][row][col]=String(Number(t[key][row][col])+1000);
 const r=run(`perturb-${key}-${row}-${col}`,serialize(t),'Increase one target cell by 1000; may trigger dependent checks.');
 assert.ok(r.counts.calcIssues>0);
}
const pipelineFile='mission-3/sources/202512-1652-001/e21e863d84c9cbf0.txt';
const pipelineText=fs.readFileSync(pipelineFile,'utf8');
const paragraph=pipelineText.split('\n')[215];
assert.ok(paragraph.includes('$122.27'));
run('pipeline-paragraph','14. Estimates of annualized cost to the Federal government\n'+paragraph,'Verbatim source L216 with explicit synthetic Q14 heading.');
run('pipeline-full',pipelineText,'Unmodified frozen text; path '+pipelineFile);
const bridge=JSON.parse(fs.readFileSync('release/icr-evidence/v1.0.0/tsa/item15-bridges.json'))[0];
const bridgeText='15. Explain program changes and adjustments\nPrior baseline: '+bridge.baseline+' hours.\n'+bridge.components.map((n,i)=>n+': '+bridge.component_deltas[i]+' hours.').join('\n')+'\nNew burden: '+bridge.current+' hours.';
run('twic-bridge',bridgeText,'Synthetic readable serialization of frozen BASELINE-TWIC-2025, signs retained.');
run('twic-wrong-total',bridgeText.replace('510471 hours','510472 hours'),'One-hour mutation of frozen bridge serialization.');
run('twic-current-full',fs.readFileSync('mission-3/sources/202504-1652-008/ec91651842d62d7c.txt','utf8'),'Unmodified current frozen statement.');
run('twic-prior-full',fs.readFileSync('mission-3/sources/202502-1652-004/4639c859f157e253.txt','utf8'),'Unmodified predecessor frozen statement.');
run('headed-sample','12. Provide estimates of hour burden\n'+cases.find(c=>c.id==='aligned-pipes').input,'Synthetic Q12 heading plus standard Markdown formatting; same sample values.');
const generic='12. Provide estimates of hour burden\nRespondents submit annually. The total is 100 hours.\n| Activity | Respondents | Frequency | Hours per response | Total hours |\n| --- | --- | --- | --- | --- |\n| A | 100 | 2 | 0.5 | 100 |';
run('generic-hour-pass',generic,'Independent standard burden table control.');
run('generic-hour-fail',generic.replace('| 0.5 | 100 |','| 0.5 | 999 |'),'Wrong total should fail row arithmetic.');
const compliance=pipelineText.split('\n').find(l=>l.startsWith('Compliance Inspection:'));
run('pipeline-compliance','14. Estimates of annualized cost to the Federal government\n'+compliance,'Additional frozen bounded case: 4800 × 88.39 = 424272 vs 424261.04, compatible with cent-rate rounding; original paragraph.');
const micro=[];
for(const expr of [
'parseNumber("-$1,234.50")','parseNumber("(123)")','parseNumber("−10")','parseNumber("10 hours")','parseNumber("5%")','parseNumber("0")','parseNumber("")','parseNumber("n/a")','parseNumber("1,2")','parseNumber("1e3")','parseNumber("0x10")',
'average([100,NaN,300])','average([])','roundForDisplay(-1.5,0)','roundForDisplay(1.005,2)',
'classify(100,100,0,0)','classify(100.4,100.1,0,0)','classify(101,100,1,0)','classify(102,100,1,0)','classify(NaN,100,1,0)',
'diffText(100.4,100.1,"number",0)','diffText(100.51,100.49,"number",0)','diffText(99,100,"money",0)',
'getSection("before Provide estimates of hour and cost burdens KEEP For collections of information whose results will be published after")',
'getSection('+JSON.stringify('12. Burden\nALL\n16. Publication')+')','escapeHtml('+JSON.stringify('<script>"&')+')'])micro.push({expression:expr,result:snapshot(evaluate(expr))});
// Report/event smoke checks use real event bindings/renderers; not a browser certification.
getNode('loadSampleBtn').click(); getNode('runBtn').click();
await evaluate('copyReport()'); assert.equal(clipboard,evaluate('state.lastReportText'));
context.navigator.clipboard.writeText=async()=>{throw new Error('test denial');};
await evaluate('copyReport()'); assert.equal(fallback,evaluate('state.lastReportText'));
getNode('sectionFilter').value='attention'; getNode('sectionFilter').change();
const attentionIncludesInfo=evaluate('filterItems("structure").some(x=>x.severity==="info")');
getNode('clearBtn').click(); assert.equal(evaluate('state.checks.length'),0);
// Fresh direct comparison via installed esbuild, without copying Jay source into this repo.
const require=createRequire(path.join(jayRoot,'app/package.json'));
const esbuild=require('esbuild');
const temp=fs.mkdtempSync(path.join(os.tmpdir(),'pra-review-'));
const bundle=path.join(temp,'jay.mjs');
await esbuild.build({stdin:{contents:`export {reviewDocument} from ${JSON.stringify(path.join(jayRoot,'app/src/lib/review/index.ts'))}; export {govCostRow,govCostTotal} from ${JSON.stringify(path.join(jayRoot,'app/src/lib/calc/govcost.ts'))};`,resolveDir:jayRoot},bundle:true,platform:'node',format:'esm',outfile:bundle,logLevel:'silent'});
const jay=await import(pathToFileURL(bundle));
const comparisons=[];
for(const id of ['sample','aligned-pipes','pipeline-paragraph','pipeline-full','twic-bridge','twic-wrong-total','twic-current-full','headed-sample','generic-hour-pass','generic-hour-fail','pipeline-compliance']){
 const input=cases.find(c=>c.id===id).input;
 const r=jay.reviewDocument(input);
 comparisons.push({id,input,sections:r.doc.sections.map(s=>({questionNo:s.questionNo,tables:s.tables.length,figures:s.figures})),findings:r.findings,passports:r.passports,score:r.score,detectedRoundingMode:r.detectedRoundingMode});
}
const sv=value=>({value,unverified:true,note:'Review fixture'});
const fedRows=[{kind:'labor',name:'manager',annualHours:sv(100*8),hourlyWage:sv(122.27)},{kind:'labor',name:'analyst',annualHours:sv(100*24),hourlyWage:sv(104.17)}].map(x=>jay.govCostRow(x,'roundLast'));
const total=jay.govCostTotal(fedRows,'roundLast'); assert.equal(total.value,347824);
const net=bridge.component_deltas.reduce((a,b)=>a+b,0); assert.equal(net,80154); assert.equal(bridge.baseline+net-bridge.current,0);
const results={environment:{node:process.version,platform:process.platform,locale:Intl.DateTimeFormat().resolvedOptions().locale,benchmark_sha:sha(root),icr_tool_sha:sha(jayRoot),checker_sha256:crypto.createHash('sha256').update(html).digest('hex')},method:'Exact final inline script in Node vm with DOM/clipboard shim; real render/check functions. Jay entry points bundled read-only into disposable /tmp. No browser, host or dependency installation.',cases,micro,uiSmoke:{clipboardSuccess:true,clipboardFallback:true,clear:true,attentionIncludesInfo},jayComparisons:comparisons,independentControls:{pipeline:{grouped:100*(8*122.27+24*104.17),literal:100*(8*122.27)+(24*104.17),published:290825.84,groupedMinusPublished:347824-290825.84,jayRows:fedRows,jayTotal:total,interpretation:'Calculated diagnostic, not an official correction.'},twic:{bridge,net,residual:bridge.baseline+net-bridge.current,interpretation:'Displayed component reconciliation only, not causal decomposition.'}}};
fs.writeFileSync(out,JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify({out,cases:cases.length,micro:micro.length,sample:sampleRun.counts,coherent:coherent.counts,jay:comparisons.map(x=>({id:x.id,sections:x.sections.map(s=>s.questionNo),findings:x.findings.length,math:x.findings.filter(f=>f.ruleId.startsWith('MATH'))}))},null,2));
