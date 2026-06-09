<div align="center">

# Penguin Species Classification API

Production-grade machine learning inference service built with FastAPI and Scikit-Learn.

[![Python](https://img.shields.io/badge/Python-3.12-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)]()
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-RandomForest-orange)]()
[![Status](https://img.shields.io/badge/Status-Ready_for_Deployment-success)]()

</div>

---

## Overview

This project implements a machine learning inference service that predicts penguin species from biological measurements and categorical attributes.

The system was originally developed as a Streamlit prototype and later redesigned into a production-style FastAPI microservice architecture with separated training and inference workflows.

The objective of the project is to demonstrate practical machine learning deployment concepts including:

* Offline model training
* Artifact serialization
* Feature encoding persistence
* REST API development
* Request validation
* Reproducible inference pipelines

---

## Business Problem

Given a penguin's physical characteristics:

| Feature           | Type        |
| ----------------- | ----------- |
| island            | Categorical |
| bill_length_mm    | Numerical   |
| bill_depth_mm     | Numerical   |
| flipper_length_mm | Numerical   |
| body_mass_g       | Numerical   |
| sex               | Categorical |

the service predicts one of the following species:

* Adelie
* Chinstrap
* Gentoo

---

## System Architecture

```text
Client Application
        │
        ▼
  FastAPI Endpoint
        │
        ▼
 Request Validation
     (Pydantic)
        │
        ▼
   predictor.py
        │
        ▼
 encoder.pkl
        │
        ▼
  model.pkl
        │
        ▼
 Species Prediction
```

---

## Dataset

Dataset Source:

Palmer Penguins Dataset

Records Before Cleaning:

```text
344
```

Records After Cleaning:

```text
333
```

Preprocessing Steps:

* Removed rows containing missing values
* Removed non-predictive year column
* Applied One-Hot Encoding to categorical variables
* Persisted encoder for production inference

---

## Model Development

### Algorithm

Random Forest Classifier

### Motivation

Random Forest was selected because it:

* Handles mixed numerical and categorical features effectively
* Reduces variance through ensemble learning
* Provides strong performance on tabular datasets
* Is less prone to overfitting than a single decision tree

---

## Model Evaluation

### Performance Metrics

| Metric                         | Score |
| ------------------------------ | ----- |
| Test Accuracy                  | 1.00  |
| Mean Cross Validation Accuracy | 0.991 |

### Validation Strategy

The model was evaluated using:

* Hold-out test set evaluation
* 5-fold cross validation
* Label-shuffling sanity test

During label shuffling, accuracy dropped to approximately 27–43%, indicating that the model learned meaningful feature relationships rather than memorizing training samples.

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
    "status": "healthy"
}
```

---

### Species Prediction

```http
POST /predict
```

Request:

```json
{
    "island": "Dream",
    "bill_length_mm": 41.9,
    "bill_depth_mm": 17.2,
    "flipper_length_mm": 201.0,
    "body_mass_g": 4267.0,
    "sex": "male"
}
```

Response:

```json
{
    "prediction": "Gentoo"
}
```

---

## Repository Structure

```text
.
│
├── app
│   ├── main.py
│   └── predictor.py
│
├── artifacts
│   ├── encoder.pkl
│   └── model.pkl
│
├── pipeline.ipynb
│
├── streamlit_app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Training Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Encoding
      │
      ▼
Random Forest Training
      │
      ▼
Model Evaluation
      │
      ▼
Artifact Export
      │
      ├── encoder.pkl
      └── model.pkl
```

---

## Inference Workflow

```text
JSON Request
      │
      ▼
FastAPI Validation
      │
      ▼
DataFrame Conversion
      │
      ▼
Encoder Transformation
      │
      ▼
Random Forest Inference
      │
      ▼
JSON Response
```

---

## Technologies

* Python
* FastAPI
* Scikit-Learn
* Pandas
* NumPy
* Joblib
* Uvicorn
* Jupyter Notebook

---

## Future Roadmap

* React-based frontend integration
* Multi-model deployment dashboard
* CI/CD automation
* Containerized deployment
* Model monitoring and observability

---

## Author

Jaganathan J

Machine Learning Engineering • Data Science • Backend Systems