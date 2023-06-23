import pandas as pd

# 載入寶可夢資料集
# TODO
data=pd.read_csv('pokemon.csv')
# 處理遺漏值
features = ['Attack', 'Defense']
# TODO
data.dropna(axis=0,subset=features,inplace=True)
# 取出目標寶可夢的 Type1 與兩個特徵欄位
# TODO
a=data['Type1']=='Normal'
b=data['Type1']=='Fighting'
c=data['Type1']=='Ghost'
selectdata=data[a|b|c]
xtrain,ytrain=selectdata[features],selectdata['Type1']
# 編碼 Type1
from sklearn.preprocessing import LabelEncoder
# TODO
le=LabelEncoder()
ytrain=le.fit_transform(ytrain) 

# 特徵標準化
from sklearn.preprocessing import StandardScaler
# TODO
scalar=StandardScaler()
scalar.fit(xtrain)
xtrainstd=scalar.transform(xtrain)


# 建立線性支援向量分類器，除以下參數設定外，其餘為預設值
# #############################################################################
# C=0.1, dual=False, class_weight='balanced'
# #############################################################################
from sklearn.svm import LinearSVC
# TODO
model=LinearSVC(C=0.1, dual=False, class_weight='balanced')
model.fit(xtrainstd,ytrain)
# 計算分類錯誤的數量
# TODO
ypred=model.predict(xtrainstd)
print((ytrain!=ypred).sum())
# 計算準確度(accuracy)
from sklearn.metrics import accuracy_score
print('Accuracy: ',accuracy_score(ytrain, ypred))

# 計算有加權的 F1-score (weighted)
from sklearn.metrics import f1_score
# TODO
f1=f1_score(ytrain,ypred,average='weighted')
print('F1-score: ',f1)

# 預測未知寶可夢的 Type1
# TODO
newdata=[[100,75]]
newdata=scalar.transform(newdata)
label=le.inverse_transform(model.predict(newdata))
print(label)