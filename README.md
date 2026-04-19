Phishing Website Detection System

Machine Learning Project
A web-based application that detects whether a given URL is safe or phishing using a trained ML model.

--------------------------------------------------

OVERVIEW

This project uses a machine learning model to classify URLs as legitimate or phishing.
The system is deployed using a Flask web application where users can input a URL and get instant predictions.

--------------------------------------------------

HOW IT WORKS

1. User enters a URL in the web interface
2. URL is cleaned using regex
3. Text is transformed using a trained vectorizer
4. Model predicts whether URL is safe or phishing
5. Result is displayed on the webpage

--------------------------------------------------

MODEL DETAILS

Vectorizer: Converts URL text into numerical features
Model: Trained classification model (phising.pkl)

Prediction Output:
- good → Safe website
- bad → Phishing website

--------------------------------------------------

PROJECT STRUCTURE

phishing-website-detection-system/

app.py
templates/
vectorizer.pkl
phising.pkl
phishing_nmb.pkl
urls-dataset.csv
realtimephishingdetection.ipynb
myenv/

--------------------------------------------------

INSTALLATION

git clone https://github.com/yourusername/phishing-website-detection-system.git
cd phishing-website-detection-system

pip install flask scikit-learn pandas numpy

--------------------------------------------------

USAGE

Run the application:
python app.py

Open in browser:
http://127.0.0.1:5000

--------------------------------------------------

FEATURES

- Real-time URL classification
- Simple web interface using Flask
- Fast predictions using pre-trained model
- Regex-based URL preprocessing

--------------------------------------------------

TECH STACK

Python
Flask
Scikit-learn
Pandas
NumPy

--------------------------------------------------
