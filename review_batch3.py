from pathlib import Path
import json,csv,re,datetime
R=Path(__file__).parent
DIMS=['reproducibility','provenance','segmentation','labor','item13','item14','item15','validation','consistency']
reviews=[]
def case(ref,archetype,complexity,rel,scores,reasons,activities,labor,cost13,federal,changes,assumptions,issues,methods,checks,thoroughness='extensive'):
 m=json.loads((R/'icrs'/ref/'retrieval.json').read_text());sid=m['supporting_statement_source_ids'][0]
 d={'icr_id':ref,'omb_control_number':m['omb_control_number'],'agency':m['agency'],'title':m['title'],'submission_date':m['submission_date'],'archetype':archetype,'complexity':complexity,'tsa_relevance':rel,'review_status':'REVIEWED_PROVISIONAL','review_iteration':3,'rubric_version':'1.0.0','source_ids':[sid,m['record_source_id']],'source_verification_depth':'Complete Supporting Statement A plus package; underlying cited sources not all independently retrieved. Specific corroboration recorded separately.','score':dict(zip(DIMS,scores)),'score_rationale':dict(zip(DIMS,reasons)),'thoroughness':thoroughness,'model':{'activity_columns':['activity','annual_responses','hours_per_response','reported_annual_hours'],'activities':activities,'labor':labor,'item13':cost13,'item14':federal,'item15':changes,'assumptions':assumptions},'reconstruction_issues':issues,'methods_worth_testing':methods,'checks':[]}
 for label,expr,reported,unit,note in checks:
  val=eval(expr,{'__builtins__':{}},{'sum':sum,'round':round});d['checks'].append({'label':label,'formula':expr,'calculated':val,'reported':reported,'difference':val-reported,'unit':unit,'interpretation':note,'source_id':sid})
 d['total_score']=sum(scores);reviews.append(d)

case('202411-2070-003','chemical release reporting andnonreporter determination','high','direct',[18,10,14,8,6,7,6,3,3],
['Counts,constant burdens andratios reconstruct total; FormA formula labelsforms instead ofchemicals.','Specific RBBM2011 reference,2023ECEC andadministrative counts; inheritedconstants need independent revalidation.','Forms,chemicals,facilities andnonreporters distinct; facility distributions expose heterogeneity.','Separate wages,benefits,20%overhead and3/89/8 mix; overhead andweights inherited.','Zero directly attributable capital/O&M asserted; more scope rationale desirable.','Actualheadcounts,GS13/1 andnonFTE categories; gross costs reconstruct,load components notfully exposed.','Consolidated rules and13442notification hours described; no complete driver bridge.','Observed filing distributions; legacyburden calibration remains critical.','Minor rounding,onechemical count discrepancy,forms-versus-chemicals equationlabel error.'],
[['FormR chemicals',78156,35.70516,2790555],['FormA chemicals',9686,21.95867,212681],['Petitions',None,None,925],['Supplier notifications',None,None,103058],['Nonreporter determination',None,None,734976],['Discretionary authority notices',None,None,93]],
{'wages':[53.10,45.60,23.80],'benefits':[24.46,22.86,10.60],'overhead_on_compensation':.20,'mix':[.03,.89,.08],'weighted_loaded':79.23,'reference_period':'December2023','reported_cost':304424425},
{'annual_cost':0,'reason':'No specific directly associated capital/O&M'},
{'fte_by_task':[2,1.5,1.5],'nonfte_by_task':[30000,1115000,1326000],'grade':'GS13/1 WashingtonDC','base_hourly':55.46,'loaded_hourly':109.08,'fte_total_cost':1134419,'annual_cost':3605419,'paper_processing_unit':99.19,'electronic_processing_unit':8.57},
{'form_R_increase':5667,'form_A_increase':2044,'supplier_notification_increase':13442,'consolidated_control':'2070-0216 andmultiple rule ICRs','overlap':'Explicitly acknowledged; full driver allocation incomplete'},
['FormA/FormR burden ratio.615; steady-state unitconstant calibrated to2011method.','25271unique facilities;6134FormAs containing9686chemicals.','Nonformconstant839052 includes compliance assessment by nonreporters.'],
['RBBM displayed equation multiplies FormA forms but numerical calculation requires FormA chemicals.','78156+9686=87842 versus87841total; oneunit rounding/copy issue.','Legacy calibrated factors remain unchanged despite technological andreporting changes; revalidation needed.'],
['Model burden for determining non-applicability, not only respondents who file.','Separate response count from underlying units in multi-chemical forms.','Transparent direct compensation plus overhead andlabor weights; inherited calibration requires provenance chain.'],
 [('Hours','78156*35.70516+9686*21.95867+839052',3842287,'hours','Small rounding difference'),('Loaded mix','(77.56*.03+68.46*.89+34.4*.08)*1.2',79.23,'USD/hour','Rounding'),('Federal total','30000+1115000+1326000+1134419',3605419,'USD','Exact')])

