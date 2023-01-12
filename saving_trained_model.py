# Pickle: One of the simplest ways to save a scikit-learn model is to use the pickle module to serialize the model object to a file.
# You can use the pickle.dump() function to save the model, and the pickle.load() function to load it later.

import pickle

# Save the model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load the model from a file
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Joblib: Another way to save a scikit-learn model is to use the joblib library, which is a more efficient alternative to pickle for large numpy arrays.
# You can use the joblib.dump() function to save the model, and the joblib.load() function to load it later.

from joblib import dump, load

# Save the model to a file
dump(model, 'model.joblib')

# Load the model from a file
loaded_model = load('model.joblib')
