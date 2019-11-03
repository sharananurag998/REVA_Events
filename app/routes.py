from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Anurag'}
	return render_template('index.html', title='Home', user=user)

@app.route('/registrations')
def registrations():
	return render_template('registration.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/Event')
def calander():
    events = [
        {
            'event': 'Hackathon 2019',
            'venue': 'REVA Rangasthala',
        },
        {
            'event': 'Under 25',
            'venue': 'Kuvempu Theatre'
        }
    ] 
    return render_template('Event_Calandar1.html', events = events)

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login2.html', title='Sign In', form=form)

@app.route('/certificates')
def certificates():
	return render_template('certificates.html')

@app.route('/qrread')
def qr():
	return render_template('qrreader.html')

@app.route('/evn_det')
def ev():
	return render_template('event details.html')

