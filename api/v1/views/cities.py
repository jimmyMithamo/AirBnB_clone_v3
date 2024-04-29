#!/usr/bin/python3
"""
View for Cities that handles all RESTful API actions
"""

from flask import jsonify, request, abort
from models import storage
from models.city import City
from api.v1.views import app_views

@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """ returns list of all City objects """
    cities_all = []
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    cities = state.cities
    for city in cities:
        cities_all.append(city.to_dict())

    return jsonify(cities_all)

@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """ gets a city object by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city = city.to_dict()
    return jsonify(city)

@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """ deletes a city object by id"""
    empty_dict = {}
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify(empty_dict), 200

@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """creates a city object"""
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    data['state_id'] = state_id
    city = City(**data)
    city.save()
    city = city.to_dict()
    return jsonify(city), 201

@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(404, "Not a JSON")
    ignore_keys = ["id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in ignore_keys:
            city.name = data["name"]
            city.save()
    return jsonify(city.to_dict()), 200