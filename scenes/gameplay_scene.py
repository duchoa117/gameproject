from player import create_player
from enemy import create_enemy
from gift import  create_gift, create_coin
from maps.map_generate_map import generate_map
import game_object
from player.player import Player
from input.input_manager import global_input_manager
from maps.background import Background


class GameplayScene:
    def __init__(self):
        pass
    
    def setup(self):
        game_object.add(Background())
        generate_map("assets/maps/map.json")
        player = Player(35*16,27*16, global_input_manager)
        game_object.add(player)
        create_enemy.create_enemy()
        create_gift.create_gift()
        create_coin.create_coin()

    def destroy(self):
        game_object.clear()