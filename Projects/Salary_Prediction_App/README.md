# 💼 Salary Prediction App using Simple Linear Regression

This is an end-to-end machine learning project that demonstrates how to build, train, and deploy a salary prediction model using **Simple Linear Regression (SLR)**. The model predicts an employee’s salary based on their years of experience.

---

## 📌 What This Project Covers

✅ Perform Exploratory Data Analysis (EDA)  
✅ Train and evaluate a Simple Linear Regression model  
✅ Save the trained model using `pickle`  
✅ Build a frontend using **Streamlit**  
✅ Deploy the app locally for real-time predictions  

---

## 🧠 Technologies Used

| Tool          | Purpose                          |
|---------------|----------------------------------|
| Python        | Programming language             |
| Pandas, NumPy | Data manipulation                |
| Matplotlib, Seaborn | Visualization (optional)    |
| Scikit-learn  | Machine Learning (LinearRegression) |
| Pickle        | Save/load trained model          |
| Streamlit     | Web app frontend                 |

---

## 📁 Folder Structure

```

GitHub\_SLR\_App/
│
├── Day40\_End\_to\_End\_ML\_App\_with\_Streamlit.ipynb  # Full analysis & ML pipeline
├── SLR\_app1.py                                   # Streamlit frontend app
├── linear\_regression\_model.pkl                   # Pickled trained model
├── requirements.txt                              # All necessary dependencies
└── README.md                                     # This file

````

---

## 🚀 How to Run the App

### 📦 1. Install Dependencies

Open terminal in the project folder and run:

```bash
pip install -r requirements.txt
````

### ▶️ 2. Launch the Web App

```bash
streamlit run SLR_app1.py
```

It will open in your browser at:
**[http://localhost:8501](http://localhost:8501)**

---

## 🧪 Model Summary

* Algorithm: **Simple Linear Regression**
* Target: **Salary**
* Feature: **Years of Experience**
* Trained on real-world sample dataset (CSV)
* Performance evaluated with R², MSE, and statistical metrics

---

## 📝 Example Predictions

| Years of Experience | Predicted Salary (₹) |
| ------------------- | -------------------- |
| 1.0                 | ₹39,000 approx       |
| 5.0                 | ₹70,000 approx       |
| 10.0                | ₹115,000 approx      |

---

## ✅ Highlights

* End-to-End ML Pipeline ✅
* Frontend + Backend Integration ✅
* Beginner-Friendly & Educational ✅
* Ready to Deploy or Expand ✅

---

## 🙋‍♂️ Author & Acknowledgement

Made with ❤️ by **Akshay Bhujbal**
Educational purpose project — inspired by real datasets.
