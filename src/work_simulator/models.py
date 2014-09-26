# -*- coding: utf-8 -*-
from flask.ext.restless import APIManager

from . import db, app

api_manager = APIManager(app, flask_sqlalchemy_db=db)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Player {}>'.format(self.name)


# models for which we want to create API endpoints
app.config['API_MODELS'] = {'player': Player}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {'player': Player}