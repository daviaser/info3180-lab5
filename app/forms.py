# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.csrf import CSRFProtect

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), DataRequired()])
    description = TextAreaField('Description', validators=[InputRequired(), DataRequired()])
    poster = FileField('Poster',validators=[DataRequired(), FileRequired(), FileAllowed(['png', 'jpg', 'jpeg'], 'Images only!')] )
    