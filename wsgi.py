# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort, request
import itertools

app = Flask(__name__)

my_dict = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Socialive.tv' }
}

@app.route('/')
def hello():
    return "hello world ff!"


@app.route('/api/v1/products_old')
def product_old():
    return

@app.route('/api/v1/products')
def read_all_product():
    return jsonify(list(my_dict.values()))


@app.route('/api/v1/products/<int:id>')
def read_one_product(id):
    product = my_dict.get(id)
    if product is None:
        abort(404)

    return (jsonify(product), 200)

@app.route('/api/v1/products/<int:id>',methods = ['delete'])
def delete_one_product(id):
    product = my_dict.get(id)
    if product is None:
        abort(404)

    del my_dict[id]
    return (None, 204)

@app.route('/api/v1/products',methods = ['post'])
def add_one_product():
    next_index = max(my_dict.keys()) + 1
    my_request_json = request.get_json()
    #print(my_request_json)
    if 'name' not in my_request_json:
        abort(404)
    #print(type(my_request_json))
    #print(my_request_json['name'])
    my_dict[next_index] = {'id':4, 'name': my_request_json['name'] }
    #print(my_dict)

    return ("", 201)

@app.route('/api/v1/products',methods = ['patch'])
def update_one_product():
    my_request_json = request.get_json()
    #print(my_request_json)
    if 'id' not in my_request_json or 'name' not in my_request_json:
        abort(404)

    if my_request_json['id'] not in my_dict:
        abort(422)

    my_dict[my_request_json['id']]['name'] = my_request_json['name']
    print(my_dict)

    return ("", 204)
