from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Reading inputs from web form
            longitude = float(request.form['longitude'])
            latitude = float(request.form['latitude'])
            housing_median_age = float(request.form['housing_median_age'])
            total_rooms = float(request.form['total_rooms'])
            total_bedrooms = float(request.form['total_bedrooms'])
            population = float(request.form['population'])
            households = float(request.form['households'])
            median_income = float(request.form['median_income'])
            ocean_proximity = request.form['ocean_proximity']

            # One-hot encoding mapping for ocean_proximity
            # Matches dummy variables created during training (drop_first=True)
            ocean_INLAND = 1.0 if ocean_proximity == 'INLAND' else 0.0
            ocean_ISLAND = 1.0 if ocean_proximity == 'ISLAND' else 0.0
            ocean_NEAR_BAY = 1.0 if ocean_proximity == 'NEAR BAY' else 0.0
            ocean_NEAR_OCEAN = 1.0 if ocean_proximity == 'NEAR OCEAN' else 0.0

            data = [
                longitude, latitude, housing_median_age, total_rooms,
                total_bedrooms, population, households, median_income,
                ocean_INLAND, ocean_ISLAND, ocean_NEAR_BAY, ocean_NEAR_OCEAN
            ]

            data = np.array(data).reshape(1, 12)
            
            # Load trained model artifact
            model = joblib.load(os.path.join("artifacts/model_trainer/model.joblib"))
            predict = model.predict(data)

            return render_template('index.html', prediction=str(np.round(predict[0], 2)))

        except Exception as e:
            return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)