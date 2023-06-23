#簡單迴歸
#匯入套件
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#設定來源
temp= np.array([29,28,34,31,25,29,32,31,24,33,25,31,26,30])
sales=np.array([7.7,6.2,9.3,8.4,5.9,6.4,8.0,7.5,5.8,9.1,5.1,7.3,6.5,8.4])

X=pd.DataFrame(temp,columns=['temperature'])
y=pd.DataFrame(sales,columns=['drink sales'])

#建立模型
lm=LinearRegression()
lm.fit(X, y)
print('迴歸係數:',lm.coef_)
print('截距:',lm.intercept_)

#進行預測 氣溫26 30 的業績
#當初設定什麼型態，預測也依定是那種型態
newtemp=pd.DataFrame(np.array([26,30]),columns=['temperature'])
#predict_sales一定在線上面 以新資料預測y
predict_sales=lm.predict(newtemp)
print(predict_sales)

#繪圖表示
plt.scatter(temp,sales)#散布圖
regsales=lm.predict(X)#以原資料預測y值
plt.plot(temp,regsales,color='blue')#劃出迴歸線
plt.plot(newtemp,predict_sales,color='red',marker='o',markersize=10)
plt.show()
#%%多元迴歸
#匯入套件
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#資料設定
waist_heights=np.array([[67,160],[68,165],[70,167],[65,170],[80,165],[85,167],[78,178],[79,182],[95,175],[89,172]])
weight=np.array([50,60,65,65,70,75,80,85,90,81])
X=pd.DataFrame(waist_heights,columns=['waist','height'])
y=pd.DataFrame(weight,columns=['weight'])

#建立模型
lm=LinearRegression()
lm.fit(X, y)
print('迴歸係數:',lm.coef_)
print('截距:',lm.intercept_)

#預測腰圍跟身高[64,164][82,172]的體重
new_waist_height=pd.DataFrame(np.array([[66,164],[82,172]]))
predict_weight=lm.predict(new_waist_height)
print(predict_weight)
#%%資料集
from sklearn import datasets

#botson dialabetes 用於回歸
boston =datasets.load_boston()
diabetes=datasets.load_diabetes()

#iris digits 主用於分類
iris= datasets.load_iris()
digits=datasets.load_digits()

print(boston.keys())
print(diabetes.keys())
print(iris.keys())
print(digits.keys())
#bunch 很像dict +.欄位可以直接抓值
print(boston.feature_names)
print(boston.DESCR)
#%%波士頓房價
import pandas as pd
from sklearn import datasets

boston=datasets.load_boston()
#建立dataframe
X=pd.DataFrame(boston.data,columns=boston.feature_names)
print(X.head())
target=pd.DataFrame(boston.target,columns=['MEDV'])
print(target.head())
#%%波士頓房價
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

boston=datasets.load_boston()
#建立dataframe
X=pd.DataFrame(boston.data,columns=boston.feature_names)
target=pd.DataFrame(boston.target,columns=['MEDV'])
#用另一種方式 轉一維
y=target['MEDV']
#原先是這樣
#y=pd.DataFrame(boston.target,columns=['MEDV'])


lm=LinearRegression()
lm.fit(X, y)
print('迴歸係數:',lm.coef_)
print('截距:',lm.intercept_)

predict_price=lm.predict(X)



coef=pd.DataFrame(boston.feature_names,columns=['features'])
coef['estimatedcoef']=lm.coef_#新增欄位
print(coef)

#繪RM跟y的關係
plt.scatter(X.RM, y)
plt.title('relationship bwt RM & price')
plt.show()

plt.scatter(y,predict_price)
plt.show()

#%%測試訓練資料集
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import matplotlib.pyplot as plt

boston=datasets.load_boston()
#建立dataframe
X=pd.DataFrame(boston.data,columns=boston.feature_names)
target=pd.DataFrame(boston.target,columns=['MEDV'])
#用另一種方式 轉一維
y=target['MEDV']

#測試訓練
XTrain,XTest,yTrain,yTest=tts(X,y,test_size=0.33,random_state=(5))
#回歸 帶訓練的資料
lm=LinearRegression()
lm.fit(XTrain,yTrain)
#帶預測資料
predict_test=lm.predict(XTest)
predict_train=lm.predict(XTrain)

