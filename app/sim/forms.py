# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class SimForm(FlaskForm):
    sentence1 = StringField(u'请输入第一个句子', validators=[Required()])
    sentence2 = StringField(u'请输入第二个句子', validators=[Required()])
    submit = SubmitField(u'计算两个句子的相似度')