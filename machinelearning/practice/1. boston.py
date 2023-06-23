from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
# TODO
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae

boston = load_boston()
# df = pd.DataFrame(boston.data.T, ['CRIM','ZN','INDUS','CHAS','NOX','RM' ,'AGE','DIS','RAD','TAX', 'PTRATIO','B','LSTAT']) #有13個feature
# TODO
# MEDV即預測目標向量
# TODO
# X = df[['CRIM','ZN','INDUS','CHAS','NOX','RM' ,'AGE','DIS','RAD','TAX', 'PTRATIO','B','LSTAT']]
# y = df['MEDV']
X=pd.DataFrame(boston.data,columns=boston.feature_names)
y=pd.DataFrame(boston.target,columns=['medv'])
y=y['medv']
#分出20%的資料作為test set
# TODO
XTrain,XTest,yTrain,yTest=tts(X,y,test_size=0.2,random_state=1)

#Fit linear model 配適線性模型
lm=LinearRegression()
lm.fit(XTrain,yTrain)

ypred=lm.predict(XTest)

# TODO
print('MAE:','{:.4f}'.format(mae(yTest, ypred)))
print('MSE:','{:.4f}'.format(mse(yTest, ypred)))
print('RMSE:','{:.4f}'.format(mse(yTest, ypred)**0.5))

X_new=[[0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90 , 4.98]]
X_new=pd.DataFrame(X_new)
prediction = lm.predict(X_new)
print('{:.4f}'.format(float(prediction)))

#ans
#MAE: 3.7507
# MSE: 23.3808
# RMSE: 4.8354
# 30.0663