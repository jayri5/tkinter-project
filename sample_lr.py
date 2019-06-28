from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

iris = datasets.load_iris()

#print type(iris)
#print iris.data
#print iris.feature_names
#print iris.target
#print iris.target_names

X = iris.data[:,3]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=4)
X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
#print y_test_mod

y_test = y_test.ravel()
y_pred = y_pred.ravel()
#print y_pred

print(r2_score(y_test ,y_pred))
