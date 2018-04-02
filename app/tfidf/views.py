from flask import render_template, redirect, request, url_for, flash, current_app
from . import tfidf
from .forms import TfidfForm

@tfidf.route('/')
def index():
    form = TfidfForm()
    if form.validate_on_submit():
        word = form.input_word.data
        '''
        find answer
        '''
        answer = word
        return render_template('tfidf.html', form=form, answer=answer)

    return render_template('tfidf.html', form=form)