import pandas as pd
import numpy as np
from sklearn import preprocessing, linear_model

# 原始資料
titanic = pd.read_csv("titanic.csv")
# print('raw data')
# TODO
agemedian=np.nanmedian(titanic['Age'])
# 將年齡的空值填入年齡的中位數
# TODO

print("年齡中位數=",agemedian)
# TODO
newage=np.where(titanic['Age'].isnull(),agemedian,titanic['Age'])
titanic['Age']=newage
# 更新後資料
# print('new data')
# TODO

# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic['PClass'])

# TODO
X=pd.DataFrame([encoded_class,titanic['SexCode'],titanic['Age']]).T
y=titanic['Survived']
# 建立模型
# TODO
lg=linear_model.LogisticRegression()
lg.fit(X, y)
print('截距=','{:.4f}'.format(float(lg.intercept_)))
print('迴歸係數=',lg.coef_[0][1])


# 混淆矩陣(Confusion Matrix)，計算準確度
print('Confusion Matrix')
# TODO
print('{:.4f}'.format(lg.score(X, y)))

# 年齡中位數= 28.0
# 截距= 1.9966
# 迴歸係數= 2.38340080218156
# Confusion Matrix
# 0.8149


