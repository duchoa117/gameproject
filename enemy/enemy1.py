from game_object import GameObject, game_objects
import  game_object
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall
from random import choice


# from input.input_manager import InputManager
class Enemy1(GameObject):
    def __init__(self, x, y, dx, dy, speed):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        # 1 load image
        self.renderer = ImageRenderer("assets/images/sprite/enemy/enemy1_down.png")
        self.width = 25
        self.height = 25
        self.box_collider = BoxCollider(self.width, self.height)
        self.directory = [1,2,3,4]
        self.speed = speed
        self.dx = dx
        self.dy = dy

    def update(self):
        GameObject.update(self)
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

        if self.dy > 0:
            
            self.renderer = ImageRenderer("assets/images/sprite/enemy/enemy1_down.png")
        elif self.dy < 0:
            self.renderer = ImageRenderer("assets/images/sprite/enemy/enemy1_up.png")
        elif self.dx > 0:
            self.renderer = ImageRenderer("assets/images/sprite/enemy/enemy1_right.png")
        elif self.dx < 0:
            self.renderer = ImageRenderer("assets/images/sprite/enemy/enemy1_left.png")
        self.x += self.dx
        self.y += self.dy
        self.overlap = False









    def render(self, canvas):
        GameObject.render(self,canvas)

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
