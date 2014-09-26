# -*- coding: utf-8 -*-
from collections import defaultdict

from . import exception, game


class Player(object):
    """A player"""

    def __init__(self, username):
        # A dictionary of entity: amount owned
        self.owned_entities = defaultdict(int)  # {entity: 0 for entity in game.AVAILABLE_ENTITIES}
        self.money = 10
        self.username = username

    # Fake stub
    @classmethod
    def get_player_from_database(cls, username):
        """Fetch a player from the database"""
        # TODO: Look into flask logging
        player = DATABASE.get(username, None)
        if player is None:
            print('Creating new player object "%s"' % username)
            player = cls(username=username)
            DATABASE[username] = player
        else:
            print('Restoring player "%s" from database' % username)

        return player

    def acquire_entity(self, entity_id):
        """Acquire a new entity"""
        # TODO: Error handling
        entity_id = int(entity_id)

        entity = game.AVAILABLE_ENTITIES.get(entity_id, None)
        if entity is None:
            raise ValueError('%d is not a valid entity id!')

        assert issubclass(entity, game.AbstractMoneyGeneratingEntity)

        # TODO: Wrap this so it can be shown on the interface
        if self.money < entity.MONEY_COST:
            raise exception.NotEnoughMoneyException()

        self.money -= entity.MONEY_COST
        self.owned_entities[entity.__class__] += 1

        return True

    @property
    def serialized_player(self):
        """Serialized version of a player attribute to keep in the session

        As the Player object becomes more complex we might need to do some
        real serialising to keep the player object in the session.
        """
        serialized = self.__dict__.copy()
        serialized.pop('owned_entities')

        return serialized

DATABASE = {}
