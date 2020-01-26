from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo


""" FORM FOR SEARCH"""


class SearchForm(FlaskForm):
    date = DateField(
        'Date',
        validators=[
            DataRequired()
        ]
    )
    origin = StringField(
        'From',
        validators=[
            DataRequired
        ]
    )
    destination = StringField(
        'To',
        validators=[
            DataRequired
        ]
    )
    search = SubmitField()
