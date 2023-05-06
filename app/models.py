from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    user_name = db.Column(db.String(30), nullable=False)
    user_last_name = db.Column(db.String(30), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    data_register = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    telegram_login = db.Column(db.String(30), unique=True)
    telegram_notifications = db.Column(db.Boolean)

    def __repr__(self):
        return f'User(id={self.id}, email={self.email}, user_name={self.user_name}'


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
