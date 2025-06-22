from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    head_boy = db.Column(db.String(20))
    head_girl = db.Column(db.String(20))
    sports_prefect = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    user = db.relationship('User')