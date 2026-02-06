# FastAPI app that receives 5 sensor values and returns the Decision Tree prediction.

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load trained model once when API starts
model = joblib.load("decision_tree_model.joblib")

app = FastAPI(title="3W Sensor Prediction API")

# Request body schema
class SensorInput(BaseModel):
    P_PDG: float
    T_TPT: float
    P_TPT: float
    T_JUS_CKP: float
    P_MON_CKP: float


@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: SensorInput):
    # Convert input to model format
    user_input = np.array([[
        data.P_PDG,
        data.T_TPT,
        data.P_TPT,
        data.T_JUS_CKP,
        data.P_MON_CKP
    ]])

    prediction = model.predict(user_input)

    return {
        "prediction": int(prediction[0])
    }
