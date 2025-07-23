import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model_serving", "xgb_model.joblib")

model = joblib.load(MODEL_PATH)

sample = [[80, 95, 20, 37.0]]

print(model.predict_proba(sample))
