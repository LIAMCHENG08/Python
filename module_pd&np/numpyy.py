#產生陣列
import numpy as np
x=np.array(([1,2,3],[4,5,6]))#轉換成陣列
y=np.array([(1,2,3),(4,5,6)])
print(x,y,sep='\n')#輸出結果是一樣的

data=[1,2,3,4,5]
array1=np.array(data)
array2=np.array(data,dtype=(float))#dtype轉換裡面的型態
array3=np.array(data,dtype=(bool))
print(array1,array2,array3,sep='\n')

#無中生有陣列
print(np.zeros((3,5)))#裡面為容器
print(np.ones((3,2)))#裡面值為浮點數

print(np.arange(3,20,2,dtype=float))#包前不包後,型態轉換
print(np.linspace(0,100,21))#包前包後，平均切分

#相關屬性
a=np.array([[3,6,9],[2,4,6]])
print(a.ndim)#多少維度
print(a.shape)#幾行幾列
print(type(a))# a的型態
print(a.dtype)#a裡面元素的型態
print(a.data)#記憶體位子
print(a.T)#轉置，一個對一個或轉90度
print(a)#轉置後還是不變，除非寫a=a.T
print(a.size)#元素個數
print(a.itemsize)
print(a.nbytes)

#統計函式
n=np.random.rand(5,4)#5*4的常態分佈
print(n)
print(n.mean())#平均值
print(n.sum())#總和
print(n.min())
print(n.max())
q=np.array([[2,3,4],[5,6,7]])
print(q.cumsum())#累計加總2+3+4+5+6+7 會變成一維陣列
print(np.std(n))#標準差
#%%
import numpy as np
x=np.arange(12).reshape(2,6)
print(x)
y=x[1][1:]
print(y)
y[1]=200  
print(y)
print(x)#資料會變動，因為是同一個東西

arr=np.arange(10) 
slice=arr[5:8]#slice是arr索引5到7
arr[5:8]=7#arr5到7的值換成7
slice[1]=87#slice索1值換87
print(slice)
print(arr)#是同一個東西，所以換掉slice[1]索引1的值，arr的值也會更動



x1=np.arange(12).reshape(3,4)
print(x)
y1=x[[0,1,2],[2,1,0]]#一個對一個
print(y1)

z1=x[np.ix_([0,2],[1,3])]#可用於抓任一點 全部都要對到
print(z1)

x2=np.arange(36).reshape(6,6)
print(x2)
y2=x2[0,3:5] #data[row:間格,column:]
print(y2)
z2=x2[:,2]
print(z2)
q1=x2[2::2,::2]
print(q1)

