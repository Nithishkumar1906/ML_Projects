# Breast Cancer Prediction App

## Overview

A Flask web app that predicts whether a breast tumor is benign or malignant from five diagnostic measurements, using a Random Forest classifier trained on the Wisconsin-style breast cancer dataset.

## Problem Statement

Given tumor measurements (radius, texture, perimeter, smoothness, area), classify the diagnosis as malignant or benign and surface a confidence score for each class.

## Dataset

[`Breast_cancer_data.csv`](./Breast_cancer_data.csv) — 569 records with columns `mean_radius`, `mean_texture`, `mean_perimeter`, `mean_area`, `mean_smoothness`, `diagnosis`.

## Approach

- Model training happens in [`model-training.ipynb`](./model-training.ipynb): load the CSV, split into train/test (455/114), and fit a `RandomForestClassifier(n_estimators=500)`.
- The trained model is serialized to [`model.pkl`](./model.pkl) and loaded by the Flask app at startup.
- `app.py` exposes a form (`templates/home.html`) that collects the five features, builds a single-row `DataFrame`, and calls `model.predict()` / `model.predict_proba()` to render a diagnosis and confidence breakdown.

## Model

`RandomForestClassifier` (scikit-learn), `n_estimators=500`.

## Evaluation

Test accuracy: **92%** (114-sample held-out test set), as reported in `model-training.ipynb`.

## Results

The app returns a plain-language prediction ("has breast cancer" / "does not have breast cancer") plus a per-class confidence percentage.

## Key Learnings

- End-to-end path from a trained scikit-learn model to a Flask inference endpoint.
- Serving a model via `joblib`/`pickle` and wiring form inputs to a `DataFrame` matching the training schema.

## Technologies Used

Python, pandas, scikit-learn, Flask, joblib.

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

## Notes

- `requirements.txt` was empty in the original repo; it has been filled in based on the packages `app.py` actually imports.
- A duplicate, unused copy of `home.html` sat at the project root (Flask only reads from `templates/`) and has been removed.
