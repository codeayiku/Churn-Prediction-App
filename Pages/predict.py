import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Set the title of the app
st.set_page_config(page_title="Customer Churn Prediction - Predict", layout="wide")

# Prediction Page Content
st.title("🤖 Predict Customer Churn")

# Load the trained model and preprocessor
model = joblib.load('model/forest_model.joblib')
preprocessor = joblib.load('model/preprocessor.pkl')  # Ensure this is the path to your preprocessor

# Collect user input from the sidebar
st.sidebar.write("### Enter Customer Details")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
tenure = st.sidebar.number_input("Tenure (months)", min_value=0, max_value=72, value=24)
phone_service = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_backup = st.sidebar.selectbox("Online Backup", ["No", "Yes", "No internet service"])
device_protection = st.sidebar.selectbox("Device Protection", ["No", "Yes", "No internet service"])
tech_support = st.sidebar.selectbox("Tech Support", ["No", "Yes", "No internet service"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", min_value=0.0, max_value=120.0, value=50.0)
total_charges = st.sidebar.number_input("Total Charges ($)", min_value=0.0, max_value=9000.0, value=1200.0)

# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'customerID': ['placeholder'],  # Add placeholder for customerID
    'gender': [gender],
    'SeniorCitizen': [1 if senior_citizen == "Yes" else 0],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
})

# Preprocess the input data
input_data_preprocessed = preprocessor.transform(input_data)

# Predict churn
if st.button("Predict"):
    prediction = model.predict(input_data_preprocessed)
    probability = model.predict_proba(input_data_preprocessed)
    st.write(f"### Prediction: {'Churn' if prediction[0] else 'No Churn'}")
    st.write(f"### Probability of Churn: {probability[0][1]:.2f}")
