
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("salary_model.pkl")

st.title("💼 Employee Salary Prediction")

age = st.number_input("Enter Age", 18, 100)
hours = st.number_input("Working Hours per Week", 1, 100)
education = st.selectbox("Education", ["Bachelors", "HS-grad", "Masters", "Some-college"])
occupation = st.selectbox("Occupation", ["Sales", "Exec-managerial", "Prof-specialty", "Craft-repair"])

if st.button("Predict Salary"):
    data = pd.DataFrame([{
        "age": age,
        "hours_per_week": hours,
        "education": education,
        "occupation": occupation
    }])
    prediction = model.predict(data)[0]
    result = ">50K" if prediction == 1 else "<=50K"
    st.success(f"Predicted Salary: {result}")
