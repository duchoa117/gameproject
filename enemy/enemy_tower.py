from game_object import GameObject, game_objects
from player.player import Player
import  game_object
from game_object import add

from renderers.image_renderer import ImageRenderer
from renderers.animation import Animation
from physics.box_collider import BoxCollider
from frame_counter import FrameCounter
from enemy.bullet_enemy import BulletEnemy 
import pygame

class EnemyTower(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self,x ,y)
        # 1 load image
        self.image_urls = ["assets/images/sprite/enemy/tower/tower1.png", "assets/images/sprite/enemy/tower/tower2.png", "assets/images/sprite/enemy/tower/tower3.png", "assets/images/sprite/enemy/tower/tower4.png"]
        self.renderer = Animation(self.image_urls, True)
        self.frame_counter = FrameCounter(100)
    def update(self):
        self.frame_counter.run()
        if self.frame_counter.expired :
            for game_object in game_objects:
                if type(game_object ) == Player:
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound("music/player/tower shoot.wav"))
                    bullet_enemy = BulletEnemy(11*16, 15*16, game_object.x, game_object.y)
                    
                    add(bullet_enemy)
                    self.frame_counter.reset()
    def render(self, canvas):
        GameObject.render(self,canvas)
    

