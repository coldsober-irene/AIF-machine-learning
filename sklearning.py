from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the data
X, y = load_data()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a LinearRegression object
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Use the model to make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
score = model.score(X_test, y_test)
print("R^2: ", score)
