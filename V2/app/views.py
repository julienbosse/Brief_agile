from flask import render_template, request, abort, redirect, url_for, Flask
from app import app
import datetime
from joblib import load
from geopy.geocoders import Nominatim
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import sklearn
import time
from app import models
import json
import http.client, urllib.parse


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
    income = float(request.form['income'])/10
    rooms = request.form['rooms']
    bedrooms = request.form['bedrooms']

    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': 'ebdb53cd8ffbdf290d81f2babdc46a25',
        'query': address,
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()

    data = res.read().decode('utf-8')

    location = json.loads(data)

    latitude = float(location["data"][0]["latitude"])
    longitude = float(location["data"][0]["longitude"])

    #geolocator = Nominatim(user_agent="Estimaison")
    # location = geolocator.geocode(address)

    # model : ["ll", 'longitude', 'latitude', 'rooms_per_household', 'bedrooms_per_household', "median_income"]

    model = load('app/static/model.joblib')
    prediction = model.predict([[longitude*latitude, longitude, latitude, rooms, bedrooms, income]])[0]

    source = "https://www.google.com/maps/embed/v1/view?key=AIzaSyDstWgA2pIh8wutGWQ35pVzE7Pc5cl6yCU&center="+str(longitude)+","+str(latitude)+"&zoom=18&maptype=roadmap"

    date = datetime.datetime.now().strftime("%x %X")
    return render_template(
        'predict.html',
        date=date,
        address=address,
        prediction=prediction,
        longitude=longitude,
        latitude=latitude,
        source=source)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template('dashboard.html', date=date)


@app.route('/team', methods=['GET', 'POST'])
def team():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template('team.html', date=date)
