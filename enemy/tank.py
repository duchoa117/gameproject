from game_object import GameObject, game_objects
import  game_object
from renderers.image_renderer import ImageRenderer
from enemy.enemy_animator import EnemyAnimator
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall
from random import choice


# from input.input_manager import InputManager
class Tank(GameObject):
    def __init__(self, x, y, dx, dy, speed):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        self.die = False
        # 1 load image
        self.renderer = EnemyAnimator()
        self.width = 20
        self.height = 20
        self.box_collider = BoxCollider(self.width, self.height)
        self.directory = [1,2,3,4]
        self.speed = speed
        self.dx = 0
        self.dy = self.speed
        self.hp = 15

    def update(self):
        GameObject.update(self)
        self.renderer.update(self.dx, self.dy, self.die)
        if self.x > 520:
            self.dx = -self.speed
            self.dy = 0
        else:
            self.check_overlap()

            if not self.overlap:
                self.directory = [1,2,3,4]
            else:
                if len(self.directory) == 0:
                    self.directory = [1, 2, 3, 4]
                move  = choice(self.directory)
                if move == 1:
                    self.dy = self.speed
                    self.dx = 0
                elif move == 2:
                    self.dy = -self.speed
                    self.dx = 0
                elif move == 3:
                    self.dx = self.speed
                    self.dy = 0
                elif move == 4:
                    self.dx = -self.speed
                    self.dy = 0
                self.reset_boxcollide()
                self.check_overlap()
                if self.overlap:
                    self.directory.remove(move)

        
        self.x += self.dx
        self.y += self.dy
        self.overlap = False
        


    def render(self, canvas):
        GameObject.render(self,canvas)
        self.renderer.render(canvas, self.x , self.y)
        if self.die:
            self.deactivate()
       

    def reset_boxcollide(self):
        self.box_collider.y = self.y
        self.box_collider.x = self.x


    def check_overlap(self):
        self.box_collider.y = self.y + self.dy
        self.box_collider.x = self.x + self.dx
        for game_object in game_objects:
            if type(game_object) == Wall:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.overlap = True
