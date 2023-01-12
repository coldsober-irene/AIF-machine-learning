from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Load the data
X, y = load_data()

# Create an instance of the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, max_depth=5)

# Perform cross-validation
scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')

# Print the mean and standard deviation of the scores
print("Accuracy: {:.2f}% (+/- {:.2f}%)".format(scores.mean() * 100, scores.std() * 100))

"""this is the techniques used in sklearn to measure the performance of the model"""
# The cross_val_score function takes the RandomForestClassifier object, the input data (X), 
# and the target data (y) as arguments, as well as the number of folds for cross-validation (cv) and the scoring metric (scoring). 
# It returns an array of scores, one for each fold. 
# In this example, the mean and standard deviation of the scores are printed to provide an estimate of the model's performance
