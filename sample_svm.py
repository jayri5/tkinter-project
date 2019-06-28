from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import datasets
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

#print type(iris)
#print iris.data
#print iris.feature_names
#print iris.target
#print iris.target_names

X = iris.data[:,3]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=4)
X_train_mod = X_train.reshape(-1,1)
X_test_mod = X_test.reshape(-1,1)
y_train_mod = y_train.reshape(-1,1)
y_test_mod = y_test.reshape(-1,1)

model = svm.SVC(kernel='linear')
model.fit(X_train_mod,y_train_mod)
y_pred_mod = model.predict(X_test_mod)


print(accuracy_score(y_test_mod,y_pred_mod))
