#!/usr/bin/python3
"""
app to connect API
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close_storage(self):
    """call storage.close()"""
    storage.close()


@app.errorhandler(404)
def error_handler(error):
    """return a JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True, debug=True)
