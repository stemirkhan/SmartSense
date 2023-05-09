from flask import render_template, url_for, redirect
from flask_login import login_user, current_user, login_required, logout_user

from app import app
from app.models import User, SensorReading, db
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for(endpoint='dashboard'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    readings_value = db.session.query(SensorReading).order_by(SensorReading.id.desc()).first()
    sensor_readings = (('Температура', readings_value.temperature),
                       ('Влажность', readings_value.humidity),
                       ('Угарный газ', readings_value.carbon_monoxide),
                       ('Атмосферное давление', readings_value.pressure))

    return render_template('dashboard.html', sensor_readings=sensor_readings, title='Dashboard')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('login')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
