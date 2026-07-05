# Real Estate Price Prediction API

Welcome to the **Real Estate Price Prediction** repository! This project builds and serves a Machine Learning model trained on the California Housing dataset to predict median housing prices.

The project is structured with a modular directory layout where the model is served via a **FastAPI** web service.

> [!NOTE]
> **Model Training & Step-by-Step Tuning:**
> This repository is a learning project where different ML algorithms and hyperparameter tuning techniques are evaluated step-by-step. The current model is a working prototype. The objective is to incrementally refine feature engineering, pipelines, and algorithms to continuously reduce the Root Mean Squared Error (RMSE) score.

---

## 🛠️ Tech Stack & Dependencies

The project is built using:
- **Language:** Python
- **API Framework:** [FastAPI](https://fastapi.tiangolo.com/) (served using [Uvicorn](https://www.uvicorn.org/))
- **Machine Learning & Pipeline:** [Scikit-Learn](https://scikit-learn.org/)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **Serialization:** [Joblib](https://joblib.readthedocs.io/)
- **Data Validation:** [Pydantic](https://docs.pydantic.dev/)

---

## 📁 Repository Structure

Here is an overview of the key directories and files in this repository:

* **[app/](file:///D:/coding/realestatecompany/app)** - FastAPI application source code.
  * **[main.py](file:///D:/coding/realestatecompany/app/main.py)** - Entry point of the FastAPI application. Defines the endpoints (`/` and `/predict`).
  * **[schemas.py](file:///D:/coding/realestatecompany/app/schemas.py)** - Contains [UserInput](file:///D:/coding/realestatecompany/app/schemas.py#L2) Pydantic schema for request validation.
  * **[predictor.py](file:///D:/coding/realestatecompany/app/predictor.py)** - Loads the serialized joblib model and exposes the prediction helper.
  * **[custom_transformers.py](file:///D:/coding/realestatecompany/app/custom_transformers.py)** - Implements custom Scikit-Learn transformers (e.g., [ClusterSimilarity](file:///D:/coding/realestatecompany/app/custom_transformers.py#L10)) used in the model preprocessing pipeline.
  * **[model/housing_prediction_model.pkl](file:///D:/coding/realestatecompany/app/model/housing_prediction_model.pkl)** - The serialized Scikit-Learn pipeline/model.
* **[datasets/](file:///D:/coding/realestatecompany/datasets)** - Contains raw data used for modeling.
  * **[housing/housing.csv](file:///D:/coding/realestatecompany/datasets/housing/housing.csv)** - The California Housing dataset.
* **[requirements.txt](file:///D:/coding/realestatecompany/requirements.txt)** - Package dependencies to run both the notebooks and the API.
* **[best.ipynb](file:///D:/coding/realestatecompany/best.ipynb)** & **[test.ipynb](file:///D:/coding/realestatecompany/test.ipynb)** - Jupyter notebooks used for data exploration, model experimentation, engineering features, and tracking RMSE results.

---

## 🚀 Local Setup & Installation

Follow these steps to clone the repository and run the API service locally:

### 1. Clone the Repository
```bash
git clone <repository_url>
cd realestatecompany
```

### 2. Set Up a Virtual Environment
It is highly recommended to run this in a virtual environment to manage dependencies properly:

* **On Windows:**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
* **On macOS/Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Dependencies
Install all required libraries specified in the [requirements.txt](file:///D:/coding/realestatecompany/requirements.txt):
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Application
Start the Uvicorn local development server from the project root:
```bash
uvicorn app.main:app --reload
```
Once started, the API will be accessible at: `http://127.0.0.1:8000`

---

## 🐳 Running with Docker

As an alternative to manual setup, you can build and run the application inside a Docker container. This ensures that the application runs in an isolated environment with all correct package dependencies pre-installed.

### 1. Build the Docker Image
Navigate to the root directory containing the [Dockerfile](file:///D:/coding/realestatecompany/Dockerfile) and run:
```bash
docker build -t real-estate-prediction-api .
```

### 2. Run the Docker Container
Start the container and map port `8000` of the container to port `8000` on your host machine:
```bash
docker run -p 8000:8000 real-estate-prediction-api
```
The API will then be available at `http://127.0.0.1:8000`.

---


## 📡 API Endpoints

### 1. Health Check
Checks if the web server is online and running.

* **Method:** `GET`
* **Path:** `/`
* **Response:**
  ```json
  {
    "message": "Server is Running..."
  }
  ```

### 2. Predict House Price
Predicts the estimated median housing price based on the input housing features.

* **Method:** `POST`
* **Path:** `/predict`
* **Request Body (JSON):**
  
  Must conform to the [UserInput](file:///D:/coding/realestatecompany/app/schemas.py#L2) schema:
  
  | Field | Type | Validation Rules | Description |
  | :--- | :--- | :--- | :--- |
  | `longitude` | float | None | Longitude coordinate |
  | `latitude` | float | None | Latitude coordinate |
  | `housing_median_age` | int | Must be `> 0` | Median age of the house |
  | `total_rooms` | int | Must be `> 0` | Total number of rooms in the block |
  | `total_bedrooms` | int | Must be `> 0` | Total number of bedrooms in the block |
  | `population` | int | Must be `> 0` | Total population in the block |
  | `households` | int | Must be `> 0` | Total households in the block |
  | `median_income` | float | Must be `> 0` | Median income of households (in tens of thousands) |
  | `ocean_proximity` | string | Case-insensitive | Proximity to ocean. Valid options: `"NEAR BAY"`, `"<1H OCEAN"`, `"INLAND"`, `"NEAR OCEAN"`, `"ISLAND"` |

  **Sample Request Payload:**
  ```json
  {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 120,
    "median_income": 8.3252,
    "ocean_proximity": "NEAR BAY"
  }
  ```

* **Sample Response (JSON):**
  ```json
  {
    "Estimated Housing Price": 452600.0
  }
  ```

---

## 🧪 Testing the API

### Testing with Postman
1. Create a new request in Postman.
2. Set the method to **POST** and the URL to `http://127.0.0.1:8000/predict`.
3. Go to the **Body** tab, choose **raw**, and select **JSON** as the format.
4. Paste the sample request payload (from above) and click **Send**.

### Testing with cURL
You can also test directly from your command line:
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d "{\"longitude\": -122.23, \"latitude\": 37.88, \"housing_median_age\": 41, \"total_rooms\": 880, \"total_bedrooms\": 129, \"population\": 322, \"households\": 120, \"median_income\": 8.3252, \"ocean_proximity\": \"NEAR BAY\"}"
```

### Interactive API Docs (Swagger UI)
FastAPI automatically generates interactive API documentation. Start the server and visit:
* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **Redoc:** `http://127.0.0.1:8000/redoc`

---
