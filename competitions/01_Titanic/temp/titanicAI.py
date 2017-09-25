import pandas as pd
from sklearn import datasets,linear_model
from sklearn.linear_model import LinearRegression
import csv

reader = csv.reader(file('train.csv', 'rb'))
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
train['Sex'][train.Sex=='male']=1
train['Sex'][train.Sex=='female']=-1
train['Sex'][train.Sex=='male']=1
train['Sex'][train.Sex=='female']=-1
linreg = LinearRegression()
x_train=train[["Pclass","Sex","Age","SibSp","Parch","Fare"]]
y_train=train[["Survived"]]
print x_train.head()
linreg.fit(x_train, y_train)
