from app import app
from app import db
from app.forms import LoginForm, AddEventForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app.models import User, Event
from flask_login import logout_user
from flask import request
from flask_login import login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
def index():
    events = Event.query.all()
    first_event = Event.query.filter_by(id=1)
    return render_template('index.html', title='Home',events=events, first=first_event)

@app.route('/registrations')
@login_required
def registrations():
    user_name = request.args.get('name')
    return render_template('registration.html',user=user_name)

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
    events = Event.query.all()
    return render_template('Event_Calandar1.html', events = events)

@app.route('/certificates')
@login_required
def certificates():
	return render_template('certificates.html')

@app.route('/qrread')
@login_required
def qr():
	return render_template('qrreader.html')

@app.route('/branch')
@login_required
def brn():
    branch = request.args.get('br')
    events = Event.query.filter_by(branch=branch).all()
    return render_template('branch_event.html', branch=branch, events=events)

@app.route('/qrgen')
@login_required
def qrg():
	return render_template('qrgenerator.html')

@app.route('/evn_det')
def ev():
    evn_id = request.args.get('id')
    event = Event.query.get(evn_id)
    return render_template('event details.html',event=event)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/payment-gateway')
def gateway():
    evn_id = request.args.get('id')
    event = Event.query.get(evn_id)
    return render_template('gateway.html',event=event)

@app.route('/reset')
def reset():
    return render_template('reset.html')

@app.route('/add-event', methods=['GET', 'POST'])
def add():
    form = AddEventForm()
    if form.validate_on_submit():
        event = Event(name=form.name.data, body=form.body.data, venue=form.venue.data, branch=form.branch.data, image=form.image.data, timestamp = form.timestamp.data)
        db.session.add(event)
        db.session.commit()
        return redirect('/evn_det')
    return render_template('add_event.html',  form=form)


@app.route('/MyProfile')
def profile():
    return render_template('profile.html')

@app.route('/MyEvents')
def MyEve():
    events = Event.query.all()
    return render_template('MyEvents.html', events=events)

@app.route('/google_calendar')
def google_cal():
    return render_template('calendar.html')
