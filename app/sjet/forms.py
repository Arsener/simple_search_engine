# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class SjetForm(FlaskForm):
    query = StringField(u'请输入你想查询的内容', validators=[Required()])
    submit = SubmitField(u'Geegle一下')