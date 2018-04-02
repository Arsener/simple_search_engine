from flask import Blueprint

sjet = Blueprint('sjet', __name__)

from . import views, errors
