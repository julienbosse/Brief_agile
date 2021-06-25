from flask import render_template, request, abort, redirect, url_for, Flask
from app import app
import datetime
from joblib import load
from geopy.geocoders import Nominatim
import time


@app.route('/', methods=['GET', 'POST'])
def index():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template('index.html', date=date)


@app.route('/form_predict', methods=['GET', 'POST'])
def form_predict():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template('form_predict.html', date=date)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    address = request.form['address']
    income = request.form['income']
    rooms = request.form['rooms']
    bedrooms = request.form['bedrooms']

    geolocator = Nominatim(user_agent="Estimaison")
    location = geolocator.geocode(address)

    # model : ["ll", 'longitude', 'latitude', 'rooms_per_household', 'bedrooms_per_household', "median_income"]

    model = load('app/static/model.joblib')
    prediction = model.predict([[location.longitude*location.latitude, location.longitude, location.latitude, rooms, bedrooms, income]])[0]

    date = datetime.datetime.now().strftime("%x %X")
    return render_template(
        'predict.html',
        date=date,
        address=address,
        prediction=prediction,
        longitude=location.longitude,
        latitude=location.latitude)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template('dashboard.html', date=date)
