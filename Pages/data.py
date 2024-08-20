# data.py
import streamlit as st
import pandas as pd

# Set the title of the app
st.set_page_config(page_title="Customer Churn Prediction - Data Overview", layout="wide")

# Data Page Content
st.title("📊 Data Overview")

# Load data
df = pd.read_csv("data/train.csv")

# Display the dataframe
st.dataframe(df.head(10))

# Add some summary statistics
st.write("### Summary Statistics")
st.write(df.describe())
