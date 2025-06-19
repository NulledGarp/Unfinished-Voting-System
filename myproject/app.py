from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voters.db'
db = SQLAlchemy(app)

# Database model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Create DB/default demo user
@app.before_request
def create_demo_user():
    db.create_all()
    if not Student.query.filter_by(student_id="test123").first():
        demo_student = Student(student_id="test123", password="test123")
        db.session.add(demo_student)
        db.session.commit()

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        student_id = request.form['student_id']
        password = request.form['password']
        user = Student.query.filter_by(student_id=student_id).first()

        if user and user.password == password:
            return redirect(url_for('voters'))
        else:
            flash('Invalid credentials', 'error')

    return render_template('login.html')
# Admin login route
@app.route('/admin-login', methods=['GET', 'POST'])

# Voters route
@app.route('/voters')
def voters():
    return render_template('voters.html')
# Submit vote route
@app.route('/submit_vote', methods=['GET', 'POST'])
def submit_vote():
    if request.method == 'POST':
        head_boy = request.form.get('head_boy')
        head_girl = request.form.get('head_girl')
        # You can process/store the vote here if needed
        return render_template('submit_vote.html')
    return render_template('submit_vote.html')

if __name__ == '__main__':
    app.run(debug=True)