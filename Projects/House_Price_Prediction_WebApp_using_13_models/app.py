from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# List of all pre-trained model filenames
model_names = [
    'LinearRegression', 'RobustRegression', 'RidgeRegression', 'LassoRegression', 'ElasticNet',
    'PolynomialRegression', 'SGDRegressor', 'ANN', 'RandomForest', 'SVM', 'LGBM',
    'XGBoost', 'KNN'
]

# Load models from pickle files
models = {}
for name in model_names:
    try:
        models[name] = pickle.load(open(f'{name}.pkl', 'rb'))
    except FileNotFoundError:
        print(f"Warning: {name}.pkl not found!")

# Load evaluation metrics from CSV
try:
    results_df = pd.read_csv('model_evaluation_results.csv')
except FileNotFoundError:
    results_df = pd.DataFrame(columns=["Model", "MAE", "MSE", "RMSE", "R2"])

@app.route('/')
def index():
    return render_template('index.html', model_names=models.keys())

@app.route('/predict', methods=['POST'])
def predict():
    try:
        model_name = request.form['model']
        input_data = {
            'Avg. Area Income': float(request.form['Avg. Area Income']),
            'Avg. Area House Age': float(request.form['Avg. Area House Age']),
            'Avg. Area Number of Rooms': float(request.form['Avg. Area Number of Rooms']),
            'Avg. Area Number of Bedrooms': float(request.form['Avg. Area Number of Bedrooms']),
            'Area Population': float(request.form['Area Population'])
        }
        input_df = pd.DataFrame([input_data])

        if model_name in models:
            model = models[model_name]
            prediction = model.predict(input_df)[0]
            return render_template(
                'results.html',
                prediction=round(prediction, 2),
                model_name=model_name,
                input_data=input_data  # ✅ <-- pass this!
            )
        else:
            return jsonify({'error': 'Model not found'}), 400

    except Exception as e:
        return render_template(
            'results.html',
            prediction="Error: " + str(e),
            model_name="Invalid",
            input_data={}  # also pass empty to avoid template error
        )

@app.route('/results')
def results():
    return render_template('model.html', tables=[results_df.to_html(classes='table table-striped table-bordered')], titles=results_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
