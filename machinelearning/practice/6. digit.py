# #############################################################################
# 本題參數設定，請勿更改
seed = 0    # 亂數種子數
# #############################################################################
# TODO

import numpy as np
from sklearn.datasets import load_digits

# 載入手寫數字資料集
dataset=load_digits()
X_digits =dataset.data    #TODO    數值特徵
y_digits =dataset.target    #TODO    數字類別

# 特徵標準化(scale/StandardScaler)
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
# TODO
data=scale(X_digits)
# 取出資料集的數字類別數
n_digits = 10


# 建立兩個 K-Means 模型，除以下參數設定外，其餘為預設值
# #############################################################################
# kmean1: init='k-means++', n_clusters=n_digits, n_init=10, random_state=seed
# kmean2: init='random', n_clusters=n_digits, n_init=10, random_state=seed
# #############################################################################
from sklearn.cluster import KMeans
# TODO
kmean1=KMeans(init='k-means++', n_clusters=n_digits, n_init=10, random_state=seed)
kmean2=KMeans(init='random', n_clusters=n_digits, n_init=10, random_state=seed)
# 利用 PCA 結果建立 K-Means 模型，除以下參數設定外，其餘為預設值
# #############################################################################
# pca: n_components=n_digits, random_state=seed
# kmean3: init=pca.components_, n_clusters=n_digits, n_init=1, random_state=seed
# #############################################################################
from sklearn.decomposition import PCA
# TODO
pca=PCA(n_components=n_digits, random_state=seed).fit(data)
kmean3=KMeans(init=pca.components_, n_clusters=n_digits, n_init=1, random_state=seed)

# 分別計算上述三個 K-Means 模型的輪廓係數(Silhouette coefficient)與
# 分類準確率(accuracy)，除以下參數設定外，其餘為預設值
# #############################################################################
# silhouette_score: metric='euclidean'
# #############################################################################
from sklearn.metrics import silhouette_score
from sklearn.metrics import accuracy_score
lst_name = ['K-Mean (k-means++)', 'K-Means (random)', 'K-Means (PCA-based)']
# TODO
lst_model=[kmean1,kmean2,kmean3]

for name,model in zip(lst_name,lst_model):
    model.fit(data)
    silhouette=silhouette_score(data,model.labels_,metric='euclidean')
    print((name,silhouette))
    print(accuracy_score(y_digits,model.labels_))
    



# 進行 PCA 降維後再做 K-Means，除以下參數設定外，其餘為預設值
# #############################################################################
# kmeans: init='k-means++', n_clusters=n_digits, n_init=10, random_state=seed
# PCA: n_components=2, random_state=seed
# #############################################################################
# TODO
kmeans=KMeans(init='k-means++', n_clusters=n_digits, n_init=10, random_state=seed)
reduce_data=PCA(n_components=2, random_state=seed).fit_transform(data)
kmeans.fit(reduce_data)

print('PCA+KMeans Silhouette=   ',silhouette_score(reduce_data,kmeans.labels_,metric='euclidean'))
print('Accuracy=    ',accuracy_score(y_digits ,kmeans.labels_))

#ANS
#0.1441
#0.1410
#0.1388
#0.3780