import requests as rq
import csv
import pandas as pd
url='https://bit.ly/3MUQPQx'
#變成response物件
r=rq.request('GET',url)
#轉成串列
data=list(csv.reader(r.text.split()))
#轉成串列法二
x=r.text.split()
y=csv.reader(x)
data2=list(y)

df=pd.DataFrame(data[1:],columns=['電話號碼','名稱','廳數','地址'])

df.index+=1
print(df)

#%%
import requests as rq

url='https://tinyurl.com/287rnmwr'

html_content=rq.get(url)
json_content=html_content.json()

for item_detail in json_content:
    print_info='站點'+item_detail['sna']+' '+'地址'+item_detail['ar']\
        +' '+'總停車格'+item_detail['tot']+' '+'場站目前車輛數量'+\
            item_detail['sbi']+' '+'空位數量'+item_detail['bemp']+' '+\
                '資料更新時間'+item_detail['mday']
    
    print(print_info)
    #%%
import requests
import json
import math
from collections import Counter
# http://www.omdbapi.com/?i=tt3896198&apikey=7d2cb24b
OMDB_URL = 'http://www.omdbapi.com/?&apikey=7d2cb24b'

def get_data(url):
    #data = json.loads(requests.get(url).text)#loads要用在字串
    data = requests.get(url).json()
    if data['Response'] == 'True':
        return data
    else:
        return None

def search_ids_by_keyword(keywords):
    movie_ids = list()
    query = '+'.join(keyword.split())  # e.g., "Iron Man" -> Iron+Man
    url = OMDB_URL + '&s=' + query
    data = get_data(url)

    if data:
        # 取得第一頁電影 id
        for item in data['Search']:
            movie_ids.append(item['imdbID'])
        # 取得搜尋結果總數
        total = int(data['totalResults'])
        num_pages = math.ceil(total/10)

        # 取得第二頁以後的資料
        for i in range(2, num_pages+1):
            url = OMDB_URL + '&s=' + query + '&page=' + str(i)
            data = get_data(url)
            if data:
                for item in data['Search']:
                    movie_ids.append(item['imdbID'])
    return movie_ids


def search_by_id(movie_id):
    url = OMDB_URL + '&i=' + movie_id
    data = get_data(url)
    return data if data else None

keyword =  'iron man'
m_ids = search_ids_by_keyword(keyword)
print('關鍵字 %s 共有 %d 部影片' % (keyword, len(m_ids)))
print('取得影片資料中...')
movies = list()
for m_id in m_ids:
    movies.append(search_by_id(m_id))
print('影片資料範例 first20:')
for m in movies[:20]:
    print('Title:',m['Title'],'Year:',m['Year'],'imdbID:',m['imdbID'])

years = [m['Year'] for m in movies]
# collections.Counter() 會統計一個 list 中各項目出現的次數, 並回傳一個 dict
year_dist = Counter(years)
print('發行年份分布:', year_dist)
# 如果該電影的 'imdbRating' 欄位不是 'N/A' 則轉換其值為 float 並放入 ratings 內
ratings = [float(m['imdbRating']) for m in movies if m['imdbRating'] != 'N/A']
print('平均評分:', sum(ratings)/len(ratings))


