import hmac
import hashlib
import urllib2
import json
import timestring
import requests

from eventFunctions import getEventsByFestival

from flask import Flask, url_for, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

start = 0

@app.route('/')
def index():
  start = 0
  return render_template('index.html')

@app.route('/festivals.html', methods=['POST'])
def festivals():
  festival = request.form["Category"]
  perpage = request.form["per_page"]
  year = request.form["year"]
  events = getEventsByFestival(festival, year, perpage, start)
  return \
  render_template('festivals.html', events=events)
