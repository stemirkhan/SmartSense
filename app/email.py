from flask import render_template
from flask_mail import Message

from app import mail, app

from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body

    sender = Thread(target=send_async_email, args=(app, msg))
    sender.start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()

    send_email('[SmartSense] Reset Your Password',
               sender=app.config['MAIL_USERNAME'], recipients=[user.email],
               html_body=render_template('email/message_reset_password.html', user=user, token=token))
