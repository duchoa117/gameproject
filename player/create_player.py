import game_object
import  pygame
from player.player import Player
def create_player():
    player = Player(35*16,27*16)
    game_object.add(player)
