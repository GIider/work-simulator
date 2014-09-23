# -*- coding: utf-8 -*-


class AbstractMoneyGeneratingEntity(object):
    """A abstract entity that generates money"""

    # The amount of dosh we generate each interval
    MONEY_GENERATED = None

    # The amount of seconds between each money generation
    MONEY_INTERVAL = None

    # The amount of money it costs to purchase this entity
    MONEY_COST = None


class Trainee(object):
    """A concrete entity that generates money"""

    MONEY_GENERATED = 10
    MONEY_INTERVAL = 5
    MONEY_COST = 1

    def __repr__(self):
        return 'Trainee'

AVAILABLE_ENTITIES = [Trainee]
