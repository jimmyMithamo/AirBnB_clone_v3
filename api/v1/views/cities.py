#!/usr/bin/python3
<<<<<<< HEAD
"""
cities.py
"""

=======
from flask import jsonify, abort, request
>>>>>>> 7e28e44 (changes)
from api.v1.views import app_views
from models import storage
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """return all cities in a state"""
    cities = storage.all(City).values()
    return jsonify([city.to_dict() for city in cities if city.state_id == state_id])

@app_views.route("cities/<city_id>", methods=["GET"], strict_slashes=False)
def get_city(city_id):
    """retrieves a city by id"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)
