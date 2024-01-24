from flask import Flask
from flask import render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'some secret'

@app.route('/')
def counter():
    #llogjika per te rritur counterin
    if 'counter' in session:
        session['counter'] = session['counter']+ 1
        return render_template('counter.html', counter= session['counter'])
    session['counter'] = 1
    return render_template('counter.html', counter= session['counter'])



@app.route('/increase')
def counterIncreseByTwo():
    #llogjika per te rritur counterin
    if 'counter' in session:
        session['counter'] = session['counter']+ 2
        return render_template('counter.html', counter= session['counter'])
    session['counter'] = 1
    return render_template('counter.html', counter= session['counter'])
   
@app.route('/destroy_counter')
def destroyCounter():
    # llogjika per te fshire counterin
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)