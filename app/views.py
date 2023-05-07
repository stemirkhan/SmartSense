from flask import render_template, url_for, redirect
from flask_login import login_user, current_user

from app import app
from app.models import User
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for(endpoint='dashboard'))

    return render_template('login.html', title='Sign In', form=form)
