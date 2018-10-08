from flask_wtf import Form
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import Required

class CarForm(Form):
    year       = IntegerField('Year', validators=[Required()])
    miles      = IntegerField('Milage', validators=[Required()])
    fiscal_pow = IntegerField('Fiscal Pow', validators=[Required()])
    fuel_type  = SelectField('Fuel Type', validators=[Required()])
    make       = SelectField('Make', validators=[Required()])

    submit = SubmitField('Submit')