#implement logistic regression algorithm using sklearn on the given IRIS dataset and display the accuracy and classification report

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import make_classification
import numpy as np


iris = datasets.load_iris()
X = iris['data']
y = iris['target']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=
0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


clf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None
, min_samples_leaf=5, bootstrap=True)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:",accuracy_score(y_test, y_pred))
print("\n")
print(classification_report(y_test, y_pred))





