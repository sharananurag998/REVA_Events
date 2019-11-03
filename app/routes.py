from app import app
from app.forms import LoginForm, AddEventForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask import request
from flask_login import login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Anurag'}
	return render_template('index.html', title='Home', user=user)

@app.route('/registrations')
@login_required
def registrations():
    user_name = request.args.get('name')
    return render_template('registration.html',user=user_name)

# @app.route('/login')
# def login():
# 	return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login2.html', title='Sign In', form=form)


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

# @app.route('/login2', methods=['GET', 'POST'])
# def login2():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect('/index')
#     return render_template('login2.html', title='Sign In', form=form)

@app.route('/certificates')
@login_required
def certificates():
	return render_template('certificates.html')

@app.route('/qrread')
@login_required
def qr():
	return render_template('qrreader.html')

@app.route('/evn_det')
def ev():
    evn_name = request.args.get('name')
    return render_template('event details.html',event_name = evn_name)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/payment-gateway')
def gateway():
    return render_template('gateway.html')

@app.route('/reset')
def reset():
    return render_template('reset.html')

@app.route('/add-event')
def add():
    form2 = AddEventForm()
    return render_template('add_event.html', form=form2)