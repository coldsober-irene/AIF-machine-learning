from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor

# Generate some synthetic data
X, y = make_regression(n_samples=100, n_features=5, n_targets=3, random_state=0)

# Create a RandomForestRegressor model
estimator = RandomForestRegressor(random_state=0)

# Wrap the model in a MultiOutputRegressor
multi_output_model = MultiOutputRegressor(estimator)

# Fit the model to the data
multi_output_model.fit(X, y)

# sub-method 2
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

multi_output_model.fit(X_train, y_train)
y_test_pred = multi_output_model.predict(X_test)
mse = mean_squared_error(y_test, y_test_pred)

print("Mean Squared Error on test set: ", mse)
