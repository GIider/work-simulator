# -*- coding: utf-8 -*-
from work_simulator import models

glider = models.Player.create_if_not_exists(username='Glider')
trainee = models.Entity.create_if_not_exists(name='Azubi', money_generated=1, money_cost=0, money_interval=5)

models.OwnedEntities.set_owned_amount_for_player(player_id=glider.id, entity_id=trainee.id, amount=5)