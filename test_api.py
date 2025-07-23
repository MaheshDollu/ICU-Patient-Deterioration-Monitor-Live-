from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Vitals(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    resp_rate: int
    temperature: float

@app.post("/stream")
async def stream(vitals: Vitals):
    # Dummy risk score logic (just sum of vitals mod 1)
    risk_score = (vitals.heart_rate + vitals.spo2 + vitals.resp_rate + vitals.temperature) % 1
    return {"patient_id": vitals.patient_id, "risk_score": risk_score}
