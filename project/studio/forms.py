from wtforms import (
    StringField,
    TextAreaField,
)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class ArticleForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    body = TextAreaField(validators=[InputRequired()])