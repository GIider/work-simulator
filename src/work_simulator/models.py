# -*- coding: utf-8 -*-
from flask.ext.restless import APIManager

from . import db, app

api_manager = APIManager(app, flask_sqlalchemy_db=db)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    money = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Player {}>'.format(self.name)

# Make sure all tables exist when we run for the first time
db.create_all()

# models for which we want to create API endpoints
app.config['API_MODELS'] = {'player': Player}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {'player': Player}

api_manager.create_api(Player, methods=['GET', 'POST', 'DELETE'])