case('202312-2050-001','PCB cleanup anddisposal rule transition','high','direct',[14,10,15,6,7,7,8,3,1],
['Role-hour matrix andold/new burdens explicit; labor products fail forannualreports.','2018wages,2019ECEC,2005RACER defaults identified; age andbase rates require validation.','Facilitytype,activity andthree laborroles; overlap ledger linked to2070-0112.','Overhead1.336 components includingprofit disclosed withlimitations; final rates notfully derived.','Mailing3.96*442 clear; existing ICR unitprice source andcapitalzero rationale.','Grade/role hours andgross/net impacts; tableheader respondent rates conflict withgovernment rates.','8276gross versus8266baseline=10net explicitlytable; Item15new/nochange wording misleading.','Economic assessment andcandid overhead uncertainty;timeassumptions notempirically tested.','Manager38h*102.26+clerical2h*38.27 doesnot reproduce6136; copying andminute conversion problems.'],
[['Read rule',1085,1.16,1259],['Postcleanup notice',430,4.1,1763],['Cleanup records',430,.1,43],['Waiver',12,8.1,97],['Waiver records',12,.1,1],['Annualreports',124,40,4960],['Activitynotice',100,1.53,153]],
{'roles':['legal','manager','technical','clerical'],'loaded_rates':[118.63,102.26,48.73,38.27],'wage_year':2018,'overhead_factor':1.336,'overhead_components':{'general_admin':.02,'fixed':.166,'insurance':.05,'profit':.10},'reported_labor_cost':977438},
{'capital':0,'mail_unit':3.96,'notifications':430,'waivers':12,'annual_cost_precise':1750.32,'summary_cost':1751},
{'roles':['GS13/5','GS11/5','GS6/5'],'loaded_rates':[83.82,58.82,35.75],'wage_year':2018,'hours_by_task':[473,73.2,186],'gross_cost':46998,'gross_hours':732,'baseline_hours':240,'net_hours':492},
{'new_gross_hours':8276,'prior_affected_hours':8266,'net_change_hours':10,'baseline_control':'2070-0112','drivers':[1259,1763,43,-703,1,-2356,3]},
['Annualreport59to40hours;waiver old800new97;reading rule charge1085facilities.','RACER overhead assumednonoverlapping butmaynotvarywithlabor; limitation explicitlydiscussed.'],
['Annualreport rolehours andrates imply3962.42 perresponse, not6136; tablecost760876 notexplained.','Federal tableheaders repeatrespondentrates; sourceparagraph givesdifferent federalrates.','Emailfield saidone minute but1.50to1.53hours adds1.8minutes.','Item15 nochange language masks10hour netincrease inaffectedexistingICR.'],
['Explicit gross-to-net cross-ICR transition table; allocate displaced obligations.','Document overhead components andlimitations rather than treatingallload factors as equivalent.'],
 [('Net burden','8276-8266',10,'hours','Exact'),('Mail costs','442*3.96',1750.32,'USD','Exact'),('Annualreport unitlabor','38*102.26+2*38.27',6136,'USD','Material rate/product mismatch'),('Federal gross/net','473+73.2+186-240',492,'hours','Rounded')])

