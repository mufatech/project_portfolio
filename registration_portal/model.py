from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_registered = db.Column(db.digit(80), unique=True, nullable=False)
    pin = db.Column(db.digit(80), unique=True, nullable=False)
    fname = db.Column(db.String(80), unique=True, nullable=False)
    lname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(255), nullable=False)