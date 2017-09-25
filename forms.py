from flask_wtf import Form
from wtforms import StringField, BooleanField, DateField, TextField, validators, ValidationError, IntegerField
from wtforms.validators import DataRequired

class RequestForm(Form):
    title = TextField('title', validators=[validators.required()])
    description = TextField('description', validators=[validators.required()])
    client_id = IntegerField('client_id', validators=[validators.required()])
    priority = IntegerField('priority', validators=[validators.required()])
    target_date = DateField('target_date', validators=[validators.required()])
    product_id = IntegerField('product_id', validators=[validators.required()])