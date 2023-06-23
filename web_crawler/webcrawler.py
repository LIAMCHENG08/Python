import requests

url='https://www.momoshop.com.tw/search'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/112.0.0.0 Safari/537.36'}
r=requests.get(url+'searchShop.jsp?keyword=HTC',headers=headers)
if r.status_code==200:
    r.encoding='big5'
    print(r.text)
else:
    print('HTTP請求錯誤...'+url)

#%%
import requests
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/Gossiping/index.html'

r=requests.get(url,cookies={'over18':'1'})
if r.status_code==200:
    r.encoding='utf8'
    soup=BeautifulSoup(r.text,'lxml')
    tag_divs=soup.find_all('div','r-ent')
    for tag in tag_divs:
        if tag.find('a'):
            tag_a=tag.find('a')
            print(tag_a['href'])
            print(tag_a.text)
            print(tag.find('div',class_='author').string)
            
else:
    print('HTTP請求錯誤...'+url)
            
#%%
import requests
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/NBA/index.html'
deleted=BeautifulSoup("<a href='deleted'>本文已刪除</a>",'lxml' ).a
r=requests.get(url)
if r.status_code==200:
    soup=BeautifulSoup(r.text,'lxml')
    tag_divs=soup.find_all('div','r-ent')
    for tag in tag_divs:
        tag_a=tag.find('a') or deleted 
        print(tag_a['href'])
        print(tag_a.text)
        print(tag.find('div',class_='author').string)
else:
    print('HTTP請求錯誤...'+url)    
    
#%%
import requests
from bs4 import BeautifulSoup as bs
import random
#https://free-proxy-list.net/ 從這個網頁取得也可以從其他的免費代理伺服器
            #ip address:port
proxy_ips=['169.55.89.6:80','146.19.233.162:3128','45.136.58.51:8888']
ip=random.choice(proxy_ips)
print('use',ip)
res=requests.get('http://ip.filefab.com/index.php',
                 proxies={'http':'http://'+ip})
soup=bs(res.text,'lxml')
print(soup.find('h1',id='ipd').text.strip())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            