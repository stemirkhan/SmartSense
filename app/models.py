from flask_login import UserMixin
from werkzeug.security import generate_password_hash,  check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property

from app import db, login_manager

from datetime import datetime


class RoleUser(db.Model):
    __tablename__ = 'roles_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    users = db.relationship('RoleUser', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'Role(rile_id={self.id})'


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    _password_hash = db.Column(db.String(500), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    data_register = db.Column(db.DateTime, default=datetime.utcnow)
    telegram_login = db.Column(db.String(30), unique=True, nullable=True)
    telegram_notifications = db.Column(db.Boolean)

    roles = db.relationship('RoleUser', backref='role', lazy=True, cascade='all, delete-orphan')

    def get_id(self):
        return self.id

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password_hash, password)

    def __repr__(self):
        return f'User(id={self.id}, email={self.email}, user_name={self.name})'


class ServerAccessToken(db.Model):
    __tablename__ = 'server_access_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    access_token = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return f"ServerAccessToken(token_id={self.id}, token_name={self.name})"


class SensorReading(db.Model):
    __tablename__ = 'sensor_readings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    carbon_monoxide = db.Column(db.Integer)
    humidity = db.Column(db.Float)

    def __repr__(self):
        return f'SensorReading(recording_id={self.id})'


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
