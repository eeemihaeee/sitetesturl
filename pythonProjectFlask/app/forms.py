from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('User',validators = [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField("Sign In")

