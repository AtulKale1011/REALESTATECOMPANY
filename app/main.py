from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from app.schemas import UserInput
from app.predictor import prediction_model
import pandas as pd

app = FastAPI()

@app.get('/')
def health_check():
    return {"message": "Server is Running..."}, status.HTTP_200_OK


@app.post('/predict')
def predict(request: UserInput):

    input_data = pd.DataFrame([{
        "longitude": request.longitude,
        "latitude": request.latitude,
        "housing_median_age": request.housing_median_age,
        "total_rooms": request.total_rooms,
        "total_bedrooms": request.total_bedrooms,
        "population": request.population,
        "households": request.households,
        "median_income": request.median_income,
        "ocean_proximity": request.ocean_proximity
    }])

    try:
        estimated_prediction = prediction_model.predict(input_data)

        return JSONResponse(
            status_code=200,
            content={
                "Estimated Housing Price" : float(estimated_prediction)
            }
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=e.message
        )