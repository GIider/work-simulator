# -*- coding: utf-8 -*-


class AbstractMoneyGeneratingEntity(object):
    """A abstract entity that generates money"""

    # Numeric ID of the entity
    ID = None

    # The amount of dosh we generate each interval
    MONEY_GENERATED = None

    # The amount of seconds between each money generation
    MONEY_INTERVAL = None

    # The amount of money it costs to purchase this entity
    MONEY_COST = None


class Trainee(AbstractMoneyGeneratingEntity):
    """A concrete entity that generates money"""

    ID = 1
    MONEY_GENERATED = 10
    MONEY_INTERVAL = 5
    MONEY_COST = 1

    def __repr__(self):
        return 'Trainee'

# A dictionary of all entities that are available for purchase
AVAILABLE_ENTITIES = {Trainee.ID: Trainee}
