from flask import render_template, redirect, request, url_for, flash, current_app
from . import tfidf

@tfidf.route('/')
def index():
    return render_template('tfidf.html')