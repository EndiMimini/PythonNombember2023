from flask_app import app
from flask import render_template, request, session, redirect, flash,jsonify

from flask_app.models.user import User


@app.route('/loginPage')
def loginPage():
    if 'user_id' not in session:
        return render_template('login.html')
    return redirect('/controller')

@app.route('/registerPage')
def registerPage():
    if 'user_id' not in session:
        return render_template('register.html')
    return redirect('/controller')

@app.route('/controller')
def controller():
    if 'user_id' not in session:
        return redirect('/loginPage')
    else:
        return redirect('/')
    
@app.route('/register', methods=['POST'])
def register():
    if 'user_id' not in session:
        if len(request.form['email'])<1 or len(request.form['firstName'])<2  or len(request.form['lastName'])<2  or len(request.form['password'])<8:
            flash('Te dhena te pasakta', 'registerError')
            return redirect(request.referrer)
        data = {
            'email': request.form['email'],
            'firstName': request.form['firstName'],
            'lastName': request.form['lastName'],
            'password': request.form['password']
        }
        session['user_id']= User.save_user(data)
        return redirect('/controller')
    return redirect('/controller')
    
@app.route('/login', methods=['POST'])
def login():
    if 'user_id' not in session:
        if len(request.form['email'])<1 or len(request.form['password'])<8:
            flash('Te dhena te pasakta', 'loginError')
            return redirect(request.referrer)
        data = {
            'email': request.form['email'],
            'password': request.form['password']
        }
    
        if not User.get_user_by_email(data):
            flash('The email does not exists', 'loginError')
            return redirect(request.referrer)
        
        user = User.get_user_by_email(data)
        if request.form['password'] != user['password']:
            flash('Incorrect password', 'loginError')
            return redirect(request.referrer)
        session['user_id'] = user['id']
        return redirect('/controller')

       
    return redirect('/controller')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/controller')