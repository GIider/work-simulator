# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request, redirect, session

import decorator
import player
import exception

app = Flask(__name__)

# Use os.urandom(32) to generate a new secret key every time we restart
# to invalidate the session.
# If you want a persisting session while you modify files simply use a static
# string

app.secret_key = 'Bruce Schneier knows Alice and Bob\'s shared secret.'  # os.urandom(32)


@app.route('/')
def index():
    return redirect('/pages')


@app.route('/pages')
@app.route('/pages/<page>')
def pages(page='index'):
    return render_template('pages/{}.html'.format(page))


@app.route('/pages/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            error = 'Username can\'t be blank!'
        else:
            session['player'] = player.Player.get_player_from_database(username=username).serialized_player
            return redirect('')

    return render_template('pages/login.html', error=error)


@app.route('/pages/logout')
def logout():
    if 'player' in session:
        session.pop('player')

    return redirect('/')


@app.route('/game')
@app.route('/game/<page>')
@decorator.login_required
def game(page='index'):
    # Workaround to always be up to date
    username = session['player']['username']
    session['player'] = player.Player.get_player_from_database(username=username).serialized_player

    return render_template('game/{}.html'.format(page))


@app.route('/game/purchase/<entity>')
@decorator.login_required
def purchase(entity):
    username = session['player']['username']
    player_instance = player.Player.get_player_from_database(username=username)

    error = None
    try:
        player_instance .acquire_entity(entity)
    except exception.NotEnoughMoneyException:
        error = 'Not enough funds!'

    session['player'] = player.Player.get_player_from_database(username=username).serialized_player

    return render_template('game/acquirebondsman.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
