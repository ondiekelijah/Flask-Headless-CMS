from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    FileField
)

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired,Length,Optional,Regexp
from .models import Authors,Category
from flask_pagedown.fields import PageDownField



class ArticleForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    body = PageDownField(validators=[InputRequired()])
    image = FileField(validators=[FileAllowed(["jpg", "png", "jpeg", "svg","webp"])])
    author = SelectField('Author', choices=[], coerce=int)
    category = SelectField('Category', choices=[], coerce=int)


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
    c_title = StringField(validators=[InputRequired(),
        Length(2, 300),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_. ]*$",
                0,
                "Titles must have only letters, " "numbers, dots or underscores",
            ),
        ])
