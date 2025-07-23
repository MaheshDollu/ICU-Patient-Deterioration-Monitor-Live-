import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="ICU Patient Monitor", layout="wide")
st.title("🏥 ICU Patient Deterioration Monitor (Live)")
import streamlit as st
import requests
import pandas as pd





API_BASE = "https://icu-patient-deterioration-monitor-live-3.onrender.com"

def fetch_latest():
    try:
        res = requests.get(f"{API_BASE}/patients")
        if res.status_code == 200:
            return pd.DataFrame(res.json())
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error fetching latest data: {e}")
        return pd.DataFrame()

def fetch_history(patient_id):
    try:
        res = requests.get(f"{API_BASE}/patients/history/{patient_id}")
        if res.status_code == 200:
            return pd.DataFrame(res.json())
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error fetching history for {patient_id}: {e}")
        return pd.DataFrame()

def risk_level(score):
    if score >= 0.8:
        return "🔴 Critical Risk"
    elif score >= 0.6:
        return "🟠 Moderate Risk"
    elif score >= 0.4:
        return "🟡 Low Risk"
    else:
        return "🟢 Normal"

placeholder = st.empty()

while True:
    df = fetch_latest()
    with placeholder.container():
        if df.empty:
            st.write("No patient data received yet.")
        else:
            # Show overall patient table
            st.dataframe(df)

            # Select patient for detailed view
            patient_ids = df['patient_id'].unique().tolist()
            selected_patient = st.selectbox("Select patient to view history", patient_ids)

            # Show patient history chart
            history_df = fetch_history(selected_patient)
            if not history_df.empty:
                st.line_chart(history_df.set_index(history_df.index)[['risk_score', 'heart_rate', 'spo2', 'resp_rate', 'temperature']])
            else:
                st.write("No history data available for this patient.")

            # Show risk alerts
            for _, row in df.iterrows():
                level = risk_level(row["risk_score"])
                if level == "🔴 Critical Risk":
                    st.error(f"🔥 CRITICAL ALERT: Patient {row['patient_id']} — Risk Score: {row['risk_score']:.2f}")
                    st.balloons()
                elif level == "🟠 Moderate Risk":
                    st.warning(f"⚠️ Moderate Risk: Patient {row['patient_id']} — Risk Score: {row['risk_score']:.2f}")
                elif level == "🟡 Low Risk":
                    st.info(f"ℹ️ Low Risk: Patient {row['patient_id']} — Risk Score: {row['risk_score']:.2f}")
                else:
                    st.success(f"✅ Normal: Patient {row['patient_id']} — Risk Score: {row['risk_score']:.2f}")

    time.sleep(5)
