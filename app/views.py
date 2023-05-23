from flask import render_template, url_for, redirect, jsonify, request, flash
from flask_login import login_user, current_user, login_required, logout_user

from app import app
from app.models import User, SensorReading, db, ResetPasswordToken
from app.forms import LoginForm, ResetPasswordRequestForm, ResetPasswordForm
from app.email import send_password_reset_email


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

        flash('The entered email or password information is not correct.')

    return render_template('login.html', title='Sign In', form=form)


@app.route('/dashboard')
@app.route('/')
@login_required
def dashboard():
    readings_value = db.session.query(SensorReading).order_by(SensorReading.id.desc()).first()
    sensor_readings = (('Температура', 'temperature', readings_value.temperature),
                       ('Влажность', 'humidity', readings_value.humidity),
                       ('Угарный газ', 'carbon_monoxide', readings_value.carbon_monoxide),
                       ('Атмосферное давление', 'atmosphere_pressure', readings_value.pressure))

    if request.is_json:
        return jsonify({kit[1]: kit[2] for kit in sensor_readings})

    return render_template('dashboard.html', sensor_readings=sensor_readings, title='Dashboard')


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            jwt_token = ResetPasswordToken.query.filter_by(user_id=user.id).first()

            if not jwt_token:
                send_password_reset_email(user)
                flash('Password reset instructions have been sent to your email')
            else:
                flash('Password reset instructions were recently sent to your email')

            return redirect(url_for('login'))

        flash('User with such data does not exist')

    return render_template('forgot_password.html', title='Forgot Password', form=form)


@app.route('/reset_password/<reset_token>', methods=['GET', 'POST'])
def reset_password(reset_token):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    user = User.verify_reset_password_token(reset_token)
    if not user:
        return redirect(url_for('login'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password = form.password.data

        jwt_token = ResetPasswordToken.query.filter_by(user_id=user.id).first()

        db.session.delete(jwt_token)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('reset_password.html', title='Reset Password', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('login')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
