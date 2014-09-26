# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session

from . import app, decorator, player, exception


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
