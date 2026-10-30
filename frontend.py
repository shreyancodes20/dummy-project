import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"  # your FastAPI server

st.set_page_config(page_title="Student Pass/Fail Predictor", page_icon="🎓")
st.title("🎓 Student Pass/Fail Predictor")
st.write("Enter the student's details and the model will predict the result.")

# ---- Input form ----
study_hours = st.slider("Study hours per day", 0.0, 24.0, 5.0, step=0.5)
attendance = st.slider("Attendance (%)", 0.0, 100.0, 80.0, step=1.0)
previous_score = st.slider("Previous exam score", 0.0, 100.0, 60.0, step=1.0)
study_mode = st.selectbox("Study mode", ["self", "coaching", "group"])

# ---- Predict ----
if st.button("Predict"):
    payload = {
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_score": previous_score,
        "study_mode": study_mode,
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        result = response.json()

        if response.status_code == 200:
            prediction = result["predicted_category"]
            if prediction == "Pass":
                st.success(f"Prediction: {prediction} ✅")
            else:
                st.error(f"Prediction: {prediction} ❌")

            st.subheader("Confidence")
            for label, prob in result["probabilities"].items():
                st.write(f"{label}: {prob:.0%}")
                st.progress(prob)
        else:
            st.error(f"API error: {result}")

    except requests.exceptions.ConnectionError:
        st.error("Can't reach the API. Start it first with: uvicorn main:app --reload")
    except Exception as e:
        st.error(f"Something went wrong: {e}")