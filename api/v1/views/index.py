#!/usr/bin/python3
"""file"""
from models import storage
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', strict_slashes = False)
def status():
    """returns status of our api"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes = False)
def get_stat():
    """gets the number of class objects"""
    new_dict = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(new_dict)
