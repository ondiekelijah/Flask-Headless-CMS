from wtforms import (
    StringField,
    TextAreaField,
)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Length,Optional,Regexp


class ArticleForm(FlaskForm):
    title = StringField(validators=[InputRequired(),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_. ]*$",
                0,
                "Titles must have only letters, " "numbers, dots or underscores",
            ),
        ])
    body = TextAreaField(validators=[InputRequired()])


class AuthorForm(FlaskForm):
    name = StringField(validators=[InputRequired(),
           Length(2, 300),
        Regexp(
                "^[A-Za-z][A-Za-z0-9_. ]*$",
                0,
                "Titles must have only letters, " "numbers, dots or underscores",
            ),

        ])

    
class CategoryForm(FlaskForm):
    title = StringField(validators=[InputRequired(),
        Length(2, 300),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_. ]*$",
                0,
                "Titles must have only letters, " "numbers, dots or underscores",
            ),
        ])
