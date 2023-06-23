#反斜線 \n換行 \t:Tab \"想出現單雙引號 
print('\\')

print('\'i\'m \n\ta guy\'')
      
#%%
#變數命名 

name='abc'
name=789-1234.123
abc=1234

#%%
#字串只能乘正整數  運算符號
print(20-True*2)
print('abc'*2)
print(12/5)
print(12//5)
print(12%5)
print(2**3)
#%%
#簡寫
a,b,c=3,4,5

b+=a
a*=c
c-=b
e=a/b
f=a**b
print(a>b)
print(a==b)
print(a,b,c,e,f)

print(a==15 and b==7)
#%%
#sep預設" " end預設"\n" 用法
print(100,111.5,False,'abc',sep=',',end="")
print(True,end=('!!!'))
print(bool())
#%%
'''#input()裡面不管是什麼都為字串 用eval可變各種型態，
如()是變數需事先設定'''

'''PI=3.14159
r=eval(input('請輸入圓半徑:'))
print('半徑為',r,"的圓面積為",PI*r*r,sep="")'''

abc='xyz'
name=eval(input("請輸入東西"))
#%%
#格式化輸出(一)
#%d 10進位整數 %f 10進位浮點數 %s字串格式符號

print('%-5d除%6d是%-10.2f'%(20,7,20/7))
print('哈囉!%-5.2s哈哈哈'%'python')  
#%%
#格式化輸出(二)
# %==>{:} .format

print('{1:?^9.3f}除以{0:!>9.3f}'.format(-20,-10))
 #%%
#練習
legth=eval(input("請輸入正方形之邊長:"))
perimeter=legth*4
area=legth**2
print('邊長為{0:.2f}周長為{1:.2f}面積為{2:.2f}'.format(legth,perimeter,area))
#%%
s="python程式設計"
print(s[2:5])
print(s[3:8])
print(s[5:-1])
print(s[:-2])
print(s[2:])
print(s[-1:0:-1])
print(s[-2:-8:-2])
print(s[-8:-2:2])
print(s[::2])
#%%
#test函式
print(ord('a'))
print(chr(125))
t1='hello python'
print(len(t1))
print(t1.upper())
print(t1.title())
print(t1.islower())
print(t1.isalpha())
t2='12345'
t3='二'
print(t2.isdigit())
print(t3.isdigit())

print(t2.isnumeric())
print(t3.isnumeric())
#%%
#字串處理
t1='hohohoho'
print(t1.count('ho'))
print(t1.startswith('ho'))
t2='2,4,8,15,6'
print(t2.split(','))
t3='   holy moly  '
print(t3.strip())
print(t3.lstrip())
t4='?????www.world'
print(t4.lstrip('?w'))
k='hello kitty'
print(format(k,'?^24'))
#%%
#數值處理函數
print(abs(-100))#絕對值
print(pow(2, 10))#次方
print(divmod(1025, 2))#商數&餘數

print(int(66.66))
print(int('666'))
print(int('66.66'))#無法處理
print(float(666))
print(float('666'))
print(float('66.66'))#可以處理

print(round(5.5))#回傳最接近的數，奇數進位、偶數不進位,負數則相反
print(round(6.5))
print(round(-5.5))
print(round(-6.5))

#猜數字遊戲
import random
num = random.randint(1, 6)
answer = eval(input('請猜數字1-6:'))
print(num, '==' ,answer, 'is',num == answer)


import math
print(10*10*math.pi)
#%%
#自訂函數
#1.宣告函數a.需def進行宣告 b.加縮排
#2.呼叫函數a.函數名稱一樣 b.()內個數一樣 ps()內不管是甚麼型態，個數一樣就都可以
def saysth(x,y):
    print('hello kitty!'*2)
    
saysth(bool(), '123.122')
#%%
def teatime(dessert,drink='奶茶'):#可以預設參數值，但無預設要在前、有預設要在後
    print('我的甜點:',dessert,'\n飲料:',drink,sep='')
teatime('蔥抓餅','咖啡')#引數會取代參數
teatime(drink='啤酒',dessert='炸雞')#可以調換引數順序，只是需要把參數抓下來等於
teatime('牛排')#預設參數值 引數可以不用帶
#%%
#全域&區域
x=100
def test():
    print(x)
test()
#%%
x=100
def test():
    x=200
    print(x)
test()#區域為200
print(x)#全域100
#%%
#return的目的將區域轉全域，如不之後不會用到，則可以不寫return，函式也可以成立
def num(x,y):
    num1=x//y#商
    num2=x%y#餘數
    return num1,num2
x=eval(input('請輸入被除數:'))
y=eval(input('請輸入除數:'))
print(num(x, y))
#%%
#if else
num1=eval(input('請猜一個0-100的數:'))

if num1!=87:
    print('猜錯了')
   
else:
    print('答對了')
  #%%  
num1=eval(input('請猜一個0-100的數:'))

print('猜對了' if num1==87 else '答錯了')
#%%
#if elif else #巢狀
musttolose=input('請輸入剪刀、石頭、布:')

if musttolose =='剪刀':
    print('我出石頭你輸了')
elif musttolose =='石頭':
    print('我出布你輸了')
elif musttolose =='布':
    print('我出剪刀你輸了')
else:
    print('輸不起??')
#%%
#不建議用巢狀閱讀性不佳 用elif也可以做出來
score =eval(input('輸入0-100:'))  
if score>=90:
    print('great')
else:
    if score>=80:
        print('good')
    else:
        if score >=70:
            print('not bad')
        else:
            print('very bad')
#%%
# while&for 迴圈
number = eval(input('請輸入一個數值:'))
while number != 87:
    if number>87:
        print('往下猜')
    else : 
        print('往上猜')
        
    number = eval(input('請輸入一個數值:'))
   
print('你答對了')


#%%
for i in range(10,-10,-2): #range裡一定是數值
    print(i)
    
name='apple banana cat'
for i in name: #name
    print(i)

for i in range(len(name)):
    print(i,name[i])
#%%
# import random
# number = random.randint(0,20)
# while number !=17:
#     if number >17:
#         print(number,'往下猜')
#         number =number-1
#     elif number <17:
#         print(number,'往上猜')
#         number=number+1
#     else:
        
        
#      print('你答對了')
#%%
i =0
while i<10:
    i =i+1
    if i%3!=0:
        continue
    print(i)
#%%
#容器
x=[]#建立串列
a=list()#轉換
a=[1,2.3,bool(),'fsf',['sasd','dss']]
print(a)
del a[2]#刪除
print(a)
a[0]=10000#更新
print(a)
b=a[3]#取得
print(b)
c=a[0:3]#回傳
print(c)
d=a[3][1]
print(d)
#%%
y=[1,2,3]
z=[6,100,7]
print(y+z,y*3)#兩串列相加還是一個串列  
              #相乘還是一個串列
q=[1,4,9,['dfg','hjk']]
w=[9,1,4]
print(q==w)#順序不一樣就是不一樣
print('d' in q,'dfg' in q)#要一模一樣才能找出

print(q[0])

#用串列建構建立串列
aaa=[i for i in range(10)]#i是產生的值
print(aaa)

aaa=[i+3 for i in range(10)]#i+3是產生的值
print(aaa)

print(len(aaa))#算個數
print(sum(aaa))#加總

q.append(10)#加值
print(q)
q.extend(w)#加容器
print(q)
#%%
#tuple與list不一樣； 是() 跟 資料不能變更(目的)
tup=tuple() #建立tuple
tup1=()

tup=(3.3,'as',bool(1))
print(tup)

a,b,c=tup#拆解 一個對一個
print(a,b,c)

a,*b=(1,'fgg',9.99)# *意思是剩下其他的，b產生的結果會轉成list
print(a,b)
#%%
#set 沒有順序(不支援相關運算) 以{}表示 目的:唯一性
A=set()#建立
A.add(3)
b={1,3,'a','d'}
print(A,b)
c={3,'a',1,'d'}
print(b==c)#沒順序
s1={1,1,2,2,2,2,3,3,3,3,3}
s2={1,2,2,2,3,3,3}
print(s1,s2,sep='\n')#唯一性 不管擺多少只會取出一個
print(len(s1))#個數
s3={1,2,3,4}
s4={3,4,5,6}
print(s3-s4)#只可用- 表差集
#%%
#dict 字典 沒有順序、不可重複、可改變值 不可改變key
s1={'one':1,'two':2,'three':3}#建立
s2=dict(three=3,one=1,two=2)
print(s1==s2)#沒順序
print(s1,s2,sep='\n')

s3={}
s3['10']=10#新增 s3[key]=值
s3['20']=20
s3['30']=30
print(s3)
del s3['10']#刪值整組被拿掉
print(s3)
s4=s3['30']#key有點被拿來當索引
print(s4)
s3['30']=100 #變更值
print(s3)

s5=dict(a=1,b=2,c=3)
s6=dict(a=9,b=2,c=4)
print(s5['a']==s6['a'])#值不一樣
print(s5['c']!=s6['c'])
print(1 in s5)#in / not in 找值會找不到
print('a'in s5)#要找key

s7={'q':10,'w':20,'e':30}
print(s7.keys())#key
print(s7.values())#值
print(s7.items())#全部
#%%
#模組命名
import calendar #法一
print(calendar.month(2019,2))

import calendar as cal #簡寫
print(cal.month(2019,3))
#%%
#不用在寫模組名
from calendar import month
print(month(2019, 3))

