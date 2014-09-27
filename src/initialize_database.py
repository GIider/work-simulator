# -*- coding: utf-8 -*-
from work_simulator import models

PLAYER_NAMES = ('Glider', 'furinvader')

players = []
for player_name in PLAYER_NAMES:
    player = models.Player.create_if_not_exists(username=player_name)

    players.append(player)

trainee = models.Entity.create_if_not_exists(name='Azubi', money_generated=1, money_cost=0, money_interval=5)

for player_id in players:
    models.OwnedEntities.set_owned_amount_for_player(player_id=player_id, entity_id=trainee.id, amount=5)