case('202405-1218-005','portable fire extinguisher inspection records','high','direct',[17,11,14,8,8,5,9,4,2],
['Building-area exposure model andoutsourcing partitions clear; prose describes multiplication where division required.','EIA CBECS/MECS vintages,SOC/ECEC andindustry consultations identified; currentlinksnotarchives.','Manufacturing/nonmanufacturing,customary85%,outsourced90%,inhouse10% meaningful.','30.76/(1-.294)=43.57; occupation transparent, no separateoverhead.','Price range42–59,midpoint50.5 andoutsourcedquantity explicit; survey age unclear.','Zero federalcost asserted; tagvisiblewithoutemployerdisclosure supports limitedincrementalburden.','Oldnew hours,extinguisherstock,price andsurveyvintage table clear; effectsnotfullydecomposed.','Industryconsultations andeconomist verification ofsurveyvintage jump; datedcalibration of85/90%missing.','Item13 prose calls9567848contracted butcalculationuses8611063; tablecallsassetsrespondents.'],
[['Inhouse annual inspection',956785,.5,478393]],
{'soc':'49-9069','oews_year':2022,'wage':30.76,'ecec_period':'September2023','benefit_share':.294,'loaded':43.57,'cost':20843583},
{'stock':63785650,'noncustomary_share':.15,'contract_share':.90,'outsourced_count':8611063,'price_range':[42,59],'mean_price':50.50,'annual_cost':434858682},
{'annual_cost':0,'reason':'No cost asserted;record tagreadilyvisible'},
{'old_stock':39132742,'new_stock':63785650,'old_hours':293496,'new_hours':478393,'delta_hours':184897,'old_unitinspectioncost':17.28,'new_unitcost':50.50,'classification':'adjustment','source_vintage_change':'CBECS2012→2018;MECS2010→2018'},
['Oneextinguisher/11250sqft;industryengineer85%usual/customary;servicecompany90%outsourced.','Appendix buildingsegmenttables preserve EIA exposureinputs.'],
['Item13 prose contractedcount differsfromformula.','Respondents labeled956785 althoughnumberrepresents extinguishers, notdistinctemployers.','Prose saysmultiply squarefeetby11250, dimensionally divisionisrequired.'],
['Explicit make-or-buy partition withoutcharging outsourcedlaboragain inItem12.','Renewal source-vintage comparison distinguishes observed growth from survey redesign/rebasing.'],
 [('Inhouse stock','63785650*.15*.10',956785,'extinguishers','Rounding'),('Outsourcedcost','8611063*50.5',434858682,'USD','Rounding'),('Loaded wage','30.76/(1-.294)',43.57,'USD/hour','Rounding'),('Hourbridge','478393-293496',184897,'hours','Exact')])

case('202504-1902-007','utility central-service financial reporting','medium','direct',[18,8,13,5,6,7,8,2,2],
['Threeforms withpopulationfrequencyhours; total57973doesnot matchrows57973? rows57973exact.','Actualfilerbasis,2024FERCsalary andBLSclerk source; BLSvintage/load notderived.','Reporter versusrepresentedcompany correction useful; recordkeeping distinct.','Federalaveragepayproxy justified generically;39.53fileclerkrate withbenefitsnotderived.','1GB*10*51=510 transparent; marketpriceexamples mismatchunitpriceconservatism unexplained.','FTEsalary plusPRAadmin allowance;8369basisnotbottomup andtwofiledcollectionsfor3ICs unexplained.','Detailedoldnewrows andcountmethodchange; costrow calledROCIScost butcontainslabor.','Observedfilers supportcounts; no1080hourrecordkeeping validation.','Item15 laborcost mislabeledROCISannualcost; newhoursrowssum57973 but componentreported earlier55080+2886+7=57973.'],
[['Form60',37,78,2886],['Form61',14,.5,7],['555Arecords',51,1080,55080]],
{'reporting_rate':100,'basis':'FERC2024average salaryplusbenefits207786/year','records_rate':39.53,'records_soc':'43-4071','reported_labor_cost':2466612},
{'capital':0,'storage_GB_peryear':1,'storage_cost_each':10,'respondents':51,'annual_cost':510,'paperstorage':'removed'},
{'FTE':[.5,.1,0],'annual_salary_benefits':207786,'PRAadmin_percollection':8396,'admin_count':2,'annual_cost':141464},
{'old_hours':[3276,40,131760],'new_hours':[2886,7,55080],'old_responses':[42,80,122],'new_responses':[37,14,51],'classification':'adjustment','retired_onetime':'described butnotseparatelyquantified'},
['Form61 actualfilersreplace representedcompanies;averageburden supposedtocapture complexity.','100%electronicstorage; decliningmarketprices anticipated.'],
['Item15 labels laborcost asROCISannualcost, obscuring510nonlaborcost.','Total laborcost2466612 differsfromdisplayedcomponents288600+700+2177312=2466612? exact; noarithmeticissuehere.','PRAadmincount2versus3ICs needs collectionunitclarification, notassumederror.'],
['Quantified denominator correction: filer versusrepresentedcorporategroup.','Explicit PRAadministration asfederalcostcategory.'],
 [('Hours','2886+7+55080',57973,'hours','Exact'),('Federalcost','.6*207786+2*8396',141464,'USD','Rounding'),('Storage','51*10',510,'USD','Exact'),('Change','(37-42)*78+(14-80)*.5+(51-122)*1080',-77103,'hours','Exact')], 'moderate')

