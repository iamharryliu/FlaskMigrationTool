from WebApp import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(16))
    signup_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    birth_date = db.Column(db.DateTime, nullable=False, default=datetime(1995, 3, 1))

