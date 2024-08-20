# dashboard.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('data/train.csv')

# Set the title of the app
st.set_page_config(page_title="Customer Churn Prediction - Dashboard", layout="wide")

# Dashboard Page Content
st.title("📈 Dashboard")

# Load data
df = pd.read_csv("data/train.csv")

# Visualization: Distribution of Churn
st.write("### Churn Distribution")
fig, ax = plt.subplots()
sns.countplot(x='Churn', data=df, ax=ax)
st.pyplot(fig)

# Visualization: Tenure vs. Monthly Charges
st.write("### Tenure vs. Monthly Charges")
fig, ax = plt.subplots()
sns.scatterplot(x='tenure', y='MonthlyCharges', hue='Churn', data=df, ax=ax)
st.pyplot(fig)


# Visualization: Average Monthly Charges by Churn
st.write("### Average Monthly Charges by Churn")
fig, ax = plt.subplots()
sns.countplot(x='Churn', data=df, ax=ax)
st.pyplot(fig)


# Contract vs Churn
st.write("### Churn Rate by Contract Type")
contract_churn = train.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
contract_churn['Churn Rate'] = contract_churn['Yes'] * 100
fig, ax = plt.subplots()
sns.barplot(x=contract_churn.index, y='Churn Rate', data=contract_churn, ax=ax)
ax.set_title('Churn Rate by Contract Type')
st.pyplot(fig)

# Churn by Contract Type and Paperless Billing
st.write("### Churn by Contract Type")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=train, x='Contract', hue='Churn', palette={'Yes':'pink', 'No':'skyblue'}, ax=ax)
ax.set_title('Churn by Contract Type')
st.pyplot(fig)

# Churn by Paperless Billing
st.write("### Churn by Paperless Billing")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=train, x='PaperlessBilling', hue='Churn', palette={'Yes':'pink', 'No':'skyblue'}, ax=ax)
ax.set_title('Churn by Paperless Billing')
st.pyplot(fig)

# Internet Service vs Churn
st.write("### Churn Rate by Internet Service")
internet_churn = train.groupby('InternetService')['Churn'].value_counts(normalize=True).unstack()
internet_churn['Churn Rate'] = internet_churn['Yes'] * 100
fig, ax = plt.subplots()
sns.barplot(x=internet_churn.index, y='Churn Rate', data=internet_churn, ax=ax)
ax.set_title('Churn Rate by Internet Service')
st.pyplot(fig)

# Churn by Internet Service Type
st.write("### Churn by Internet Service Type")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=train, x='InternetService', hue='Churn', palette={'Yes':'pink', 'No':'skyblue'}, ax=ax)
ax.set_title('Churn by Internet Service Type')
st.pyplot(fig)

# Tenure vs Churn
st.write("### Tenure Distribution by Churn")
fig, ax = plt.subplots()
sns.violinplot(data=train, x='Churn', y='tenure', palette={'Yes':'pink', 'No':'skyblue'}, ax=ax)
ax.set_title('Tenure Distribution by Churn')
st.pyplot(fig)

# Churn by Tenure Bins
st.write("### Churn by Tenure Bins")
fig, ax = plt.subplots(figsize=(12, 6))
sns.countplot(data=train, x='tenure_bins', hue='Churn', palette={'Yes':'pink', 'No':'skyblue'}, ax=ax)
ax.set_title('Churn by Tenure Bins')
st.pyplot(fig)

# Churn by Gender and Senior Citizen Status
st.write("### Churn by Gender")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=train, x='gender', hue='Churn', palette={'Yes':'pink', 'No':'skyblue'}, ax=ax)
ax.set_title('Churn by Gender')
st.pyplot(fig)

st.write("### Churn by Senior Citizen Status")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=train, x='SeniorCitizen', hue='Churn', palette={'Yes':'pink', 'No':'skyblue'}, ax=ax)
ax.set_title('Churn by Senior Citizen Status')
st.pyplot(fig)


# Violin Plot for Tenure by Churn
st.write("### Violin Plot for Tenure by Churn")
fig, ax = plt.subplots(figsize=(10, 6))
sns.violinplot(data=train, x='Churn', y='tenure', palette={'Yes':'pink', 'No':'skyblue'}, ax=ax)
ax.set_title('Tenure Distribution by Churn')
st.pyplot(fig)