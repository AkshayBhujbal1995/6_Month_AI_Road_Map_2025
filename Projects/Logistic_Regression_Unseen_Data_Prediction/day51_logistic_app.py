import streamlit as st
import numpy as np
import pickle

# 🎯 Load the trained model and scaler
with open("model2.pkl", "rb") as f:
    model2 = pickle.load(f)

with open("scaler2.pkl", "rb") as f:
    scaler2 = pickle.load(f)

# 📘 Updated Title
st.title("📊 Logistic Regression on Unseen Data")

st.markdown("### 🔽 Enter Details Below")

# ⌨️ Manual Inputs
age = st.number_input("Enter Age", min_value=18, max_value=100, value=30, step=1)
salary = st.number_input("Enter Estimated Salary", min_value=10000, max_value=150000, value=50000, step=1000)

# 🚀 Predict Button
if st.button("Predict"):
    user_input = np.array([[age, salary]])
    scaled_input = scaler2.transform(user_input)
    prediction = model2.predict(scaled_input)

    if prediction[0] == 1:
        st.success("✅ Prediction: Will Purchase")
    else:
        st.error("❌ Prediction: Will NOT Purchase")
