from enemy.enemy import Enemy
from enemy.enemy1 import Enemy1

import game_object
def create_enemy():
    enemy = Enemy(31*16,13*16)
    game_object.add(enemy)
    enemy1 = Enemy1(3*16,3*16)
    game_object.add(enemy1)



