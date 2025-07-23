from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from collections import defaultdict
import numpy as np
import joblib
import os

app = FastAPI()

# Load model (adjust MODEL_PATH to your actual model file location)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "xgb_model.joblib")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Failed to load model: {e}")
    model = None

patient_history = defaultdict(list)

class PatientVitals(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    resp_rate: int
    temperature: float

@app.get("/")
def root():
    return {"message": "FastAPI server is running."}

@app.post("/stream")
def predict_risk(vitals: PatientVitals):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    features = np.array([[vitals.heart_rate, vitals.spo2, vitals.resp_rate, vitals.temperature]])
    try:
        risk = float(model.predict_proba(features)[0][1])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model prediction error: {e}")

    record = {
        "patient_id": vitals.patient_id,
        "heart_rate": vitals.heart_rate,
        "spo2": vitals.spo2,
        "resp_rate": vitals.resp_rate,
        "temperature": vitals.temperature,
        "risk_score": round(risk, 2)
    }
    patient_history[vitals.patient_id].append(record)
    return record

@app.get("/patients")
def get_all_patients():
    latest_records = []
    for patient_id, records in patient_history.items():
        if records:
            latest_records.append(records[-1])  # latest record
    return latest_records

@app.get("/patients/history/{patient_id}")
def get_patient_history(patient_id: str):
    return patient_history.get(patient_id, [])
