# -*- coding: utf-8 -*-
import flask_wtf
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

class TfidfForm(flask_wtf.FlaskForm):
    input_word = StringField(u'请输入你想要计算TFIDF值的汉语词', validators=[Required()])
    submit = SubmitField(u'开始计算')