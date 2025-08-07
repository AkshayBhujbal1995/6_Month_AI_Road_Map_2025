
# 🎯 Student Marks Predictor – ML Model Deployment using Flask & HTML

This is a real-world **end-to-end machine learning project** where we predict **student marks** based on the number of **hours studied**.

---

## 📌 Business Problem

A university reports that:
- No students score above 90%
- Most students average below 60%

The management suspects that **study hours might be a key factor**.  
They need a **tool** to predict how much a student might score based on how many hours they study.

---

## 🔍 Solution

We built a **Machine Learning regression model**, deployed it using **Flask**, and created a **web interface** where users can enter hours and get predicted marks instantly.

---

## 🛠️ Technologies Used

| Component     | Tool / Library       |
|---------------|----------------------|
| Programming   | Python               |
| ML Model      | Linear Regression (scikit-learn) |
| Web Framework | Flask                |
| Frontend      | HTML, CSS            |
| Packaging     | Joblib               |
| Notebook      | Jupyter Notebook     |
| Charts        | Matplotlib           |

---

## ✅ Project Features

- Clean and simple HTML frontend
- Flask backend for real-time predictions
- Model saved using `joblib` (no retraining needed)
- Input validation (only hours between 0 and 24 allowed)
- Auto-clear previous predictions after new entry
- Moving animated background
- Explanation of real-world deployment (app vs prod server)

---

## 🖼️ Screenshots

### 🔷 App Frontend (Before Prediction)

![App Frontend](screenshots/frontend_1.png)

---

### 🔷 Prediction Example – 5 Hours Input

![Predicted Output](prediction_5hr.PNG)

---

### 🔷 Error Message for Invalid Input (e.g., 25 hours)

![Error Message](error_message.png)

---

## 💡 How to Run This Project

1. Clone the repo or download ZIP
2. Make sure Python is installed
3. Install dependencies:

```bash
pip install -r requirements.txt
````

4. Run the Flask app:

```bash
python app.py
```

5. Open your browser and go to:

```
http://127.0.0.1:5000/
```

6. Enter hours, click "Predict Marks", and see results in real-time

---

## 📊 Output Example

For 5.0 hours studied → 📈 Predicted Marks: **70.13%**
If you enter invalid input like -2 or 25 → ❌ Shows error message

---

## 🧠 Deployment Insight

This app runs on an **application server**.
In real-world companies:

* Developers work on app servers with dummy/duplicate data
* Deployment means moving code from **app server** → **production server**
* Production servers have restrictions (security, access, firewall)
* Model and data must be validated for live use

---

## 📂 Folder Structure

```
student_marks_predictor/
│
├── app.py                  # Flask backend
├── student_mark_predictor_model_pickel_file.pkl
├── templates/
│   └── index.html          # Frontend form
├── static/
│   └── background.css      # Optional: styling or images
├── screenshots/
│   ├── frontend_1.png
│   ├── prediction_5hr.png
│   └── error_message.png
├── requirements.txt
└── README.md
```

---

## 📬 Author

**Akshay Bhujbal**
Passionate about ML, Data Science, and real-world applications.
Let’s connect on LinkedIn or GitHub!

---

```

> 🔔 Make sure you **create a `screenshots` folder** and place your 3 image files there:
- `frontend_1.png`
- `prediction_5hr.png`
- `error_message.png`

Let me know if you'd like me to package this into a **ready-to-download ZIP** or help push it to GitHub.
```
