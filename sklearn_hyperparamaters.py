from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the data
X, y = load_data()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a LinearRegression object with custom hyperparameters
model = LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=-1)

# normalize is whether the datasets will be scaled to the same scale
# n_jobs: specifies the number of cpu cores to used in training the model
# copy_x: specifies whether the values of independent variables can be copied 
# in line equation, y = mx+b : b is the intercept, so fit_intercept is whether that b will be calculated

# Fit the model to the training data
model.fit(X_train, y_train)

# Use the model to make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
score = model.score(X_test, y_test)
print("R^2: ", score)
