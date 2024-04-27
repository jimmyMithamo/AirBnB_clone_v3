#!/usr/bin/python3
"""
index.py
"""

from flask import jsonify
from models import storage


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """retrieves statistics about the objects"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(stats)
