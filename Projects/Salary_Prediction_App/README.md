
# 💼 Salary Prediction App using Simple Linear Regression (SLR)

📅 **Date:** July 9, 2025  
📁 **Project:** Day40_Deploying_SLR_with_Streamlit  
🌐 **Deployment:** Streamlit Web App

---

## 🎯 Objective

This project demonstrates an end-to-end machine learning pipeline to **predict salary based on years of experience** using **Simple Linear Regression**. It includes:

- Training a regression model
- Performing detailed statistical analysis
- Saving the model using `pickle`
- Deploying a user-friendly **Streamlit app** for interactive predictions

---

## 🧠 What You'll Learn

- Data preparation, model training, and testing
- Key regression evaluation metrics (R², SSE, SSR, SST, MSE)
- Deep statistical understanding (mean, SEM, CV, skewness, z-score, etc.)
- End-to-end app deployment using **Streamlit**

---

## 🛠️ Technologies Used

- `Python`, `Pandas`, `NumPy`
- `Matplotlib`, `Seaborn` for visuals
- `Scikit-learn` for regression modeling
- `Pickle` for model saving
- `Streamlit` for frontend deployment

---

## 📁 Dataset Overview

- 📂 **File Used:** `Salary_Data.csv`
- 📈 **Features:**
  - `YearsExperience` – Independent variable
  - `Salary` – Target variable

---

## ⚙️ Pipeline Overview

### ✅ Data Analysis & Model Building

1. **EDA (Exploratory Data Analysis)**
   - Check for missing values
   - Correlation matrix
   - Descriptive stats (mean, median, std, skewness, etc.)

2. **Model Training**
   - Train-Test Split (80/20)
   - Fit using `LinearRegression()`
   - Evaluate with R², MSE, SSR, SSE, SST

3. **Prediction**
   - Predict salary for 12 and 20 years of experience
   - Plot regression line and actual values

4. **Statistical Insights**
   - Coefficient of Variation (CV)
   - Skewness & SEM
   - Z-score normalization
   - Degrees of Freedom

---

## 📦 Model Serialization

- Trained model is saved using:
  ```python
  pickle.dump(regressor, open('linear_regression_model.pkl', 'wb'))

---

## 🌐 Streamlit Web App

### 🔧 How It Works

* Load the trained `.pkl` file
* Take user input (Years of Experience)
* Predict and display salary in real-time

### 📜 Streamlit Code Preview

```python
import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("linear_regression_model.pkl", "rb"))

# UI
st.title("💼 Salary Prediction App")
years_experience = st.number_input("Enter Years of Experience:", 0.0, 50.0, step=0.1)

if st.button("Predict Salary"):
    salary = model.predict([[years_experience]])
    st.success(f"Predicted Salary: ₹{salary[0]:,.2f}")
```

---

## 🚀 How to Run

1. Clone repo and navigate to project folder
2. Install dependencies:

   ```bash
   pip install streamlit scikit-learn pandas numpy

3. Run Streamlit app:

   ```bash
   streamlit run SLR_app1.py
  

---

## 📈 Evaluation Metrics

| Metric       | Value     |
| ------------ | --------- |
| R² Score     | 0.709     |
| Train MSE    | 36,149.67 |
| Test MSE     | 12,823.41 |
| Correlation  | 0.978     |
| CV (Salary)  | 0.3546    |
| SEM (Salary) | \~₹5005   |

---

## 📊 Visualizations

* Scatterplot (actual vs predicted)
* Regression Line
* Histogram with Mean, Median, Mode
* Boxplot by Category

---

## ✅ Conclusion

* Built a fully functional **salary prediction app** using **SLR**
* Integrated advanced **statistics** and **visualizations**
* Deployed model using **Streamlit** for real-world usage
* Gained insights into **model performance**, **distribution**, and **error analysis**

---

## 📦 Next Steps

* Add more features like education, location, etc.
* Try Polynomial or Random Forest Regression
* Deploy app on Streamlit Cloud or Hugging Face Spaces

---

> 👨‍💻 Built by [Akshay Bhujbal](https://www.linkedin.com/in/akshay-1995-bhujbal) with ❤️ for real-world AI deployment!
---
