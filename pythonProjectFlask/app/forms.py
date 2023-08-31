from flask_wtf import Form
from wtforms import StringField, BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('User',validators = [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField("Sign In")

