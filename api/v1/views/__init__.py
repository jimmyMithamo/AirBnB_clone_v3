#!/usr/bin/python3
"""
creating a blueprint
"""

from flask import Blueprint
from .index import *
from .state import *

"""
from api.v1.views.cities import *
from api.v1.views.amenities import *
"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

#!/usr/bin/python3
"""
creating a blueprint
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.places import *
from api.v1.views.amenities import *
from api.v1.views.users import *
