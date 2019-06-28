from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
x=iris.data[:,3]
y=iris.target
#print x.shape
#print y.shape

x = x.reshape(-1,1)


knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(x,y)
pred = knn.predict(x)
print accuracy_score(y,pred)