#績效衡量 MAE MSE RMSE 指誤差，所以其值越小越好
#MAE
MAE_train=mae(yTrain, predict_train)
MAE_test=mae(yTest,predict_test)
#MSE
MSE_train=mse(yTrain,predict_train)
MSE_test=mse(yTest,predict_test)
#另一寫法
#MSE_train=np.mean((yTrain-predict_train)**2)
#MSE_test=np.mean((yTest-predict_test)**2)

#RMSE
RMSE_train=mse(yTrain,predict_train)**0.5
RMSE_test=mse(yTest,predict_test)**0.5

print('訓練資料的MSE',MSE_train)
print('測試資料的MSE',MSE_test)

#績效衡量 R 解釋能力(占比) 越大越好 0-1
print('訓練資料的R',lm.score(XTrain,yTrain))
print('測試資料的R',lm.score(XTest, yTest))

plt.scatter(yTest,predict_test)
plt.show()
#殘差圖
plt.scatter(predict_train,yTrain-predict_train,c='b',s=40,alpha=(0.5),label='training data')
plt.scatter(predict_test,yTest-predict_test,c='r',s=40,label='test data')
plt.hlines(y=0,xmin=0,xmax=50)
plt.legend()
plt.show()
#%%分類
#Logistic regression邏輯回歸
import pandas as pd 
import numpy as np
from sklearn import preprocessing,linear_model

#原始資料
titanic=pd.read_csv('titanic.csv')
titanic.info() 

#將年齡的空值填入年齡中位數
#nanmedian計算中位數，不會計nan值
age_median=np.nanmedian(titanic['Age'])
print('年齡中位數',age_median)
#where 判斷['Age']是不是空值，是的話帶中位數，不是的話帶原值
new_age=np.where(titanic['Age'].isnull(),age_median,titanic['Age'])
#把新的age帶回給原age
titanic['Age']=new_age
#更新後資料
titanic.info()

#轉欄位為數值
label_encoder=preprocessing.LabelEncoder()
encoded_class=label_encoder.fit_transform(titanic['PClass'])

X=pd.DataFrame([encoded_class,titanic['SexCode'],titanic['Age']]).T
y=titanic['Survived']

logistic =linear_model.LogisticRegression()
logistic.fit(X, y)
print('迴歸係數:',logistic.coef_)
print('截距:',logistic.intercept_)
#混淆矩陣(confusion matrix)
print('混淆矩陣')
preds=logistic.predict(X)
print(pd.crosstab(titanic['Survived'],preds))
#準確度
print((805+265)/(805+58+185+265))
print(logistic.score(X, y))
#%%決策樹 鳶尾花
import pandas as pd
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt

iris=datasets.load_iris()

X=pd.DataFrame(iris.data,columns=iris.feature_names)
target=pd.DataFrame(iris.target,columns=['target'])
y=target['target']

XTrain,XTest,yTrain,yTest=tts(X,y,test_size=0.33,random_state=1)

dtree=tree.DecisionTreeClassifier(max_depth=(3))
dtree.fit(XTrain, yTrain)

print('準確率',dtree.score(XTest, yTest))
print(dtree.predict(XTest))
print(yTest.values)

fig=plt.figure(figsize=(25,20))
tree.plot_tree(dtree,
               feature_names=iris.feature_names,
               class_names=iris.target_names,
               filled=(True))
fig.savefig('pic.png')
#%%
import pandas as pd
import numpy as np
from sklearn import neighbors

X=pd.DataFrame({
    'durability':[7,7,3,3],
    'strength':[7,4,4,4]})
y=np.array([0,0,1,1])
k=3

knn=neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)
#預測新產品[3,7]的分類 1好 0壞
new_tissue=pd.DataFrame(np.array([[3,7]]))
pred=knn.predict(new_tissue)
print(pred)
#%%鳶尾花
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.model_selection import train_test_split as tts

iris =datasets.load_iris()

X=pd.DataFrame(iris.data,columns=iris.feature_names)
X.columns=['sepal length','sepal width','petal length','petal width']
target=pd.DataFrame(iris.target,columns=['target'])
y=target['target']

colmap=np.array(['r','g','y'])
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.subplots_adjust(hspace=.5)
plt.scatter(X['sepal length'],X['sepal width'],color=colmap[y])
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.subplot(1,2,2)
plt.scatter(X['petal length'],X['petal width'],color=colmap[y])
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.show()

XTrain,XTest,yTrain,yTest=tts(X,y,test_size=0.33,random_state=1)
k=3
knn=neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

print('準確率',knn.score(XTest, yTest))
print(knn.predict(XTest))
print(yTest.values)

