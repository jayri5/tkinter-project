from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("Admission_Predict.csv")

#print df.head()
#print df['CGPA']
#print df.CGPA+ df.Research

#features = ['GRE Score', 'CGPA']
X = df[['CGPA','Research']]
y = df['Prob']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=10)
clf = LinearRegression()
clf.fit(X_train, y_train)
#print clf.predict(X_test)
#print y_test
result = clf.score(X_test,y_test)
print "Accuracy of the model = ", result*100

#print clf.predict([[350,150,5,2.5,2.5,8.6,1,0.92]])
