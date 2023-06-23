import pandas as pd
ss= pd.Series([1,-3,5,-7])
print(ss)
print(ss.values)#值
print(ss.index)#索引

ss1=pd.Series([4,7,-5,3], index=['a','b','c','d'])#索引可以自己設定
print(ss1.index)
print(ss1['a'])#索引a內容，像dict
print('a' in ss1)
print(7 in ss1)#像dict比對key不比值
print(7 in ss1.values)#要加values才能比
#%%
import pandas as pd
#list轉series
list1=['a',123,'b',4.56,'c',True]
list_to_series=pd.Series(list1)
print(list_to_series)

print(type(list_to_series[0]))#型態都保留一樣，像json
print(type(list_to_series[3]))
print(type(list_to_series[5]))

#dict轉series
dic1= {'a':123,'b':4.56,'c':True}

dic_to_series=pd.Series(dic1)
print(dic_to_series)

print(type(dic_to_series['a']))#型態也都保留一樣
print(type(dic_to_series['b']))
print(type(dic_to_series['c']))
#%%
#二維
import pandas as pd
data={'name':['Bob','Nancy'],'year':[1996,1997],'month':[8,1],'day':[11,8]}
df=pd.DataFrame(data)#轉二維
print(df)

#可以自己排序columns跟改索引
df1=pd.DataFrame(data,columns=['name','day','month','year','abc'],index=['a','b'])
print(df1)
#%%
import pandas as pd
x=[['Amy','f',80],['leo','m',65],['rita','f',50],['eva','f',75]]
df1=pd.DataFrame(x,columns=['name','gender','grade'])
print(df1)
print(df1['name'])#欄標題
print(df1['name'].values)#欄標題的值

print(df1['name'][1])#先df1[columns][row]  過往所學都是y[row][columns]
# print(df1['name'][1].values)上一個就是值，所以無法執行
#%%
#讀資料
import pandas as pd
df=pd.read_csv('csvsample.csv')
print(df.head())#預設前5筆
print(df.tail())#預設後5筆
print(df.info())#詳細資料
print(df['sna'][2])#先column再row
#%%
import pandas as pd
df=pd.read_csv('nba.csv')
print(df)
print(df['Name'])
print(df['Name'][0:6])

print(df[['Name','Team','Salary']].head(10))

#新增資料
# 1 的位子為索引
df.insert(1, column='Sport', value='checked')
print(df.head())

#刪除資料
#刪除資料 要加df= ，insert()不用
#axis=0(表示刪除的是row)
#axis=1(表示刪除的是column)
df=df.drop('Sport',axis=1)
print(df.head())
#2是將column索引2的資料刪除
df=df.drop(2,axis=0)
print(df.head())

#遺值
#(一)要不要處理(二)1.刪除2.填滿
#刪除
df=df.dropna()#沒寫inplace，要寫df= 
df.dropna(inplace=True)#inplace預設false
#刪特定值
df.dropna(subset=['欄位名稱','欄位名稱'])
#填滿
#填0,填1,mean,眾數,中位數,自訂
df=df.fillna(10000)
print(df.head())

#排序資料
print(df.sort_values('Name'))
#%%#filter
import pandas as pd
df=pd.read_csv('nba.csv')


#none不設定，全部show出來
#顯示所有列、欄
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print(df['Age']>=25)#只會顯示T/F
#filter
mask=(df['Age']>=25)
print(df[mask].head(8))
mask1=(df['Age']<29)
print(df[mask & mask1].head(8))

#between 包前包後
mask2=df['Age'].between(20,28)
print(df[mask2].head(8))

#判斷哪些值在裡面
mask3=df['Age'].isin([25,28,32])
print(df[mask3].head(8))
print(df[mask3].values[:10])
print(df[mask3].index.values[:10])
#%%
import pandas as pd
import numpy as np
#rand產生0~1數 5欄3列 
#\這是換行
#欄列名只能有一個字才能用index='abcde col=xyz.... 
df =pd.DataFrame(np.random.rand(5,3),\
        index=list('ABCDE'),columns=list('XYZ'))
print(df)

#loc
print(df.loc['A','X'])#loc['row','column] 包前包後
print(df.loc['B':'D',:])
print(df.loc[:,'X':'Y'])
print(df.loc[['B','E'],['X','Z']])#取特定欄列

#iloc
print(df.iloc[0,0])#不管欄列名是什麼[]裡都要用索引
print(df.iloc[0:2,:])#包前不包後
print(df.iloc[:,0:2])
print(df.iloc[[0,2],[0,2]])
#%%
#groupby
import pandas as pd
col=['class','name','bd']
data=[['classA','ANDY','1995-05-03'],
      ['classB','RITA','1995-10-12'],
      ['classC','NICO','1997-11-30'],
      ['classA','AA','2000-02-02'],
      ['classB','BB','2010-03-03'],
      ['classC','CC','2000-04-04']]
frame=pd.DataFrame(data,columns=col)
frame_class=frame.groupby('class')
print(frame_class.groups)
#取classA資料
print(frame_class.get_group('classA'))
#%%
import pandas as pd
import numpy as np
df=pd.DataFrame(
{'A':['aa','bb','aa','bb'],
'B':['one','two','one','two'],
'C':np.random.randn(4),
'D':np.random.randn(4)})
print(df)
print(df.groupby('A').sum())#B不會顯示
print(df.groupby(['B','A']).sum())

sector=df.groupby('A')
print(sector.get_group('aa'))#取出A是aa的資料
print(sector.get_group('bb'))#取出A是bb的資料
#%%
import pandas as pd
#法一
df=pd.read_csv('nba.csv')
df.to_csv('nba2.csv')
df.to_csv('nba3.csv',index=0)#不顯索引
df.to_csv('nba4.csv',index=0,header=0)#不顯header表頭

#法二(不建議)
df=pd.read_csv('nba.csv')#讀原檔
df.to_csv('nba5.csv')#輸出新檔
df0=pd.read_csv('nba5.csv')#把新檔讀進來
df1=pd.read_csv('nba5.csv',index_col=(0))#讀新檔進來沒索引
df2=pd.read_csv('nba5.csv',index_col=0,header=0)#讀新檔進來沒索引沒表頭
#%%
import pandas as pd
import numpy as np

x=np.random.rand(100,4)#100筆 4欄
y=np.random.randn(100,4)#常態分佈 0的地方機率大
#日期
df1=pd.DataFrame(x,index=pd.date_range('3/1/22',
                                       periods=100),columns=list('ABCD'))
df2=pd.DataFrame(y,index=pd.date_range('3/1/22',
                                       periods=100),columns=list('ABCD'))

#資料未累加 顯示圖表
df1.plot()
df2.plot()

#資料累加 顯示圖表
df1=df1.cumsum()
df2=df2.cumsum()
df1.plot()
df2.plot()
#%%
import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(500,3),columns=list('xyz'),
                index=pd.date_range('1/1/2022',periods=500))
#設定累加
df=df.cumsum()
#折線圖 灰階
df.plot(colormap='gray').set_ylabel('Value',fontsize=12)

#長條圖
df2=pd.DataFrame(np.random.rand(5,3),columns=['a','b','c'])
#stacked=true 堆疊
df2.plot(kind='bar',fontsize=12,stacked=True)







