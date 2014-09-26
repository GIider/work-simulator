# -*- coding: utf-8 -*-
from flask.ext.restless import APIManager

from . import db, app

api_manager = APIManager(app, flask_sqlalchemy_db=db)


class Player(db.Model):
    """The table containing all players"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    money = db.Column(db.Integer)

    STARTING_MONEY = 100

    def __init__(self, name, money=None):
        self.name = name

        if money is None:
            money = self.STARTING_MONEY

        self.money = money

    def __repr__(self):
        return '<Player {}>'.format(self.name)

    @classmethod
    def create_if_not_exists(cls, username):
        """Retrieve a user from the database or create a new one"""
        result = cls.query.filter_by(name=username).first()

        if result is not None:
            return result

        new_player = cls(name=username)
        db.session.add(new_player)
        db.session.commit()

        return new_player


class Entity(db.Model):
    """The table containing all entities"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    money_generated = db.Column(db.Integer)
    money_cost = db.Column(db.Integer)
    money_interval = db.Column(db.Integer)

    def __repr__(self):
        return '<Entity {}>'.format(self.name)


class OwnedEntities(db.Model):
    """The table containing how much entities are owned by whom"""
    id = db.Column(db.Integer, primary_key=True)

    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    owned = db.Column(db.Integer)

# Make sure all tables exist when we run for the first time
db.create_all()

# models for which we want to create API endpoints
app.config['API_MODELS'] = {'player': Player}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {'player': Player}

api_manager.create_api(Player, methods=['GET', 'POST', 'DELETE'])
api_manager.create_api(Entity, methods=['GET', 'POST', 'DELETE'])
api_manager.create_api(OwnedEntities, methods=['GET', 'POST', 'DELETE'])
