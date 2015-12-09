from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User

class LoginForm(Form):
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Log In')

class RegistrationForm(Form):
    first_name = StringField('First Name', validators=[Required(), Length(1,64)])
    last_name = StringField('Last Name', validators=[Required(), Length(1,64)])
    username = StringField('Username', validators=[Required(), Length(1,64)])
    password = PasswordField('Password', validators=[Required()])
    confirmPassword = PasswordField('Confirm Password', validators=[Required(), EqualTo('password', message='Passwords must Match')])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
