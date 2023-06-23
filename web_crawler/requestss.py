import urllib.request
res=urllib.request.urlopen(r'https://goodinfo.tw/tw/index.asp')
content=res.read()
print(content)

#%%
import requests
url='https://data.gov.tw/'
html_body=requests.get(url)
html_body.encoding='utf8'
print(html_body.text)

#%%
import requests
url='''https://data.ntpc.gov.tw/api/datasets/54A507C4-C038-41B5-BF60-BBECB9D052C6/json'''

res=requests.get(url)
print(res.status_code)

data=res.json()#要上面的網址是json格式才能用，相當於load的功能
print(data)
#%%
import requests
url='https://ssur.cc/mZTbSzU'  
res=requests.get(url)
data=res.json()#短網址也可以，但原檔要json
print(data)



