import streamlit as st
import pickle
import numpy as np

# 🎯 Load the trained regression model
model = pickle.load(open(r'd:\Full stack Data Science course\VS Code\ML\Regression\Simple Linear Regresaion\linear_regression_model.pkl', 'rb'))

# 💡 App Title and Subtitle
st.markdown("<h1 style='color:#ff4b4b;'>💼 Salary Prediction App</h1>", unsafe_allow_html=True)
st.markdown("🚀 Predict salary based on years of experience using a pre-trained **Simple Linear Regression** model.", unsafe_allow_html=True)
st.markdown("---")

# 🎛️ Input: Years of Experience
st.markdown("### 📥 Enter Your Experience:")
years_experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=1.0, step=0.5)

# 🧮 Predict Salary
if st.button("📊 Predict Salary"):
    experience_input = np.array([[years_experience]])  # reshape to 2D
    prediction = model.predict(experience_input)
    
    # ✅ Show Prediction
    st.markdown(f"<h3 style='color:green;'>💰 Predicted Salary: ₹{prediction[0]:,.2f}</h3>", unsafe_allow_html=True)

# 📄 Model Info
st.markdown("---")
st.markdown("📝 **Model Details:**")
st.markdown("- Trained on salary vs years of experience dataset")
st.markdown("- Uses a Simple Linear Regression algorithm")
st.markdown("- Predicts continuous salary outcomes based on your input")

# 🎨 Footer
st.markdown("<hr style='border: 1px solid #bbb;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
