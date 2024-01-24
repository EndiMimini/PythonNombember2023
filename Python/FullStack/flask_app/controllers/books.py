from flask_app import app
from flask import render_template, redirect, flash, session


@app.route('/books')
def books():
    if 'user_id' in session:
        return render_template('books.html')
    return redirect('/')

