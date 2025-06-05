from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectMultipleField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message="Title cannot be empty."), Length(max=100)])
    genre = StringField('Genre', validators=[DataRequired(message="Genre cannot be empty."), Length(max=100)])
    publication_date = DateField('Publication date', validators=[DataRequired("Publication date cannot be empty.")])
    id_author = StringField('Author', validators=[DataRequired(message="Author cannot be empty.")])
    categories = SelectMultipleField('Categories', coerce=int, choices=[], validators=[DataRequired(message="Choose at least 1 category")])