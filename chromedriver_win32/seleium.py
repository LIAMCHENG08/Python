#匯入套件
from selenium import webdriver
import time
#瀏覽器
driver=webdriver.Chrome('chromedriver')
time.sleep(3)
driver.quit()
#%%
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get('https://example.com/')
print(driver.title)
html=driver.page_source
print(html)
driver.quit()

#%%
from selenium import webdriver
from bs4 import BeautifulSoup as bs
driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get('https://example.com/')
print(driver.title)
#bs裡要是字串,字串要是網頁語法
soup=bs(driver.page_source,'lxml')
f=open('index.html','w',encoding=('utf8'))
#write裡要放字串
f.write(soup.prettify())
print('寫入檔案...')
f.close()
driver.close()
#%%
#新版要寫這個from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get('https://example.com/')
#新版寫法
# data=driver.find_element(By.CLASS_NAME,'content')
h1=driver.find_element(By.TAG_NAME,'p')
print(h1.text)
# print(data.text)
driver.quit()
#%%
#新版要寫這個from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium import webdriver
#模組目錄資料夾
import os

driver=webdriver.Chrome()
html_path=os.path.abspath('SeleniumTest.html')
driver.implicitly_wait(8)
driver.get(html_path)
h3=driver.find_element(By.TAG_NAME,'h3')
print(h3.text)
p=driver.find_element(By.TAG_NAME,'p')
print(p.text)
content=driver.find_element(By.CSS_SELECTOR,'p')
print(content.text)
form=driver.find_element(By.ID,'loginForm')
print(form.text)
#需打全部內容
link1=driver.find_element(By.LINK_TEXT,'Continue')
print(link1.text)
#可以打部分內容
link2=driver.find_element(By.PARTIAL_LINK_TEXT,'Cont')
print(link2.text)
user=driver.find_element(By.NAME,'username')
print(user.tag_name)
print(user.get_attribute('type'))
eles=driver.find_elements(By.NAME,'continue')
for ele in eles:
    print(ele.get_attribute('type'))

driver.close()
#%%
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os

driver=webdriver.Chrome('chromedriver')
html_path=os.path.abspath('SeleniumTest.html')
driver.implicitly_wait(10)
driver.get(html_path)
try:
    content=driver.find_element(By.CSS_SELECTOR,'body > h3')
    print(content.text)
except NoSuchElementException:
    print('選取元素不存在')
driver.quit()
#%%大樂透
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from matplotlib import pyplot as plt
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd

lotto_list=[]
driver=webdriver.Chrome()
driver.get('https://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx')
driver.find_element(By.ID,'Lotto649Control_history_radYM').click()

while True:
    select_year=Select(driver.find_element(By.ID,'Lotto649Control_history_dropYear'))
    year=input('請輸入你要找的樂透年分:')
    print('請稍後')
    select_year.select_by_value(year)
    for i in range(12):
        #找出選擇月份的標籤
        select_month=Select(driver.find_element(By.ID,'Lotto649Control_history_dropMonth'))
        select_month.select_by_value(str(i+1))
        
        #點籍查詢按紐
        driver.find_element(By.ID,'Lotto649Control_history_btnSubmit').click()
        
        #抓取網頁內容
        html=driver.page_source
        soup=bs(html,'lxml')
        #數網頁中有多少個table
        table_count=len(soup.findAll('table',{'class':'td_hm'}))
        #針對每一個table抓取樂透號碼並加入串列
        for i in range(table_count):
            for j in range(1,7):
                temp=soup.find('span',{'id':'Lotto649Control_history_dlQuery_SNo'+str(j)+'_'+str(i)})
                lotto_list.append(int(temp.text))
               
    check=input('還要繼續嗎?繼續請輸入Y')
    if check.upper()!='Y':
        print('已結束')
        break
print(lotto_list)
#%%下載網頁
from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://hahow.in/')
print(driver.title)
soup=bs(driver.page_source,'lxml')
f=open('hahow.html','w',encoding=('utf8'))
f.write(soup.prettify())
print('寫入hahow.html')
f.close()
driver.quit()
#%%hahow
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://hahow.in/courses')


while 1:
    try:
        items=driver.find_elements(By.CSS_SELECTOR,'h4.title')
        if len(items)!=0:
            for item in items:
                print(item.text)
            break
    except:
        continue
driver.quit()
#%%nba
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import pandas as pd
import time
driver = webdriver.Chrome()
driver.get("http://stats.nba.com/players/traditional/?sort=PTS&dir=-1")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler').click() 
# driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/button').click() 
time.sleep(5)
pages_remaining = True
page_num=int(driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[4]').text[-2::])
page_current = 1
while pages_remaining:
# 使用Beautiful Soup剖析HTML網頁
    soup = BeautifulSoup(driver.page_source, "lxml")
    table = soup.select_one("#__next > div.Layout_base__6IeUC.Layout_withSubNav__ByKRF.Layout_justNav__2H4H0 > div.Layout_mainContent__jXliI > div.MaxWidthContainer_mwc__ID5AG > section.Block_block__62M07.nba-stats-content-block > div > div.Crom_base__f0niE > div.Crom_container__C45Ti > table") 
# table = soup.table 
# table= soup.find('table')
    data = pd.read_html(str(table)) # list格式
# print(df[0].to_csv())
    data[0].to_csv("ALL_players_stats" + str(page_current) + ".csv",index=0)
    print("儲存頁面:", page_current)
    try:
# 自動按下一頁按鈕
        next_link = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]')
#print('ok')
        next_link.click()
        time.sleep(5)
        if page_current <page_num:
            page_current = page_current + 1
        else:
            pages_remaining = False
    except:
        pages_remaining = False 
print("已完成，程式結束") 
driver.close()




