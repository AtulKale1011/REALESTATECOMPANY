import os
import joblib
from pandas import DataFrame
from dotenv import load_dotenv

load_dotenv()

class Predictor():

    prediction_model = joblib.load(f"{os.getenv("Model_Path")}")

    @classmethod
    def predict(self, input_data: DataFrame):
        return self.prediction_model.predict(input_data)[0]
    

prediction_model = Predictor