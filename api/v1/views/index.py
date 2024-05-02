#!/usr/bin/python3
"""
Create flask app blueprint
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route("/status")
def api_status():
    """
    Display status.
    """
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route("/stats")
def get_stats():
    """
    Provide display of all count of objects.
    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }

    return jsonify(stats)
