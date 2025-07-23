import requests

url = "http://localhost:8000/stream"
data = {
    "patient_id": "test123",
    "heart_rate": 85,
    "spo2": 92,
    "resp_rate": 22,
    "temperature": 37.8
}

res = requests.post(url, json=data)
print(res.status_code)
print(res.json())