case('202401-1615-055','immigration residence petition withbiometrics','medium','adjacent',[19,6,13,4,7,5,9,2,4],
['Two clearrows andbiometric multiple-person explanation.','2018BLSalloccupations and1.46multiplier withoutsource; currentfee rule identified.','Petition andbiometricpeople separated; range ofpurchasedassistance.','Alloccupations choice explained butstaleuniversalrate andbenefitsunsupported.','25%*515*153000 explicit; range20–1000doesnotitselfjustify515mean.','Fee-based activitycostproxy; acknowledges cross-subsidy forfreebenefits undermines collection-specific equivalence.','Oldnewtable preciselyexplains27999hours removedwithfeecontent.','No empirical supportfor25%or515; timingasserted.','Hourandcostproducts reconcile to rounding.'],
[['Petition',153000,4.387,671211],['Biometrics',306000,1.17,358020]],
{'wage':24.98,'oews_year':2018,'factor':1.46,'loaded_rate':36.47,'all_occupations':True,'cost':37536054},
{'assistance_share':.25,'assistance_average':515,'range':[20,1000],'population':153000,'annual_cost':19698750,'filing_fee_informational':750},
{'method':'fee-based proxy foractivity-based costing includingunassignedoverhead andfreebenefits','count':153000,'fee':750,'cost':114750000},
{'prior_hours':1057230,'proposed_hours':1029231,'program_delta':-27999,'petition_old':699210,'petition_new':671211,'biometrics_unchanged':358020},
['Two biometricpersons perpetition average;assistance25%at515USD.'],
['Fee proxy includesfreebenefit cross-subsidy; doesnotisolategross costofthiscollection.','515average notmidpoint of20–1000range andno empiricaldistribution supplied.'],
['Concise itemizedprior/newhours table; preservefees andresourcecosts asdistinct concepts.'],
 [('Hours','153000*4.387+306000*1.17',1029231,'hours','Exact'),('Purchasedservices','153000*.25*515',19698750,'USD','Exact'),('Federalproxy','153000*750',114750000,'USD','Exact proxy,notvalidationofcostscope'),('Change','671211-699210',-27999,'hours','Exact')], 'moderate')

