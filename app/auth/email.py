from flask import render_template, current_app
from flask_mail import Message

from app import mail
from app.models import ResetPasswordToken, db

from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, html_body):
    app = current_app._get_current_object()
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    sender = Thread(target=send_async_email, args=(app, msg))
    sender.start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()

    current_token = ResetPasswordToken(jwt_token=token, user_id=user.id)
    db.session.add(current_token)
    db.session.commit()

    send_email('[SmartSense] Reset Your Password',
               sender=current_app.config['MAIL_USERNAME'], recipients=[user.email],
               html_body=render_template('auth/email/message_reset_password.html', user=user, token=token))
