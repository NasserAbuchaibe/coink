from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email



class LoginForm(FlaskForm):
    username = StringField('Nombre Completo', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    city = StringField('Ciudad', validators=[DataRequired()])
    submit = SubmitField('Crear usuario')
