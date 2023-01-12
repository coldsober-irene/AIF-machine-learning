# MinMaxScaler scales the data to a given range, usually between 0 and 1. It subtracts the minimum value and divides by the range of the data. 
# It can be useful when the data has outliers or a wide range of values.

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

#StandardScaler standardizes the data by subtracting the mean and dividing by the standard deviation. This is useful when the data has a Gaussian distribution.
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# It is important to note that normalization is done on the training set and should be applied to the test set using the transform() method
# and the same scaler object (not the fit_transform()) to avoid leaking information from the test set into the training set.
# Also, it's important to mention that not all datasets need to be normalized, 
# and it depends on the specific problem you're working on and the characteristics of your data.

# Imputer: used to handle missing values in the data by replacing them with a specific value (e.g., the mean, median, or most frequent value)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
imputer.fit_transform(X)

# LabelEncoder : used to convert categorical variables into numerical values.
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
encoder.fit_transform(y)

# OneHotEncoder: used to convert categorical variables into a binary encoded representation.
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
encoder.fit_transform(X)

# MinMaxScaler and StandardScaler : used to normalize the data by scaling it to a specific range or standardizing it by removing the mean and scaling to unit variance.
from sklearn.preprocessing import MinMaxSc


