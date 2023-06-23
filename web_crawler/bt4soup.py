from bs4 import BeautifulSoup as bs

data='''
<html><head><title>The Dormouse's \
    story</title></head> <body>\
        <p class="title"><b>The Dormouse's story</b></p>\
            <p class="story">Once upon a time there were three little sisters; \
                and their names were <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,\
                    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and\
                        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p> \
                        <p class="story">...</p>

'''
bsdata=bs(data,'lxml')
print(bsdata)#解析器，不是字串
print(bsdata.prettify())#變樹狀
print(bsdata.b)#後面的.b是title,可以直接抓到值
print(bsdata.p.string)#string是抓內容，用.text也可以,#如果有很多title,也只會抓第一個
print(bsdata.find('p').text)
print(bsdata.find('b'))#title要用字串，若是屬性
print(bsdata.find('b').text)
print(bsdata.find(href="http://example.com/lacie"))#若是屬性的話，屬性不是字串
print(bsdata.find(class_="sister"))#若遇到class，記得加底線(經驗)
print(bsdata.find_all('p'))#找出所有p標籤的值，標籤要變字串
for i in bsdata.find_all('a'):
    print(i.get('href'))#get是用在要找屬性的值，get裡面要變字串
for j in bsdata.findAll('p'):
    print(j.get('class'))#不用加底線
#%%
from bs4 import BeautifulSoup as bs

data='''

<html><head><title>國立臺灣大學系統</title></head>
<body>
<p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
<p class="ntu_system">
<a href="http://www.ntu.edu.tw" class="union" id="link1">臺灣大學</a>
<a href="http://www.ntnu.edu.tw" class="union" id="link2">臺灣師範大學</a>
<a href="http://www.ntust.edu.tw" class="union" id="link3">臺灣科技大學</a>
</p></body></html>

'''
bsdata=bs(data,'lxml')
print('1:',bsdata.title)
print('2:',bsdata.find('a'))
print('4:',bsdata.findAll('a',{'class':'union'}))#進階篩選，印出a標籤且class為union
print('5',bsdata.find('a',{'id':'link2'}))#網頁id基本唯一性，所以用find
print(bsdata.find('a',id='link1'))#也有這種寫法
print(bsdata.find('a','union'))#逗號後面預設為class,如果沒寫的話
print('6:',bsdata.find('a',{'href':"http://www.ntnu.edu.tw"}))#只找出第一個

web=bsdata.find('a',{'id':'link1'})
print('7:',web.get('href'))#使用get找出網址

selectdata=bsdata.select('.union')#'.'代表class,抓全部,從屬性的結果去回推
print('8:',selectdata[0].text)#有索引的概念
print('9:',selectdata[1].text)
print('10:',bsdata.select('#link3'))#  '#'代表id


