"""
Registration Form and  Login Form
"""
# Import 'FlaskForm' from 'flask_wtf', NOT 'wtforms'
from flask_wtf import Form
# Fields and validators from 'wtforms'
from wtforms import StringField, PasswordField,  TextAreaField, TextField, validators
from wtforms.validators import InputRequired, Length

# Define the 'Registration Form' class by sub-classing 'Form'

class RegistrationForm(Form):
    # This form contains four fields with input validators
    username =StringField('User Name:', validators=[InputRequired()])
    email = StringField('Email:', validators=[InputRequired(), validators.Email(message = "please enter valid email format, E.g: username@example.com"), Length(min=6, max=35)])
    password = PasswordField('New Password:', [validators.Required(),Length(min=3, max=35)])
    confirm = PasswordField('Repeat Password:', [validators.Required(), validators.EqualTo('password', message='Passwords must match')])

 # Define the 'LoginForm' class by sub-classing 'Form'
class LoginForm(Form):
    # This form contains two fields with input validators
    username = StringField('User Name:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired(), Length(min=3, max=35)])


# Define the 'Create Events Form' class by sub-classing 'Form'

class EventsForm(Form):
    # This form contains four fields with input validators
    title =TextField('Event Title:', validators=[InputRequired()])
    location = TextField('Event Location:', validators=[InputRequired()])
    category = TextField('Event Category:', validators=[InputRequired()])
    description = TextAreaField('Event Description:', validators=[InputRequired(), Length(min=10, max=400)])
