from game_object import GameObject, game_objects
from player.player import Player
import  game_object
from renderers.image_renderer import ImageRenderer
from renderers.animation import Animation
from physics.box_collider import BoxCollider
import pygame

class Coin(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        # 1 load image
        self.image_urls = ["assets/images/sprite/gift/coinup.png", "assets/images/sprite/gift/coinup_2.png", "assets/images/sprite/gift/coin_down1.png", "assets/images/sprite/gift/coin_down.png"]
        self.renderer = Animation(self.image_urls, True)
        self.width = 20
        self.height = 20
        self.box_collider = BoxCollider(self.width, self.height)
    def update(self):
        GameObject.update(self)
        if not self.overlap:
            for game_object in game_objects:
                if type(game_object) == Player:
                    self.overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                    if self.overlap:
                        self.deactivate()
                        self.sound()
                        game_object.count_coin += 1


    def render(self, canvas):
        GameObject.render(self,canvas)
    def sound(self):
        pingo = pygame.mixer.Sound("music/player/player_get_coin.wav")
        pingo.play()
        


