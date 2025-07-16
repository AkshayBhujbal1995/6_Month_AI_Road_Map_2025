import streamlit as st
import pickle
import numpy as np

# Load the saved transformer and model
with open("poly_transformer.pkl", "rb") as f1:
    poly_transformer = pickle.load(f1)

with open("poly_model.pkl", "rb") as f2:
    poly_model = pickle.load(f2)

# Streamlit UI
st.markdown("<h1 style='color:#4b8bff;'> Polynomial Regression Salary Predictor</h1>", unsafe_allow_html=True)
st.write("Enter the Position Level to predict the corresponding salary using a trained Polynomial Regression model (Degree 5).")

level = st.slider("Select Position Level", min_value=1.0, max_value=10.0, step=0.1)

if st.button("💡 Predict Salary"):
    input_array = np.array([[level]])
    transformed_input = poly_transformer.transform(input_array)
    prediction = poly_model.predict(transformed_input)
    st.success(f"Predicted Salary for Level {level}: ₹ {prediction[0]:,.2f}")
