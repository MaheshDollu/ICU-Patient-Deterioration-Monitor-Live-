import requests
import time
import random
import uuid

API_URL = "http://localhost:8000/stream"

def generate_vitals():
    return {
        "patient_id": str(uuid.uuid4())[:8],
        "heart_rate": random.randint(60, 130),
        "spo2": random.randint(85, 100),
        "resp_rate": random.randint(12, 30),
        "temperature": round(random.uniform(36.0, 40.0), 1),
    }

def send_vitals():
    while True:
        vitals = generate_vitals()
        try:
            response = requests.post(API_URL, json=vitals)
            if response.status_code == 200:
                print(f"Sent data for patient {vitals['patient_id']} — Risk: {response.json()['risk_score']:.2f}")
            else:
                print(f"Failed to send data: {response.status_code} {response.text}")
        except Exception as e:
            print(f"Error sending data: {e}")
        time.sleep(5)  # Send every 5 seconds

if __name__ == "__main__":
    send_vitals()
