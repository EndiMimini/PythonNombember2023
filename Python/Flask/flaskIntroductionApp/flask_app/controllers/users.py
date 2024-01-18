from flask_app import app
from flask import render_template, request, session, redirect

from flask_app.models.user import User

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', users =User.get_all_users())
    return redirect('/controller')

@app.route('/user/<useri>')          # The "@" decorator associates this route with the function immediately following
def userProfile(useri):
    if 'user_id' in session:
        return render_template('user.html', useri=useri)
    return redirect('/controller')

