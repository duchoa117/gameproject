import game_object
import  pygame
from player.player import Player
def create_player(input_manager):
    player = Player(35*16,26*16+8, input_manager)
    game_object.add(player)
