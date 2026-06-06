import streamlit as st

st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Diabetes Prediction Using Machine Learning")

st.markdown("### Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=25)

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=22.5
    )

    hypertension = st.selectbox(
        "Hypertension",
        ["No", "Yes"]
    )

with col2:
    glucose = st.number_input(
        "Blood Glucose Level",
        min_value=50.0,
        max_value=300.0,
        value=90.0
    )

    hba1c = st.number_input(
        "HbA1c Level",
        min_value=3.0,
        max_value=15.0,
        value=5.2
    )

    smoking = st.selectbox(
        "Smoking History",
        ["never", "former", "current"]
    )

    heart_disease = st.selectbox(
        "Heart Disease",
        ["No", "Yes"]
    )

st.write("")

if st.button("🔍 Predict Diabetes"):

    risk_score = 0

    if glucose >= 126:
        risk_score += 1

    if hba1c >= 6.5:
        risk_score += 1

    if bmi >= 30:
        risk_score += 1

    if hypertension == "Yes":
        risk_score += 1

    if heart_disease == "Yes":
        risk_score += 1

    if age >= 45:
        risk_score += 1

    st.write("")
    st.subheader("Prediction Result")

    if risk_score >= 2:
        st.error("🔴 High Diabetes Risk")
    else:
        st.success("🟢 No Diabetes Detected")

    st.write("")
    st.subheader("Patient Summary")

    st.write(f"Age: {age}")
    st.write(f"BMI: {bmi}")
    st.write(f"Blood Glucose: {glucose}")
    st.write(f"HbA1c Level: {hba1c}")