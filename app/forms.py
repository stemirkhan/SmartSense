from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    remember = BooleanField("Remember me", default=False)
