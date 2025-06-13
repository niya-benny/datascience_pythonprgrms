import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

from p2 import address

address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/iris.csv"
dataset=pd.read_csv(address)
print(dataset.head())

print(dataset.Species.unique())

x=dataset.iloc[:,1:5]
print(x)

y=dataset.iloc[:,5]
print(y)

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3,random_state=0)

clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)

y_predict=clf.predict(x_test)
print(y_predict)

accuracy= metrics.accuracy_score(y_test,y_predict)
print("Accuracy: ",accuracy)

