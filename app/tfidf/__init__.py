from flask import Blueprint

tfidf = Blueprint('tfidf', __name__)

from . import views, errors
