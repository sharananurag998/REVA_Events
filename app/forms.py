from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()

class addEventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired()])
    about = StringField('About', validators=[DataRequired()])
    venue = StringField('Venue', validators=[DataRequired()])
    branch = StringField('Branch', StringField('About', validators=[DataRequired()]))
