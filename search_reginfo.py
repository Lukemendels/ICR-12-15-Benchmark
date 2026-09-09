"""Read-only search using the published Reginfo PRA search form fields."""
import sys,re,json,urllib.parse,concurrent.futures
from pathlib import Path
from retrieve import get,clean
def search(term):
 params={'operation':'2','requestTypeCategory':'ICR','dateType':'RE','startDate':'09/09/2023','endDate':'09/09/2026'}
 params['ombControlNumber' if re.fullmatch(r'\d{4}-\d{4}',term) else 'terms']=term
 url='https://www.reginfo.gov/public/do/PRASearch?'+urllib.parse.urlencode(params)
 try:
  html=get(url).decode();rows=[]
  for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>',html,re.S):
   refs=re.findall(r'PRAViewICR\?ref_nbr=([0-9-]+)',row)
   if refs:rows.append({'refs':sorted(set(refs)),'text':clean(row)})
  result={'query':term,'url':url,'rows':rows,'all_refs':sorted(set(re.findall(r'PRAViewICR\?ref_nbr=([0-9-]+)',html)))}
  p=Path(__file__).parent/'logs/discovery';p.mkdir(exist_ok=True);(p/(re.sub(r'[^a-zA-Z0-9-]','_',term)+'.json')).write_text(json.dumps(result,indent=2));return result
 except Exception as e:return {'query':term,'error':str(e)}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
  for r in ex.map(search,sys.argv[1:]):print(json.dumps(r),flush=True)
