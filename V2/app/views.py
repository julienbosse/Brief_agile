from flask import render_template, request, abort, redirect, url_for, Flask
from app import app
import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template('index.html', date=date)
