from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, User

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        student_id = request.form['student_id']
        password = request.form['password']
        user = User.query.filter_by(student_id=student_id, password=password).first()
        if user and user.is_admin:
            session['admin'] = True
            return redirect('/admin')
        flash("Access denied or invalid credentials.")
    return render_template('admin_login.html')

@app.route('/admin')
def admin_panel():
    if not session.get('admin'):
        return "Access Denied", 403
    return render_template('admin.html')

@app.route('/vote')
def vote():
    return render_template('voters.html')

