#coding=utf-8
import pandas as pd
from sklearn import datasets,linear_model
from sklearn.linear_model import LinearRegression
import csv
import matplotlib.pyplot as plt

def read_csv(filename):
    csvf=csv.reader(file(filename,"rb"))
    item=[]
    list=[]
    def changesex(v):
        dicsex = {"male": 1, "female": 2}
        if dicsex.has_key(v):
            return dicsex[v]
        else:
            return v
    for key,value in enumerate(csvf):
      #  value = map(lambda v: v.decode("utf-8"), value)
        if key==0:
            item=value
            print item
        else:
            value=map(changesex,value)
            dic=dict(zip(item,value))
            list.append(dic)
    return list

def assess(predict_list,test_list):
    len1= len(predict_list)
    s=0
    for i in range(len1):
        if predict_list[i]==test_list[i]:
            s+=1
    print "s",s,"len1",len1
    return float(s)/len1

def ageFit(testcsv,fil_train):
    totalAge = 0
    for a in fil_train:
        totalAge += float(a["Age"])
    perAge = totalAge / float(len(fil_train))
    newtest=testcsv
    for t in newtest:
        if t["Age"]=="":
            t["Age"]=perAge
    return newtest
def Debug_log(x_test,y_test,y_predict):
    for i in range(len(y_predict)):
        if(y_test[i] != y_predict[i]):
            print(x_test[i],y_test[i],y_predict[i])
traincsv=read_csv("../data/train/train.csv")
testcsv=read_csv("../data/test/test.csv")
ans=read_csv("../data/test/gender_submission.csv")
fil_train=filter(lambda x: x["Age"]!="" and x["Pclass"]!="" and x["Sex"]!=0,traincsv)
print pd.DataFrame(traincsv)

newtest=ageFit(testcsv,fil_train)
x_train=map(lambda x:[x["Sex"],float(x["Age"]),int(x["Pclass"])],fil_train)
y_train=map(lambda y:int(y["Survived"]),fil_train)
x_test=map(lambda x:[x["Sex"],float(x["Age"]),int(x["Pclass"])],newtest)
y_test=map(lambda y:int(y["Survived"]),ans)
print x_train
print y_train
print "x_test",x_test
regr = linear_model.LinearRegression()
regr.fit(x_train,y_train)
predict_y=map(lambda x:int(x+0.5),regr.predict(x_test))
print predict_y
print "成功率:",assess(predict_y,y_test)
Debug_log(x_test,y_test,predict_y) # 看看错误情况
pd_x_train = pd.DataFrame(x_train)
plt.scatter(pd_x_train[2], y_train,  color='black')
plt.show()
