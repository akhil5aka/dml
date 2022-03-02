from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
irisData=load_iris()
print(irisData.data)
x=irisData.data
y=irisData.target
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y)
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)
print(knn.predict(x_test))