import hmac
import hashlib
import urllib2
import json
import timestring
import requests
from pprint import pprint
from eventObject import eventObject
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'This will be a cool website soon'
