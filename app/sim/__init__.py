from flask import Blueprint

sim = Blueprint('sim', __name__)

from . import views, errors
