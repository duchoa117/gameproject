from game_object import GameObject, game_objects, gamelevel
from game_object import add 
from renderers.image_renderer import ImageRenderer
from renderers.animation import Animation
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall
from enemy.enemy import Enemy
from enemy.enemy1 import Enemy1
from enemy.enemy_explosion import EnemyExplosion
import pygame

# from input.input_manager import InputManager

class BulletPlayer(GameObject):
    def __init__(self, x, y, dx, dy):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        # 1 load image
        self.width = 10
        self.height = 10
        self.box_collider = BoxCollider(self.width, self.height)
        self.dx = dx
        self.dy = dy
        self.dam = 5
        if self.dy > 0:
            self.renderer = ImageRenderer("assets/images/sprite/bullet_player/bullet_down.png")
        elif self.dy < 0:
            self.renderer = ImageRenderer("assets/images/sprite/bullet_player/bullet_up.png")
        elif self.dx > 0:
            self.renderer = ImageRenderer("assets/images/sprite/bullet_player/bullet_right.png")
        elif self.dx < 0:
            self.renderer = ImageRenderer("assets/images/sprite/bullet_player/bullet_left.png")
     

    def update(self):
        GameObject.update(self)
        self.x += self.dx
        self.y += self.dy
        
        
        for game_object in game_objects:
            if type(game_object) == Wall:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound("music/player/Boom.wav"))

                    self.deactivate()


        for game_object in game_objects:
            if type(game_object) == Enemy or type(game_object) == Enemy1:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound("music/player/Boom.wav"))
                    game_object.hp += -self.dam
                    if game_object.hp <= 0:
                        gamelevel.append("*")
                        enemy_explosion = EnemyExplosion(game_object.x, game_object.y, game_object.dx, game_object.dy, game_object._type)
                        add(enemy_explosion)
                        game_object.deactivate()
                    self.deactivate()
                
    def render(self, canvas):
        GameObject.render(self,canvas)

        


