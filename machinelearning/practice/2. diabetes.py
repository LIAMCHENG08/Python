from sklearn import datasets
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.model_selection import train_test_split as tts
# TODO
diabetes=datasets.load_diabetes()

#get x
# TODO 
X=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
y=pd.DataFrame(diabetes.target,columns=['value'])

#Total number of examples
# TODO 
lm=LinearRegression()
lm.fit(X, y)

ypred=lm.predict(X)
print('Total number of examples')
print('MSE=','{:.4f}'.format(mse(y, ypred)))
print('R-squared=','{:.4f}'.format(lm.score(X, y)))
#3:1 100
xTrain2, xTest2, yTrain2, yTest2=tts(X,y,test_size=0.25,random_state=(100))
lm2=LinearRegression()
lm2.fit(xTrain2,yTrain2)
# TODO 
ypredtest=lm2.predict(xTest2)
ypredtrain=lm2.predict(xTrain2)


print('Split 3:1')
print('train MSE=','{:.4f}'.format(mse(yTrain2,ypredtrain)))
print('test MSE=','{:.4f}'.format(mse(yTest2,ypredtest)))
print('train R-squared=','{:.4f}'.format(lm2.score(xTrain2,yTrain2)))
print('test R-squared=','{:.4f}'.format(lm2.score(xTest2,yTest2)))

# Total number of examples
# MSE= 2859.6904
# R-squared= 0.5177
# Split 3:1
# train MSE= 2947.9337
# test MSE= 2665.2278
# train R-squared= 0.5064
# test R-squared= 0.5283