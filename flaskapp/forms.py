from flask_wtf import Form
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import Required

class CarForm(Form):
    miles = IntegerField('Milage', validators=[Required()])
    make  = SelectField('Make', validators=[Required()])
    submit = SubmitField('Submit')
