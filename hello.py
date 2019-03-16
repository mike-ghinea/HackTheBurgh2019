from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'This will be a cool website soon'

@app.route('/festivals')
def festivals():
    return ''
