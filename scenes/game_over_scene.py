import game_object
from gameover.gameover import GameOver


class GameOverScene:
    def __init__(self):
        pass

    def setup(self):
        game_over_scene = GameOver(320, 240)
        game_object.add(game_over_scene)

    def destroy(self):
        game_object.clear()