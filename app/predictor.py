import joblib
from pandas import DataFrame

class Predictor():

    prediction_model = joblib.load("app/model/housing_prediction_model.pkl")

    @classmethod
    def predict(self, input_data: DataFrame):
        return self.prediction_model.predict(input_data)[0]
    

prediction_model = Predictor