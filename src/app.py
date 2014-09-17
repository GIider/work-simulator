# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, redirect, session, escape, flash

app = Flask(__name__)

# Generate a new secret key every time we restart to invalidate the session.
# If you want a persisting session while you modify files simply use a static string
app.secret_key = os.urandom(32)  # 'Bruce Schneier knows Alice and Bob\'s shared secret.'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=escape(session['username']))

    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            error = 'Username can\'t be blank!'
        else:
            session['username'] = username
            flash('You were logged in')
            return redirect('')

    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
