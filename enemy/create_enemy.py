from enemy.enemy import Enemy
from enemy.enemy1 import Enemy1

import game_object
def create_enemy():
    enemy = Enemy(31*16,13*16,"normal")
    game_object.add(enemy)
    enemy1 = Enemy1(3*16,3*16,0,4,4, "normal")
    game_object.add(enemy1)
    enemy12 = Enemy1(220,304,2,0,2, "invisible")
    game_object.add(enemy12)
    enemy12 = Enemy1(368, 272,0,-1, 1, "normal")
    game_object.add(enemy12)
    enemy12 = Enemy1(288, 108, 3, 0, 3, "normal")
    game_object.add(enemy12)