case('202506-2130-004','rail dutyrecords andfatiguemodeling','high','direct',[13,9,14,5,6,7,9,3,1],
['ManyCFRtaskrows; minutes convertedusingtruncateddecimals,employeeproduct inconsistent.','2024OPM andrailwaywagesource footnote; agencyexperience basisnotreplicable.','Electronic/paper andfatiguereview activities;explicitfulfilled/excludedobligations.','Uniform89.13industryrate; occupation-specificmix lacking.','Softwareprogramming/training/support/maintenance inflationtable;one-timeversusannualcycle notclear.','Grade/time/quantity explicit; firstrowunloadedwhileothers1.75; headingsaysx75%instead ofmarkup.','Row-levelold/newdriverreasons andaggregate1325hourchange.','Administrative histories andFASTmodel operational context; response-timeevidence mostlySME.','8minutesrowcalculatedas.13hours; training2/60computedas.03;1/60as.02.'],
[['Electronicdutyrecord',17448669,3/60,872433.45],['Paperdutyrecord',918351,8/60,119385.63],['Dispatchrecord',285000,1,285000],['Excessservice',2317,1,2317],['Initialtrainingrecord',250,2/60,7.5],['Audits',797,2,1594],['Scheduleanalysis',3,2,6],['Fatigueplans',3,20,60],['Corrections',1,1,1],['Followup',1,1,1],['Consultation',20,40,800],['Trainingprogram',36,2,72],['Trainingrecords',5539,1/60,110.78],['Exclusionrequest',1,1,1]],
{'hourly_rate':89.13,'reported_cost':114517098,'source':'Railroad wage source perfootnotes; benefitsincluded'},
{'base_components':[75000,50000,7500,15000,100000],'inflation':.0336,'annual_cost':255816},
{'grade_rates':{'GS14/5':75.70,'GS12/5':53.87},'markup':.75,'first_task_salary':157982.40,'first_task_employees':2,'first_task_share':.25,'other_costs':[12066.88,4239.20,9050.16,1589.70],'total':105937.14},
{'old_hours':1283507,'new_hours':1284832,'delta':1325,'old_responses':18660400,'new_responses':18660988,'classification':'adjustment','driver_table':'Item15CFRrows'},
['85712employees*210days statedtoyield18367020;95%electronic5%paper.','Forecastfromrailindustry andSMEhistory; somefatiguetasksFASTmodel based.'],
['85712*210=17999520, not18367020.','918351*8/60=122446.8, not119385.63; prematuretime rounding.','Initialandfatiguetrainingrecords similarly truncate/round minuteconversion beforemultiplication.','EarlierItem3 says80%electronic vsItem12 95%; datesnotexplained.'],
['CFR-level Item15 bridge with observedadministrative reasons; explicitzeroanticipatedevents.','Preserve exactminute fractions untiloutputrounding.'],
 [('Paperhours','918351*8/60',119385.63,'hours','Materialprematurerounding'),('Populationrecords','85712*210',18367020,'records','Materialdiscrepancy'),('Softwarecost','247500*1.0336',255816,'USD','Exact'),('Federalcost','2*157982.4*.25+12066.88+4239.2+9050.16+1589.7',105937.14,'USD','Exact')])

