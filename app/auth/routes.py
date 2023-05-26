from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required

from . import bp_auth
from app.models import User, ResetPasswordToken, db
from .forms import LoginForm, ResetPasswordForm, ResetPasswordRequestForm
from .email import send_password_reset_email


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('general.dashboard'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for(endpoint='general.dashboard'))

        flash('The entered email or password information is not correct.')

    return render_template('login.html', title='Sign In', form=form)


@bp_auth.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('general.dashboard'))

    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            token = ResetPasswordToken.query.filter_by(user_id=user.id).first()

            if not token or not User.verify_reset_password_token(token.jwt_token):
                send_password_reset_email(user)
                flash('Password reset instructions have been sent to your email')
            else:
                flash('Password reset instructions were recently sent to your email, try later')

            if token and not User.verify_reset_password_token(token.jwt_token):
                db.session.delete(token)
                db.session.commit()

            return redirect(url_for('auth.login'))

        flash('User with such data does not exist')

    return render_template('forgot_password.html', title='Forgot Password', form=form)


@bp_auth.route('/reset_password/<reset_token>', methods=['GET', 'POST'])
def reset_password(reset_token):
    if current_user.is_authenticated:
        return redirect(url_for('general.dashboard'))

    user = User.verify_reset_password_token(reset_token)
    if not user:
        flash('The password reset link has expired')
        return redirect(url_for('auth.login'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password = form.password.data

        jwt_token = ResetPasswordToken.query.filter_by(user_id=user.id).first()

        db.session.delete(jwt_token)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('reset_password.html', title='Reset Password', form=form)


@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('login')
