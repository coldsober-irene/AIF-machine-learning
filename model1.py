from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, RandomForestRegressor, BaggingRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
import os

# config pandas for custom setting
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 300)

class read_data:
    def __init__(self, filename, ext = "csv", conn = None, querry = None):
        """conn: connection of the database,
        querry: this the database querry such as SELECT * FROM MYTABLE"""
        self.ext = ext
        self.file = filename
        self.conn = conn
        self.querry = querry

    def get_data(self):
        if str(self.ext).lower() == "csv":
            return pd.read_csv(self.file)
        elif str(self.ext).lower() == "xlsx":
            return pd.read_excel(self.file)
        elif str(self.ext).lower() == "txt":
            return pd.read_table(self.file, sep="\t")
        elif str(self.ext).lower() == ".db":
            return pd.read_sql(self.conn, self.querry)

class do_ml:
    def __init__(self, model, x_data, y_data):
        self.model = model
        self.x_data = x_data
        self.y_data = y_data
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x_data, self.y_data, test_size=.2)

    def model_obj(self):
        if self.model == "LinearRegression":
            return LinearRegression().fit(self.x_train, self.y_train)
        elif self.model == "LogisticRegression":
            return LogisticRegression().fit(self.x_train, self.y_train)
        elif self.model == "RandomForestRegressor":
            return RandomForestRegressor().fit(self.x_train, self.y_train)
        elif self.model == "RandomForestClassifier":
            return RandomForestClassifier().fit(self.x_train, self.y_train)

    def make_prediction_and_score(self):
        model = self.model_obj(self.x_train, self.y_train)
        y_pred = model.predict(self.x_test)
        score = accuracy_score(self.y_test, y_pred)
        return model, score

    def save_model(self, path = None, model_name = None):
        full_path = "my_model"
        if path and model_name:
            full_path =  os.path.join(path, model_name)
        with open(f"{full_path}.pkl", "wb") as file:
            pickle.dump(self.model_obj(), file)

    def load_model(self, full_path):
        with open(full_path, "rb") as f:
            return pickle.load(f)

    def forecast(self, x):
        """if it is multiple regression, the shape of x should do of 2D [[]]"""
        model, _ = self.make_prediction_and_score()
        return model.predict(x)