case('202508-2126-007','driver electroniclogging records','high','direct',[13,10,13,4,6,6,6,3,0],
['Forecastanddailyrecord tables; weightingdenominator wrong andcarrierrounding producesconflictingtotals.','MCMISdatedquery,BLSprojections,OEWS/ECEC andvendorprices; allunderlyingquotesnotyetverified.','Driver/carrier,new/existing,exemptDOL andequipment/service split.','FourSOCweights exceed100%;nestedpassengercategories anddenominator concerns;ECECbenefits mislabeledoverhead.','Vendorprice ranges andmedian,installation,andmonthlyservice;replacement omittedandannualtotalincorrect.','Noincremental federalcost justified asnormalduties; inspectionallocationquestion.','Old/newinputs andcosts shown butseveraldeltas arithmeticallywrong.','MCMISobservations andinvestigator50%reviewbasis; malfunctionrates explicitlyunknown.','53.40v53.44mhours,1.6206bv1.63553bcost,over100%wageweights.'],
[['DriverRODS',4450000*240,2/60,35600000],['Carrierreview',4450000*240*.5,2/60,17800000]],
{'occupation_counts':[2044400,1003960,594230,184990],'denominator_reported':3490010,'median_wages':[26.12,20.42,18.52,28.93],'weighted_wage':25.85,'factor':1.419,'driver_loaded':36.68,'clerk_loaded':32.37,'reported_labor_cost':1882000000},
{'established_driver_count':4450000,'new_driver_count':20000,'ELD_price':350,'install_price':150,'monthly_service':30,'logbook_price':5.24,'logbook_annual':23530000,'ELD_annual':1612000000,'reported_total':1620600000,'replacement_life':None},
{'annual_cost':0,'reason':'No data submission; reviewwithinexistingpositionduties; vendorICR2126-0062 separate'},
{'old_hours':50370000,'new_hours':53400000,'old_driver_rate':29.78,'new_driver_rate':36.68,'old_carrier_rate':30.20,'new_carrier_rate':32.37,'carrier_old_cost':507060000,'carrier_new_cost':576190000,'carrier_claimed_increase':374930000},
['MCMISJan2,2025;4.45mdriversannualmean;240days;2minentry;50%review.','Employmentprojectionannualgrowth.576%; tableformula incorrectlyA/D ratherthanB/A.','NoELDmalfunctionfrequencydata;onebackupbook/year plus2fornewdriver.'],
['Occupationcounts3827580 vsdenominator3490010;laborweights sum109.68%.','Table9header31monthly butvaluesuse30.','23530000+1612000000=1635530000, notreported1620600000.','Carrierhours17.84mtable versus17.80msummary; prematurepopulationrounding.','Carrier costchange69130000, not374930000.'],
['Vendorprice survey andnew-purchasecohorts distinctfromstockservicecost; addreplacementcohorts.','Cross-agency timecardburdenexclusion andexplicitunknownmalfunction burden.'],
 [('Weightdenominator','2044400+1003960+594230+184990',3490010,'drivers','Materialdiscrepancy'),('Nonlabor total','23530000+1612000000',1620600000,'USD','Materialadditionerror'),('Carrierchange','576190000-507060000',374930000,'USD','Materialsubtractionerror'),('Exactcarrierhours','4450000*240*.5*2/60',17800000,'hours','Summaryreconstructs;Table417.84mdoesnot')])

case('202505-3060-038','satellite licensing andengineering filings','high','direct',[18,8,14,3,8,6,8,3,1],
['15filingcategories andAppendixfeequantitytable; totalhoursreconstructible fromdetailedrows.','FeesandGSgrades precise;60inhousewage unsourced;smallfirmoutsideratesurvey datedetailsabsent.','License/applicationtypeandengineer/legal split; taskhoursmeaningful.','60inhouse flat salarywithoutbenefits; outsideprofessionalfeeweights separatecorrectly.','899outsidefilings*9.3hours*275 andfees; rounds8360.7to8361beforecost.','Ninefederalstaffrows exposegrade*staff*time;sumdoesnotmatchprosetotal, andunweightedhourstotalmisleading.','4responses128hoursnewrulechange explicitandnoItem13effect.','Agencyfilingexperience andsmallDCfirmpriceconsultation; no timingmeasurement.','Federal narrative2818723.53 versus2881331.03table; GS12analystrow1508*55.07 mismatch.'],
[['Allfilingcategories',3591,None,27747.5],['NewNGSOcompatibility',4,32,128]],
{'inhouse_rate':60,'reported_cost':1664880},
{'outside_filings':899,'outside_hours':9.3,'legal_rate':300,'engineering_rate':250,'legal_share':.5,'engineering_share':.5,'reported_outside_cost':2299275,'fees':1854991.82,'total':4154267},
{'staff':[6,3,1,1,11,3,1,1,2],'hours_each':[1514,1517,1517,1517,694,2122,500,1508,2011],'rates':[91.02,77.38,65.48,55.07,91.02,77.38,55.07,55.07,55.07],'table_total':2881331.03,'prose_total':2818723.53,'benefits':'notidentified'},
{'new_respondents':4,'new_responses':4,'program_hours':128,'nonlabor_change':0},
['LocalDCfirmrate survey;899filings useoutsideprofessionalassistance9.3hoursaverage.','Detailedlicense-typeAppendixAfeecalculation preservedinrawtables.'],
['Federalprose/table totalsconflict.','1508*55.07=83045.56 ratherthan83000.32analystrow.','Federal total12780hours isunweighted sumofhoursperemployee, not29employeesworkload.'],
['Keep outsideprofessionalhours as purchased-servicequantity, separatefrominhouseburden.','Fee-by-filingtype schedule supports auditableItem13.'],
 [('Outsideservice','899*9.3*275',2299275,'USD','82.5roundingdifferencefromearlyrounding'),('Totalnonlabor','1854991.82+2299275',4154267,'USD','Rounding'),('Federalanalyst','1508*55.07',83000.32,'USD','45.24discrepancy')])

