# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request, redirect, session

import decorator

app = Flask(__name__)

# Generate a new secret key every time we restart to invalidate the session.
# If you want a persisting session while you modify files simply use a static
# string

# 'Bruce Schneier knows Alice and Bob\'s shared secret.'
app.secret_key = os.urandom(32)


@app.route('/')
def index():
    return redirect('/pages')


@app.route('/pages')
@app.route('/pages/<page>')
def pages(page='index'):
    username = ''
    if 'username' in session:
        username = session['username']

    return render_template('pages/{}.html'.format(page),
                           username=username)


@app.route('/pages/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            error = 'Username can\'t be blank!'
        else:
            session['username'] = username
            return redirect('')

    return render_template('pages/login.html', error=error)


@app.route('/pages/logout')
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect('/')


@app.route('/game')
@app.route('/game/<page>')
@decorator.login_required
def game(page='index'):
    return render_template('game/{}.html'.format(page))


if __name__ == '__main__':
    app.run(debug=True)
