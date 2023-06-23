import numpy as np
# TODO
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score as ss

input_file = ('data_perf.txt')
# Load data 載入資料
# TODO
x=[]
with open(input_file) as f:
    content=f.readlines()
    for i in content:
        data=[eval(j) for j in i.split(',')]
        x.append(data)
x=np.array(x)    
    
# Find the best epsilon 
eps_grid = np.linspace(0.3,1.2,num=10)
silhouette_scores = []
eps_best=eps_grid[0]
silhouette_score_max=-1
labels_best=None
# TODO
# from sklearn.cluster import DBSCAN

    # Train DBSCAN clustering model 訓練DBSCAN分群模型
    # ################
    # min_samples = 5
    # ################
for eps in eps_grid:
    model=DBSCAN(eps=eps,min_samples=5)
    model.fit(x) 
    
    # Extract labels 提取標籤
    labels=model.labels_

    # Extract performance metric 提取性能指標
    silhouette_score=round(ss(x,labels),4)
    silhouette_scores.append(silhouette_score)

    print("Epsilon:", eps, " --> silhouette score:", silhouette_score)

    # TODO
    if silhouette_score > silhouette_score_max:
        silhouette_score_max=silhouette_score
        eps_best=eps
        model_best=model
        labels_best=labels
    

# Best params
print("Best epsilon =",eps_best)

# # Associated model and labels for best epsilon
model =model_best   # TODO
labels =labels_best  # TODO

# Check for unassigned datapoints in the labels
# TODO
offset=0
if -1 in labels:
    offset=1

# Number of clusters in the data 
# TODO
num_clusters=len(set(labels))-offset
print("Estimated number of clusters =", num_clusters          )

# Extracts the core samples from the trained model
# TODO

#ANS
# 0.7999
# 0.6366
# 5
# 0.6401