case('202503-3060-020','incarcerated people communications disclosures','high','direct',[19,8,14,4,8,5,10,4,4],
['Eighttask equations reconstruct15175hours and1045739labor;uniqueversusmultipleobligations explicit.','GSproxy and125professionalrate disclosed, weaksourceforlatter; rule/consultationrecord extensive.','Newandexisting obligations,waivers,pricingplans andprovider types distinguished.','GS13/5proxy65.48 and125officerrate; benefitandtaskmixvalidationlimited.','Zero additionalcapital explicitly defendedagainstpubliccomment; supportforsoftwareimplementationboundarystilllimited.','ExistingECFS noadditionalprocessingresources asserted; substantiveanalysiscostnotquantified.','6690+5900+1760+825=15175; public-noticebaseline17555 reduced2380 withspecificdrivers.','Substantiveindustrychallengeandresponse; reduceswaiver240to100anddisability80to40, butnotmeasuredtiming.','Totalsandbridgesexact; assumptionqualityseparatefromarithmetic.'],
[['Disabilityaccess',35,40,1400],['Inactiveaccounts',35,100,3500],['Alternatepricing',5,200,1000],['Consumerdisclosure',35,80,2800],['Waivers',7,100,700],['Existingdisability',35,40,1400],['Annualreports',35,120,4200],['Officer certification',35,5,175]],
{'technical_proxy':'GS13/5','technical_rate':65.48,'professional_officer_rate':125,'labor_total':1045739},
{'capital':0,'om':0,'rationale':'Noadditionalcapitalbeyondnormalbusiness; response toViaPathcomments inItem8'},
{'annual_cost':0,'rationale':'ExistingECFS process/publicationcapacity;incrementalresourcesnotexpected'},
{'old_hours':6690,'new_rules':5900,'revised_rules':1760,'expanded_population':825,'new_hours':15175,'old_respondents':30,'new_respondents':35,'old_responses':33,'new_responses':47,'notice_hours':17555,'notice_reduction':2380,'classification':'programchange;noadjustment'},
['Waivertimes240to100hours afterprocedurenarrowing;disability80to40 forconsistencywithrelatedobligation.','Industrycommentschallengeimplementationcostandrequirementburden;agencyaddressesarguments.'],
['125professionalwageunsourced andGSproxyunloaded; precisiondoesnotestablish empiricalburdenvalidity.','Noadditionalcapital claim rests onscopeargument ratherthanprice/investmentdata.'],
['Two explicitlynamedbaselines: priorapproved and60-daynotice; driver-linkedrevisionhistory.','Publicchallenge/response can improveassumptions while retainingunresolveddisagreement.'],
 [('Hours','1400+3500+1000+2800+700+1400+4200+175',15175,'hours','Exact'),('Hourbridge','6690+5900+1760+825',15175,'hours','Exact'),('Noticebridge','7*(240-100)+35*(80-40)',2380,'hours','Exact'),('Labor','14300*65.48+875*125',1045739,'USD','Exact')])

for d in reviews:
 p=R/'icrs'/d['icr_id'];(p/'extraction.json').write_text(json.dumps(d,indent=2,ensure_ascii=False))
 md=[f"# {d['title']}",f"Provisional review. {d['icr_id']}; sources {', '.join(d['source_ids'])}.",f"Score {d['total_score']}/100. Public documentation only. {d['thoroughness']} statement; {d['complexity']} complexity.",'## Scoring']
 md += [f"- {k}: {d['score'][k]}. {d['score_rationale'][k]}" for k in DIMS]
 md += ['## Reconstruction issues']+['- '+x for x in d['reconstruction_issues']]+['## Methods worth testing']+['- '+x for x in d['methods_worth_testing']]
 (p/'review.md').write_text('\n\n'.join(md)+'\n')
print([(x['icr_id'],x['total_score']) for x in reviews])
