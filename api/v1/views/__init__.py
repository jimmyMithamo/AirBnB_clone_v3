#!/usr/bin/python3
"""
creating a blueprint
"""

from flask import Blueprint
from .index import *
from .states import *
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
