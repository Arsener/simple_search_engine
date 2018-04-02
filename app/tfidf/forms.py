# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

class TfidfForm(FlaskForm):
    input_word = StringField(u'请输入你想要计算TFIDF值的汉语词', validators=[Required()])
    submit = SubmitField(u'开始计算')