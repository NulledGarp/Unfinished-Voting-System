from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voters.db'
db = SQLAlchemy(app)

# ...existing Student model and create_demo_user...

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

# --- ADMIN LOGIN ROUTE ---
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        admin_id = request.form['student_id']
        password = request.form['password']
        # For demo, hardcode admin credentials or check from DB
        if admin_id == "admin" and password == "adminpass":
            session['admin'] = True
            return redirect(url_for('admin_panel'))
        else:
            flash("Access denied or invalid credentials.")
    return render_template('admin.html')

# --- ADMIN PANEL ROUTE ---
@app.route('/admin')
def admin_panel():
    if not session.get('admin'):
        return "Access Denied", 403
    return render_template('admin_panel.html')

# --- LOGOUT ROUTE ---
@app.route('/logout-admin')
def logout_admin():
    session.pop('admin', None)
    return redirect(url_for('admin_login'))

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