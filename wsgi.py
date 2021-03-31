# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World ff!"


@app.route('/api/v1/products')
def product():
    return {
                1: { 'id': 1, 'name': 'Skello' },
                2: { 'id': 2, 'name': 'Socialive.tv' }
           }
