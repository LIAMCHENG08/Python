#分群 kmeans
import pandas as pd
import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt

X=pd.DataFrame({
    'length':[51,46,51,45,51,50,33,38,37,33,33,21,23,24],
    'weight':[10.2,8.8,8.1,7.7,9.8,7.2,4.8,4.6,3.5,3.3,4.3,2.0,1.0,2.0]})
#分3群
k=3

kmeans=cluster.KMeans(n_clusters=k,random_state=22)
kmeans.fit(X)
#結果
print(kmeans.labels_)

colmap=np.array(['r','g','y'])
plt.scatter(X['length'],X['weight'],color=colmap[kmeans.labels_])
plt.show()
#%% 有ans不給 分群
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt
import sklearn.metrics as sm

iris =datasets.load_iris()

X=pd.DataFrame(iris.data,columns=iris.feature_names)
X.columns=['sepal length','sepal width','petal length','petal width']
y=iris.target
k=3

kmeans=cluster.KMeans(n_clusters=k,random_state=(12))
kmeans.fit(X)
print(kmeans.labels_)
print(y)
#由輸出看出kl:[1→0,2→1,0→2]

#由圖可知無法直接比較 還需修正
colmap=np.array(['r','g','y'])
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.subplots_adjust(hspace=.5)
plt.scatter(X['petal length'],X['petal width'],color=colmap[y])
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.title('real classification')


plt.subplot(1,2,2)
plt.scatter(X['petal length'],X['petal width'],color=colmap[kmeans.labels_])
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.title('kmeans classification')
plt.show()


print('kmeans classification',kmeans.labels_,sep='\n')

#由輸出看出kl:[1→0,2→1,0→2]
#修正標籤         放原資料[0,1,2]→ 修正值
pred_y=np.choose(kmeans.labels_,[2,0,1])
print('kmeans classification',pred_y,sep='\n')
print('real classification',y,sep='\n')

#績效矩陣
print('績效矩陣',sm.accuracy_score(y,pred_y),sep='\n')
#混淆矩陣
print('混淆矩陣',sm.confusion_matrix(y,pred_y),sep='\n')

#修正圖
colmap=np.array(['r','g','y'])
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.subplots_adjust(hspace=.5)
plt.scatter(X['petal length'],X['petal width'],color=colmap[y])
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.title('real classification')

plt.subplot(1,2,2)
plt.scatter(X['petal length'],X['petal width'],color=colmap[pred_y])
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.title('kmeans classification')
plt.show()
#%% DBSCAN 分群
from sklearn.cluster import DBSCAN
import numpy as np

X=np.array([[2,3],[3,4],[4,5],[18,71],[19,73],[20,67],[125,180]])
#eps 半徑 minsample 半徑內有幾個
clustering=DBSCAN(eps=3,min_samples=2)
clustering.fit(X)

y_predict=clustering.labels_
print(y_predict)





