#!/usr/bin/python3
<<<<<<< HEAD
"""
index.py
"""

from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ Returns the status of the api."""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
=======
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/stats', methods=['GET'])
>>>>>>> 7e28e44 (changes)
def get_stats():
    """retrieves statistics about the objects"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "users": storage.count("User")
    }
    return jsonify(stats)
<<<<<<< HEAD
=======

>>>>>>> 7e28e44 (changes)
