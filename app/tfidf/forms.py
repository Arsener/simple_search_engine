# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_uploads import UploadSet, TEXT


class FileForm(FlaskForm):
    text = UploadSet('text', TEXT)
    text_file = FileField(u'文件上传', validators=[
        FileAllowed(text, u'只能上传.txt文件！'),
        FileRequired(u'文件未选择！')
    ])
    submit = SubmitField(u'上传并计算此文档中每个词的TFIDF')