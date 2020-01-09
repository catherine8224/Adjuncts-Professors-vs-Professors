import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import time
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import random

ua = ['Mozilla/5.0',
      'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
      'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
   ]

url = 'https://www.seethroughny.net/tools/required/reports/payroll?action=get'

headers = {
      'Accept' : 'application/json, text/javascript, */*; q=0.01' ,
      'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent' : 'Mozilla/5.0',
    'Referer' : 'https://www.seethroughny.net/payrolls/122685'
}

data = {
    'PayYear[]' : '2017',
    #'BranchName[]' : 'Villages',
    'PositionName[]' : 'Adjunct Professor',
    'SortBy' : 'YTDPay DESC',
    'current_page' : '0',
    'result_id' : '122685646',
    'url' : '/tools/required/reports/payroll?action=get',
    'nav_request' : '0'  
}

results = []
results2= []
i = 0
with requests.Session() as s:
    retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[500,502,503,504])

    s.mount('https://', HTTPAdapter(max_retries=retries))

    while len(results) < 1338:
        #print(len(results))
        data['current_page'] = i
        data['result_id'] = str(int(data['result_id']) + i)
        try:
            r = s.post(url, headers = headers, data = data).json()
        except Exception:
            time.sleep(3)
            headers['User-Agent'] =  random.choice(ua)
            r = s.post(url, headers = headers, data = data).json()
            continue

        soup = bs(r['html'], 'lxml')

        for item in soup.select('tr:nth-child(odd)'):
            row = [subItem.text for subItem in item.select('td')][1:]
            results.append(row)
        for item in soup.select('tr:nth-child(even)'):
            row2 = [subItem.text for subItem in item.select('div', _class="row")][2::3]
            results2.append(row2)
        i+=1
    
df1 = pd.DataFrame(results, columns=['Name', 'Agency', 'Total Pay', 'School'])

df2 = pd.DataFrame(results2, columns=['School1', 'Title', 'Rate of Pay', 'Pay Year', 'Pay Basis', 'Branch/Major Category'])
#df = pd.merge(df1, df2, on='School', sort=False)
#df1.set_index('School').join(df2.set_index('School'))
df = pd.concat([df1, df2], axis = 1)
df = df.sort_values(by = ['School'])
df.to_csv(r'/Users/catherineng/Desktop/Python Projects/editors2017A.csv', sep=',', encoding='utf-8-sig', index=False)
