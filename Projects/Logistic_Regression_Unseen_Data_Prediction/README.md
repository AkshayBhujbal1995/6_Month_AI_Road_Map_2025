# 📘 Day 51 – Logistic Regression on Unseen Data

This project continues from **Day 50**, where we trained a Logistic Regression model to predict if a user will purchase a product based on their **Age** and **Estimated Salary**.

In **Day 51**, we go one step further:
- ✅ Rebuild the model from scratch (same settings as Day 50)
- ✅ Predict outcomes on new, unseen data
- ✅ Save the model and scaler using `pickle`
- ✅ Create a **Streamlit web app** that accepts manual user input for prediction

---

## 🚀 Features

- Predict if a user will **purchase or not** using Age & Estimated Salary
- Enter inputs manually using input fields
- Live web interface built using Streamlit
- Model and scaler saved using `pickle` for real-time prediction

---

## 🧠 Technologies Used

- Python 3.11+
- Streamlit
- scikit-learn
- pandas
- numpy

---

## ▶️ How to Run This Project

### ✅ Step 1: Clone or Download the Files

Make sure these files are present:
- `day51_logistic_app.py` ✅
- `model2.pkl` ✅
- `scaler2.pkl` ✅

You can also rebuild the model in a notebook using:
```

Day51\_Logistic\_Regression\_Unseen\_Data\_Prediction.ipynb

````

---

### ✅ Step 2: Install Dependencies

```bash
pip install streamlit scikit-learn pandas numpy
````

---

### ✅ Step 3: Run the App

```bash
streamlit run day51_logistic_app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 📊 Model Details

* Algorithm: Logistic Regression
* Scaler: StandardScaler
* Features: Age, Estimated Salary
* Output: 0 (Not Purchased) or 1 (Purchased)

> ⚠️ **Note:**
> This model is not finalized or production-ready.
> More real-world testing, feature selection, and validation are needed to ensure consistent performance on unseen data.

---

## 📝 Example Predictions

| Age | Salary | Prediction          |
| --- | ------ | ------------------- |
| 25  | 35000  | ❌ Will Not Purchase |
| 40  | 90000  | ✅ Will Purchase     |

---

## 🔮 Future Improvements

* Add **gender** with one-hot encoding
* Allow **CSV file upload** for bulk predictions
* Add **error handling** and model confidence score
* Deploy the app on **Streamlit Cloud**
* Add **more real-world test data** and **cross-validation**

---

## 🙌 Author

Made with ❤️ by Akshay Bhujbal as part of the #100DaysOfCode journey
`Day 51 – ML to Real Life 💻 → 📊 → 🌐`
