from flask_wtf import FlaskForm
from wtforms import RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SettingsForm(FlaskForm):
    operation = RadioField('Select Operation', choices=[('sum', 'Sum'), ('subtraction', 'Subtraction'), ('multiplication', 'Multiplication'), ('division', 'Division')], default='sum', validators=[DataRequired()])
    num_count = IntegerField('Number of Operands', default=2, validators=[DataRequired(), NumberRange(min=2, max=4)])
    digit_count = IntegerField('Max Digits per Number', default=2, validators=[DataRequired(), NumberRange(min=1, max=5)])
    submit = SubmitField('Start')