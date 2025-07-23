from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

# Load your ML model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "xgb_model.joblib")
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Model loading failed: {e}")
    model = None

class Vitals(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    resp_rate: int
    temperature: float

@app.get("/")
def root():
    return {"message": "FastAPI server is running."}

@app.post("/stream")
def receive_vitals(vitals: Vitals):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    try:
        X = [[vitals.heart_rate, vitals.spo2, vitals.resp_rate, vitals.temperature]]
        risk_prob = model.predict_proba(X)[0][1]
        return {"patient_id": vitals.patient_id, "risk_score": risk_prob}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
