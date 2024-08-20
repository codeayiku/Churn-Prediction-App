# Import Libraries
import streamlit as st
from PIL import Image

# Set the title of the app
st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

# Add an image from URL
image_url = "https://www.retently.com/wp-content/uploads/2015/11/leading-causes-of-churn-1.png"
st.image(image_url, caption='Leading Causes of Customer Churn', use_column_width=True)


# Home Page Content
st.title("📡 Customer Churn Prediction App")

st.write("""
Welcome to the Customer Churn Prediction App! This tool allows the marketing team to predict the likelihood of customer churn using a machine learning model. 
Use the navigation on the left to explore the data, visualize insights, and predict churn.
""")

# Section: About Customer Churn
st.header("🔍 What is Customer Churn?")
st.write("""
Customer churn, also known as customer attrition, refers to the phenomenon where customers stop doing business with a company or brand. 
This is a critical metric for companies to track, as high churn rates can significantly impact revenue and growth. 
By predicting which customers are likely to churn, businesses can take proactive measures to retain them.
""")

# Section: Key Features of the Dataset
st.header("📊 Key Features of the Dataset")
st.write("""
1. **Tenure**: The number of months a customer has stayed with the company.
2. **Monthly Charges**: The amount charged to the customer per month.
3. **Total Charges**: The total amount charged to the customer.
4. **Contract**: The type of contract the customer has (e.g., month-to-month, one year, two years).
5. **Internet Service**: The type of internet service the customer has (e.g., DSL, Fiber optic).
6. **Payment Method**: The payment method used by the customer (e.g., electronic check, mailed check).
7. **Senior Citizen**: Whether the customer is a senior citizen (1) or not (0).
8. **Gender**: The gender of the customer.
""")

# Section: App Features
st.header("⚙️ App Features")
st.write("""
- **Data Overview**: Provides a detailed view of the dataset being used, including summary statistics.
- **Dashboard**: Offers interactive visualizations to explore the relationship between different features and customer churn.
- **Prediction**: Allows users to input customer details and predict the likelihood of churn using a trained machine learning model.
- **Interactive Insights**: Gain deeper insights into factors influencing churn through various data visualizations.
""")

# Section: User Benefits
st.header("🌟 User Benefits")
st.write("""
- **Proactive Decision-Making**: Identify at-risk customers and take action to retain them before they churn.
- **Data-Driven Insights**: Leverage the power of data to understand the factors driving customer churn.
- **User-Friendly Interface**: Easy-to-use application with intuitive navigation and visualizations.
""")

# Section: How to Run the Application
st.header("🚀 How to Run the Application")
st.write("""
1. **Clone the Repository**: 
   - Clone the GitHub repository containing the application code.
   
2. **Install Dependencies**: 
   - Use `pip` to install the required Python packages as specified in the `requirements.txt` file.
   
3. **Run the Application**: 
   - Execute the application using Streamlit by running the command `streamlit run app.py` in your terminal.
   
4. **Navigate the App**: 
   - Use the sidebar to navigate between the Home, Data, Dashboard, and Predict pages.
""")

# Section: Machine Learning Integration
st.header("🤖 Machine Learning Integration")
st.write("""
This app integrates a machine learning model to predict customer churn. The model was trained on a historical customer dataset and uses features like tenure, 
monthly charges, and total charges to predict whether a customer is likely to churn. The prediction feature allows for real-time customer churn predictions, 
enabling businesses to take timely actions to reduce churn.
""")

# Add an image from URL
image_url = "https://www.retently.com/wp-content/uploads/2015/11/leading-causes-of-churn-1.png"
st.image(image_url, caption='Leading Causes of Customer Churn', use_column_width=True)

# Add social media links
st.markdown("""
**Connect with me:**

- [GitHub](https://github.com/your-username)
- [LinkedIn](https://www.linkedin.com/in/your-username)
- [Medium](https://medium.com/@your-username)
""")
