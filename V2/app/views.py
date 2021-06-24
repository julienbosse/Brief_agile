from flask import render_template, request, abort, redirect, url_for, Flask
from app import app
import datetime


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
    date = datetime.datetime.now().strftime("%x %X")
    return render_template('predict.html', date=date)
