# 🏥 ICU Patient Deterioration Monitor (Live)

A real-time ICU patient monitoring system that uses FastAPI and Streamlit to predict and visualize the risk of patient deterioration using live vitals data.

---

## 🚀 Features

- ⚙️ **FastAPI backend** with machine learning model for risk prediction
- 📊 **Streamlit dashboard** to display patient risk levels and vitals
- 🔁 **Simulated patient vitals** continuously sent to the API
- 📈 **Risk scoring** using pre-trained model (e.g., logistic regression)
- 🔍 Patient history and real-time vitals visualization

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- scikit-learn / ML model
- pandas / NumPy
- RESTful APIs
- Requests

---

## 🧪 Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/MaheshDollu/ICU-Patient-Deterioration-Monitor-Live-.git
cd ICU-Patient-Deterioration-Monitor-Live-

2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
3. Install Requirements

pip install -r requirements.txt
4. Run FastAPI Backend

cd model_serving
uvicorn api:app --reload
The API runs at: http://localhost:8000

5. Run Streamlit Dashboard
In a new terminal:


streamlit run dashboard.py
The dashboard will be live at: http://localhost:8501

6. Simulate Live Patient Data
In another terminal:


python simulate_patients.py
Vitals will be sent to the backend every 5 seconds and the dashboard will reflect updates.

📁 Project Structure

ICU-Patient-Deterioration-Monitor-Live-/
├── model_serving/
│   ├── api.py              # FastAPI app with ML model
│   ├── model.pkl           # Trained model
├── dashboard.py            # Streamlit frontend
├── simulate_patients.py    # Script to simulate live vitals
├── requirements.txt
└── README.md
🧠 ML Model Assumption
The model predicts the probability of deterioration using vitals:

Heart Rate

SpO2

Respiratory Rate

Temperature

📬 API Endpoints
POST /stream – Receive patient vitals and return risk score

GET /patients – Get list of latest patients

GET /patients/history/{patient_id} – Get vitals + risk history


