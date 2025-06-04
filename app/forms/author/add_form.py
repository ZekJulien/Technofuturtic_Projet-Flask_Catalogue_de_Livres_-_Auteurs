from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class AddAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    country = StringField('Country', validators=[Length(max=100)])