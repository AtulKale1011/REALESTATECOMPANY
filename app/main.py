from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from schemas import UserInput
from predictor import model as prediction_model
import pandas as pd

app = FastAPI()

@app.get('/')
def health_check():
    return {"message": "Server is Running..."}, status.HTTP_200_OK

@app.post('/predict')
def predict(request: UserInput):

    input_data = pd.DataFrame([request])

    estimated_prediction = prediction_model.predict(input_data)

    return JSONResponse(
        status_code=200,
        content={
            "Estimated Housing Price" : float(estimated_prediction[0])
        }
    )