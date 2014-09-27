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
        """Initialize the Player instance"""
        self.name = name

        if money is None:
            money = self.STARTING_MONEY

        self.money = money

    def __repr__(self):
        return '<Player {}>'.format(self.name)

    @classmethod
    def create_if_not_exists(cls, username):
        """Retrieve a user from the database or create a new one"""
        existing_player = cls.query.filter_by(name=username).first()

        if existing_player is not None:
            return existing_player

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

    def __init__(self, name, money_generated, money_cost, money_interval):
        """Initialize a Entity instance"""
        self.name = name
        self.money_generated = money_generated
        self.money_cost = money_cost
        self.money_interval = money_interval

    def __repr__(self):
        return '<Entity {}>'.format(self.name)

    @classmethod
    def create_if_not_exists(cls, name, **kwargs):
        """Retrieve a entity from the database or create a new one"""
        existing_entity = cls.query.filter_by(name=name).first()

        if existing_entity is not None:
            return existing_entity

        new_entity = cls(name=name, **kwargs)
        db.session.add(new_entity)
        db.session.commit()

        return new_entity


class OwnedEntities(db.Model):
    """The table containing how much entities are owned by whom"""
    id = db.Column(db.Integer, primary_key=True)

    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    amount = db.Column(db.Integer)

    def __init__(self, player_id, entity_id, amount):
        self.player_id = player_id
        self.entity_id = entity_id
        self.amount = amount

    @classmethod
    def set_owned_amount_for_player(cls, player_id, entity_id, amount):
        """Set the amount of owned entities for a player"""
        currently_owned = cls.query.filter_by(player_id=player_id, entity_id=entity_id).first()

        if currently_owned is None:
            currently_owned = cls(player_id=player_id, entity_id=entity_id, amount=amount)

            db.session.add(currently_owned)
        else:
            currently_owned.amount = amount

        db.session.commit()
        return True


# Make sure all tables exist when we run for the first time
db.create_all()

# models for which we want to create API endpoints
app.config['API_MODELS'] = {'player': Player,
                            'entity': Entity}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {'player': Player,
                                 'entity': Entity}

api_manager.create_api(Player, methods=['GET', 'POST', 'DELETE'])
api_manager.create_api(Entity, methods=['GET', 'POST', 'DELETE'])