import requests
import time
import uuid
import random

API_URL = "http://localhost:8000/stream"

def generate_vitals():
    return {
        "patient_id": str(uuid.uuid4()),
        "heart_rate": random.randint(60, 130),
        "spo2": random.randint(85, 100),
        "resp_rate": random.randint(12, 30),
        "temperature": round(random.uniform(36.0, 40.0), 1),
    }

while True:
    vitals = generate_vitals()
    try:
        response = requests.post(API_URL, json=vitals)
        if response.status_code == 200:
            print(f"Sent vitals for {vitals['patient_id']}")
        else:
            print(f"Failed to send data: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Error sending data: {e}")
    time.sleep(3)  # send every 3 seconds
