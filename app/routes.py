from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Anurag'}
	return render_template('index.html', title='Home', user=user)

@app.route('/registrations')
def registrations():
	return render_template('registration.html')