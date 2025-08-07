from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("student_mark_predictor_model_pickel_file.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            hours = float(request.form['hours'])

            # ⛔ Input validation
            if hours < 0 or hours > 24:
                return render_template('index.html', error="❌ Study hours must be between 0 and 24.")

            # ✅ Make prediction
            prediction = model.predict([[hours]])[0][0].round(2)

            # 🛑 Clamp predicted marks between 0 and 100
            prediction = max(0.0, min(100.0, prediction))

            return render_template('index.html', prediction=prediction, hours=hours)

        except Exception as e:
            return render_template('index.html', error=f"❌ Invalid input: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
