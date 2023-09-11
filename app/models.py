import os
import base64
from app import db, login
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(75), nullable=False, unique=True)
    username = db.Column(db.String(75), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))

    def _repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_attempt):
        return check_password_hash(self.password, password_attempt)
    
    def get_token(self, expires=3600):
        now = datetime.utcnow
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now +timedelta(seconds=expires)
        db.session.commit()
        return self.token
    
    def remove_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username
        }

@login.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

class Dilemma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=False)
    c_score = db.Column(db.Float, nullable=False, default=0)
    d_score = db.Column(db.Float, nullable=False, default=0)
    v_score = db.Column(db.Float, nullable=False, default=0)
    n_score = db.Column(db.Float, nullable=False, default=0)
    choice_a = db.Column(db.String(25), nullable=False)
    choice_b = db.Column(db.String(25), nullable=False)
