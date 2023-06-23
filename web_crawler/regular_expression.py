#正則表示
import re
key='abcde@abc.edu.tw'
p1='@.+.'
pattern1=re.compile(p1)
print(pattern1.findall(key))
p1='@.+\.'
patter1=re.compile(p1)
print(patter1.findall(key))
p1='@.+?\.'
patter1=re.compile(p1)
print(patter1.findall(key))

pattern=re.compile(r'\d+')
ans=pattern.findall('run 123 dassd 456')
ans1=pattern.findall('ffsd890fsd456fdsafsd1323',0,10)#範圍0-10
print(ans,ans1)

#%%
import requests
import re

url=input('請輸入網址(需包含http://):')
htmlfile=requests.get(url)
if htmlfile.status_code==requests.codes.ok:
    pattern=input('請輸入欲搜尋的字串:')
#判斷是否曾有搜尋到
    if pattern in htmlfile.text:
        print('搜尋 %s 成功'%pattern)
    else:
        print('搜尋 %s 失敗'%pattern)
#計算出現次數
    name=re.findall(pattern,htmlfile.text)
    if name!=None:
        print('%s 出現 %d 次'%(pattern,len(name)))
    else:
        print('%s 出現 0 次'%pattern)
else:
    print('網頁下載失敗')
#%%
import requests
import re
from bs4 import BeautifulSoup

res=requests.get('https://bit.ly/3gkZaJa')
soup=BeautifulSoup(res.text,'lxml')
#找出所有h開頭的標題文字
titles=soup.find_all(['h1','h2','h3','h4','h5','h6'])
for title in titles:
    print(title.text.strip())
#利用 regex找出所有h開頭的標題文字
for title in soup.find_all(re.compile('h[1-6]')):
    print(title.text.strip())

#找出所有.png結尾的圖片
imgs=soup.find_all('img')
for img in imgs:
    if 'src' in img.attrs:
        if img['src'].endswith('.png'):
            print(img['src'])

 #利用regex 找出所有.png結尾的圖片
for img in soup.find_all('img',{'src':re.compile('\.png$')}):
    print(img['src'])
    
#%%
#大樂透
import requests
from bs4 import BeautifulSoup
url='http://www.taiwanlottery.com.tw/'
html=requests.get(url)
bs=BeautifulSoup(html.text,'html.parser')

#取出class名稱為contents_box02的串列
#.代表class
data1=bs.select('.contents_box02')
#在第3個區域中抓出黃球
data2=data1[2].find_all('div',{'class':'ball_tx'})
print('大樂透黃球資料')
print(data2)

#大樂透號碼
print('開出順序:',end='')
for n in range(0,6):
    print(data2[n].text,end='')
print('\n大小順序:',end='')
for n in range(6,len(data2)):
    print(data2[n].text,end='')
#特別號
red=data1[2].find('div',{'class':'ball_red'})
print('\n特別號:',red.text)

#%%新聞
import requests as rq
from bs4 import BeautifulSoup as bs

#設定網址
url='http://tw.news.yahoo.com'

#擷取網頁原始資料得到回應物件
res=rq.get(url)
#若回應是200代表有資料，若不是200代表沒截到資料
print(res)
#回應物件內容
print(res.text)
#網頁進行解析
sp=bs(res.text,'lxml')
#取出標籤tag名稱為li,屬性內容為pos(r)資料
data1=sp.find_all('li','Pos(r)')
#編號
x=1

for i in data1:
    con=i.find('a').text
    print(x,con,sep='. ')
    x+=1
#%%
#網路擷取圖片程式
import requests,os,urllib
from bs4 import BeautifulSoup
url='https://www.edu.tw/Default.aspx'
html=requests.get(url)
html.encoding="utf-8"
bs=BeautifulSoup(html.text,'html.parser')
pics_dir="pics"
#建立資料夾
if not os.path.exists(pics_dir):
    os.mkdir(pics_dir) #在工作目錄下建立目錄pics來儲存圖片
all_links=bs.find_all('img') #用串列取得所有<img>標籤的內容
for link in all_links:
    src=link.get('src') #讀取src屬性值的內容
    attrs=[src] #將src字串轉成串列attrs
    for attr in attrs:
        if attr!=None and('.jpg'in attr or'.png'in attr):#讀取.jpg或.png檔
            full_path = attr #設定圖檔完整路徑            
            file_n=full_path.split('/')[-1] #從網址的最右側取得圖檔的名稱
            print('================')
            print('圖檔完整路徑：',full_path)            
            try:  #儲存圖片程式區塊
                image = urllib.request.urlopen(full_path)
                #f意思是建立好的資料夾把檔案寫進去'wb'是用在多媒體寫入
                f = open(os.path.join(pics_dir,file_n),'wb')
                #urllib是用read  request是用.text 內容
                f.write(image.read())
                print('下載成功：%s' %(file_n))
                f.close()
            except: #無法儲存圖片程式區塊
                print("無法下載：%s" %(file_n))
#%%爬蟲常見問題-被封鎖
import time
import requests
url='http://www.majortests.com/word-lists/word-list-0{0}.html'
for i in range(1,10):
    url2=url.format(i)
    r=requests.get(url2)
    print(r.status_code)
    print('等待3秒鐘...')
    time.sleep(3)









