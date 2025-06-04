from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class AuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    country = StringField('Country', validators=[Length(max=100)])