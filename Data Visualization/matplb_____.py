#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt
#步驟二設定資料
x=np.arange(0,5,0.1)
y=np.square(x)
#步驟三將資料帶圖表
plt.plot(x, y)
#步驟四顯示圖表
plt.show

#%%
#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt
#步驟二設定資料
x=np.arange(0,5,0.1)

#步驟三將資料帶圖表
plt.plot(x,x,'r--',x,x**2,'m.',x,x**3,'g-.')
#步驟四顯示圖表
plt.show

#%%
#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt
#步驟二設定資料
x=np.array([1,2,3,4,5])
y=x**2
#步驟三將資料帶圖表
plt.plot(x,y,'ro')

#設定標題及位置
plt.title('Y=X*2', loc=('right'))

#步驟四顯示圖表
plt.show

#%%
#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt
#步驟二設定資料
year=[1950,1960,1970,1980,1990,2000,2010]
pops=[2.5,2.7,3.3,4,4.8,6.1,7]

#中文基本設定
plt.rcParams['font.family']='Microsoft YaHei'

#步驟三將資料帶圖表
plt.plot(year,pops)
plt.title('POPULATION GROWTH')

#設定標題及位置
plt.title('POPULATION GROWTH')

#設定X Y軸名稱
plt.xlabel('人口成長(年)')
plt.ylabel('人口成長數(百萬)')

#步驟四顯示圖表
plt.show
#%%
#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt
#步驟二設定資料
x=np.array([1,2,3,4,5])
y=x**2
#步驟三將資料帶圖表
plt.plot(x,y,'ro',label='Y=X**2')#label是設定圖例裡的文字

#設定標題及位置
plt.title('Y=X*2',loc=('right'))
#設定座標軸範圍
plt.xlim(-10, 10)
plt.ylim(-50, 50)
#plt.axis([-10,10,-50,50])另一方式

#設定文字
plt.text(-10,40,'Y=X**2')

#設定圖例
plt.legend()

#設定格線
plt.grid()

#步驟四顯示圖表
plt.show
#%%
#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt

#設定X Y軸名稱
plt.xlabel('age')
plt.ylabel('monthly salary')

#設定標籤
plt.xticks(np.arange(5),('','<=30','31-60','61-100',''))
plt.yticks(np.arange(5),('','<25k','25k-50k','51k-80k','>80k'))

#設定顯示刻度線
plt.minorticks_on()

#步驟四顯示圖表
plt.show
#%%
#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt
#步驟二設定資料
x=np.array([1,2,3,4,5])
y=x*2


#步驟三將資料帶圖表
plt.plot(x,y,'ro',label='Y=*2')#LABEL是設定圖例文字
#設定圖例
plt.legend()

#設定文字
plt.text(1,10,'Y=X*2')

#步驟四顯示圖表
plt.show
#%%
#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt
#步驟二設定資料
x=np.array([1,2,3,4,5])
y=x*2


#設定畫布#figsize是比例facecolor是畫布顏色
plt.figure(figsize=(6,4),facecolor=('lightblue'))
#plt.figure(figsize=(3,4),facecolor=('lightgreen'))

#另一設定spyder看不出來，存檔才看得出來
#plt.figure(dpi=300)等比例放大
plt.plot(x,y,'ro')


#步驟四顯示圖表
plt.show

#%%
#步驟一匯入套件
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)
y1=20*np.sinc(x)
y2=x*x*np.cos(x)+0.5

#設定子圖表
plt.subplot(211)
plt.plot(x,y1,'b--')
plt.subplot(212)
plt.plot(x,y2,'r--')

#步驟四顯示圖表
plt.show
#%%
#匯入套件
import matplotlib.pyplot as plt

#資料
labels='frog','hog','bog','pog'
#扇形逆時針繪製，預設從x軸開始
sizes =[20,30,40,10]

#扇形顏色
colors_=['yellowgreen','gold','lightblue','lightcoral']

#間隔
explode=(0,0,0.1,0)

#子圖2
plt.subplot(1,2,1)
plt.bar(labels, sizes,color='blue')
#子圖1
plt.subplot(1,2,2)
plt.pie(sizes,explode=explode,labels=labels,colors=colors_,shadow=(True))

#坐標軸相等
plt.axis('equal')
plt.show()