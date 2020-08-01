from WebApp import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    signup_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    birth_date = db.Column(db.DateTime, nullable=False, default=datetime(1995, 3, 1))
    postal_code = db.Column(db.String, nullable=False, default="M1E XXX")
    total_saved = db.Column(db.Integer, nullable=False, default=0)
    transactions = db.relationship(
        "Transaction", backref="owner", cascade="all,delete", lazy=True
    )


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    merchant_name = db.Column(db.String)
    category = db.Column(db.String)
