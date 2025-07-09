import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open(
    r'd:\\Full stack Data Science course\\VS Code\\ML\\Regression\\Simple Linear Regresaion\\linear_regression_model.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="AI Jobs Salary Estimator – India", layout="centered")

# --- Custom Styling (Vibrant & Modern) ---
st.markdown("""
    <style>
        html, body, .main {
            background-color: #fdf5fd;
            color: #222;
        }
        .title-container {
            text-align: center;
            padding: 30px 0 10px 0;
        }
        .title-container h1 {
            font-size: 42px;
            color: #8e24aa;
            font-family: 'Segoe UI', sans-serif;
        }
        .subtitle {
            color: #444;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .estimate-box {
            background: linear-gradient(145deg, #ffe0f7, #d1c4e9);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: 600;
            color: #4a148c;
            border: 2px solid #ce93d8;
            box-shadow: 0 8px 18px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #8e24aa;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 30px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header with Smaller GIF ---
st.markdown("""
    <div class="title-container">
        <img src="https://media.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="100">
        <h1>AI Jobs Salary Estimator – India</h1>
        <p class="subtitle">
            Predict your potential salary in India's booming AI & Machine Learning job market.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- Input Section ---
st.header("How much experience do you have in AI/ML?")
years = st.slider("Select your total years of professional experience:", 0.0, 50.0, 2.0, step=0.5)

# --- Salary Prediction ---
if st.button("💼 Estimate My AI Job Salary"):
    prediction = model.predict(np.array([[years]]))
    lower = prediction[0] - 5000
    upper = prediction[0] + 5000

    st.markdown(f"""
        <div class='estimate-box'>
            📈 Estimated Annual AI Job Salary: ₹{prediction[0]:,.0f}<br>
            💡 Typical Range: ₹{lower:,.0f} – ₹{upper:,.0f}
        </div>
    """, unsafe_allow_html=True)

# --- Expanders ---
with st.expander("About This AI Salary Tool"):
    st.markdown("""
    This tool is powered by a trained machine learning model (Simple Linear Regression)
    and predicts **AI & ML job salaries** based on your professional experience.

    Great for learners, professionals, and analysts exploring AI careers in India.
    """)

with st.expander("AI/ML Salary Ranges in India"):
    st.markdown("""
    - **AI Intern / Junior (0–2 yrs):** ₹6 LPA – ₹12 LPA  
    - **ML Engineer / Data Scientist (2–5 yrs):** ₹12 LPA – ₹25 LPA  
    - **Senior AI Specialist (5–10 yrs):** ₹25 LPA – ₹45 LPA  
    - **AI Director / Principal (10+ yrs):** ₹45 LPA – ₹1 Cr+  
    """)

# --- Footer with Working GIF ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align:center; font-size:14px; color:#777;'>
        Created for AI career insights | Powered by Machine Learning & Streamlit
    </div>
    <div style='text-align:center; margin-top:10px;'>
        <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="100">
    </div>
""", unsafe_allow_html=True)
