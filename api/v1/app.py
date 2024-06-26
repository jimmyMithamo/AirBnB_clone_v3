#!/usr/bin/python3
"""main application"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app .register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def tear_down(exception):
    """calls storage.close"""
    storage.close()


@app.errorhandler(404)
def error_handler(error):
    """returns a JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    if os.getenv('HBNB_API_HOST') is None:
        host = '0.0.0.0'
    else:
        host = os.getenv('HBNB_API_HOST')
    if os.getenv('HBNB_API_PORT') is None:
        port = 5000
    else:
        port = int(os.getenv('HBNB_API_PORT'))
    app.run(host=host, port=port, threaded=True, debug=True)
