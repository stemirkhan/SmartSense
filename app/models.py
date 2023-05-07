from flask_login import UserMixin
from werkzeug.security import generate_password_hash,  check_password_hash

from . import db, login_manager

from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    user_name = db.Column(db.String(30), nullable=False)
    user_last_name = db.Column(db.String(30), nullable=False)
    data_register = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    telegram_login = db.Column(db.String(30), unique=True)
    telegram_notifications = db.Column(db.Boolean)

    def get_id(self):
        return self.user_id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User(id={self.user_id}, email={self.email}, user_name={self.user_name}'


class Role(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(10), nullable=False, unique=True)

    user = db.relationship('User', lazy='select')

    def __repr__(self):
        return f'Role(rile_id={self.role_id})'


class ServerAccessToken(db.Model):
    __tablename__ = 'server_access_tokens'

    token_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token_name = db.Column(db.String(30), nullable=False, unique=True)
    access_token = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return f"ServerAccessToken(token_id={self.token_id}, token_name={self.token_name})"


class SensorReading(db.Model):
    __tablename__ = 'sensor_readings'

    recording_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recording_time = db.Column(db.DateTime, default=datetime.utcnow)
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    carbon_monoxide = db.Column(db.Integer)
    humidity = db.Column(db.Float)

    def __repr__(self):
        return f'SensorReading(recording_id={self.recording_id})'


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
