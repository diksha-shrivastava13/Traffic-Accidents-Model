# Import Needed Libraries
import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel

# FastAPI libray
from fastapi import FastAPI

# Initiate app instance
app = FastAPI(title='Monthly Traffic Accidents', version='1.0',
              description='XGBoost model is used for prediction')

# Initialize model artifact files. This will be loaded at the start of FastAPI model server.
regressor = joblib.load('..models/model.joblib')
one_hot_encoder = joblib.load('..models/one_hot_encoder.joblib')
features = joblib.load('..models/features.joblib')
categorical_features = joblib.load('../models/categorical_features.joblib')


"""This structure will be used for Json validation.
With just that Python type declaration, FastAPI will perform below operations on the request data
1) Read the body of the request as JSON.
2) Convert the corresponding types (if needed).
3) Validate the data.If the data is invalid, it will return a nice and clear error,
indicating exactly where and what was the incorrect data.
"""


class Data(BaseModel):
    year: int
    month: int
    category: str
    type: str


# Api root or home endpoint
@app.get('/')
@app.get('/home')
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {'message': 'System is healthy'}


# ML API endpoint for making prediction against the request received from client
@app.post("/predict")
def predict(data: Data):
    # Extract data in correct order
    data_dict = data.model_dump()
    data_df = pd.DataFrame.from_dict(data_dict)
    # Select features required for making prediction
    data_df = data_df[features]
    # Perform label encoding for categorical features
    data_df[categorical_features] = le.transform(data_df[categorical_features])
    # Create prediction
    prediction = clf.predict(data_df)
    # Map prediction to appropriate label
    prediction_label = ['Placed' if label == 0 else 'Not Placed' for label in prediction]
    # Return response back to client
    return {"prediction": prediction_label}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
