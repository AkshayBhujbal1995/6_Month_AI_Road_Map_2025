
# 🏡 House Price Prediction Web App

**Machine Learning Regression Project | Flask Deployment**

Welcome to my **end-to-end machine learning project** that predicts house prices using multiple regression algorithms and evaluates their performance. The project includes **data preprocessing, model training, evaluation, and a user-friendly web application** to predict house prices based on user input.

---

### 📌 Project Highlights

* 🧠 **Tested 13 Regression Models**: Including Linear, Ridge, Lasso, Polynomial, Random Forest, XGBoost, and even an Artificial Neural Network (ANN).
* 📊 **Model Comparison**: Evaluated each model based on MAE, MSE, and R² Score.
* 🚀 **Top Performing Model**: `SGD Regressor` with **MAE: ₹82,567.49**, **R² Score: 0.9147**.
* 🌐 **Web App Built with Flask**: Clean two-page layout for input and output.
* 📦 **Pickled Model Deployed** for real-time predictions.
* ✅ No `static/` folder — keeping things minimal and lightweight.

---

### 🔍 Technologies Used

* Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
* Machine Learning (Supervised Regression)
* Flask (Web Framework)
* HTML (Frontend)
* Pickle (Model Serialization)

---

### 📁 Project Structure

```
project/
│
├── templates/
│   ├── index.html       # User Input Page
│   └── result.html      # Prediction Output Page
│
├── app.py               # Main Flask App
├── model.pkl            # Trained Model
├── House_Price_Prediction_Notebook.ipynb
├── requirements.txt     # Project Dependencies
└── README.md
```

---

### 🚀 How to Run Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/house-price-predictor.git
   cd house-price-predictor
   

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   

3. **Run the App**

   ```bash
   python app.py
   

4. **Open in Browser**
   Visit: `http://127.0.0.1:5000/`



### 📽️ Demo Video

> I’ve also included a short **screen-recorded demo** of the project in action. *(Optional but recommended for resumes!)*

---

### 📚 Notebook Summary

* Data cleaning & preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering
* Training & evaluating multiple regression models
* Final model selection based on accuracy
* Model deployment using Flask

---

### 🏁 Conclusion

This project showcases my ability to build a **complete machine learning pipeline** — from data to deployment. It reflects skills in **regression analysis, model selection, web app development**, and real-world deployment using Flask.

