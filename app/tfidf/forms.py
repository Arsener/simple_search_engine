from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    real_name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    school = StringField('School', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = TextAreaField('', validators=[Required()])
    submit = SubmitField('Submit')