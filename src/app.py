# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session, escape

app = Flask(__name__)
app.secret_key = 'Bruce Schneier knows Alice and Bob\'s shared secret.'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])

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
            return redirect('')

    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
