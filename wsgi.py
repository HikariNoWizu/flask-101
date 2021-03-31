# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World ff!"


@app.route('/api/v1/products_old')
def product_old():
    return {
                1: { 'id': 1, 'name': 'Skello' },
                2: { 'id': 2, 'name': 'Socialive.tv' },
                3: { 'id': 2, 'name': 'Socialive.tv' }
           }

@app.route('/api/v1/products')
def product():
    return jsonify( {
                1: { 'id': 1, 'name': 'Skello' },
                2: { 'id': 2, 'name': 'Socialive.tv' },
                3: { 'id': 3, 'name': 'Socialive.tv' }
           }
           )

