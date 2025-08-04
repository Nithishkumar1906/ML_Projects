import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")


# Route to load the homepage
@app.route("/")
def load_page():
    return render_template('home.html', prediction=None)

# Route to handle form submission and prediction
@app.route("/predict", methods=["POST"])
def predict():
    mean_radius = float(request.form["mean_radius"])
    mean_texture = float(request.form["mean_texture"])
    mean_perimeter = float(request.form["mean_perimeter"])
    mean_smoothness = float(request.form["mean_smoothness"])
    mean_area = float(request.form["mean_area"])

    features = ['mean_radius','mean_texture','mean_perimeter','mean_smoothness','mean_area']
    data = [mean_radius, mean_texture, mean_perimeter, mean_smoothness, mean_area]
    new_data = pd.DataFrame([data], columns=features)

    single = model.predict(new_data)[0]
    prob = model.predict_proba(new_data)[0]

    if single == 1:
        output = "The patient has breast cancer"
    else:
        output = "The patient does not have breast cancer"

    output_1 = "Confidence levels: {:.2f}% (Benign), {:.2f}% (Malignant)".format(prob[0]*100, prob[1]*100)

    return render_template('home.html',
        output=output,
        output_1=output_1,
        mean_radius=mean_radius,
        mean_texture=mean_texture,
        mean_perimeter=mean_perimeter,
        mean_smoothness=mean_smoothness,
        mean_area=mean_area)


app.run(debug=True)


