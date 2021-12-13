from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired

class CreateCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    comics_appeared_in = IntegerField('Comics appeared in')
    super_power = StringField('Super power')
    submit = SubmitField()
    

