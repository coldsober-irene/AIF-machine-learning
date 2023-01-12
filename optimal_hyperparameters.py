from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score

# Load the data
X, y = load_data()

# Define the parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2']
}

# Create an instance of the RandomForestClassifier
clf = RandomForestClassifier()

# Create the scorer
scorer = make_scorer(accuracy_score)

# Create the GridSearchCV object
grid_search = GridSearchCV(clf, param_grid, scoring=scorer, cv=5)

# Fit the GridSearchCV object to the data
grid_search.fit(X, y)

# Print the best parameters and the best score
print("Best parameters: {}".format(grid_search.best_params_))
print("Best score: {:.2f}%".format(grid_search.best_score_ * 100))


# The GridSearchCV object is then created by passing the RandomForestClassifier object, 
# the parameter grid, and the scoring function. The cv parameter is used to specify the number of folds for cross-validation. 
# The fit method is then used to perform the grid search. Finally, 
# the best_params_ and best_score_ attributes are used to print the optimal hyperparameters and the best score.
