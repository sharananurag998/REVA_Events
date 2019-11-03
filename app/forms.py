from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()

class AddEventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired()])
    body = StringField('About', validators=[DataRequired()])
    venue = StringField('Venue', validators=[DataRequired()])
    branch = StringField('Branch', validators=[DataRequired()])
    image = StringField('Image_URL')
    timestamp = DateField('Event_Date')
    submit = SubmitField()