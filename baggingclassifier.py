from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

base_estimator = DecisionTreeClassifier()
bag_clf = BaggingClassifier(base_estimator=base_estimator, n_estimators=10, random_state=42)
bag_clf.fit(X_train, y_train)

accuracy = bag_clf.score(X_test, y_test)
print("Accuracy:", accuracy)
