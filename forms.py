from flask_wtf import FlaskForm
from wtforms.fields import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """User registration form
    """
    username = StringField('Nombre Completo', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    city = StringField('Ciudad', validators=[DataRequired()])
    submit = SubmitField('Crear usuario')
