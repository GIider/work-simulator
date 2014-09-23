# -*- coding: utf-8 -*-
from collections import defaultdict

import game


class Player(object):
    """A player"""

    def __init__(self, username):
        # A dictionary of entity: amount owned
        self.owned_entities = defaultdict(int)  # {entity: 0 for entity in game.AVAILABLE_ENTITIES}
        self.money = 0
        self.username = username

    # Fake stub
    @classmethod
    def get_player_from_database(cls, username):
        """Fetch a player from the database"""
        player = cls(username=username)

        return player

    def acquire_entity(self, entity):
        """Acquire a new entity"""
        assert isinstance(entity, game.AbstractMoneyGeneratingEntity)

        # TODO: Wrap this so it can be shown on the interface
        if self.money < entity.MONEY_COST:
            raise ValueError('Not enough money to purchase entity!')

        self.money -= entity.MONEY_COST
        self.owned_entities[entity.__class__] += 1

        return True

    @property
    def serialized_player(self):
        return self.__dict__