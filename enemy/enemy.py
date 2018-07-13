from game_object import GameObject, game_objects
import  game_object
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall

# from input.input_manager import InputManager

class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        # 1 load image
        self.renderer = ImageRenderer("assets/images/sprite/enemy/enemy1_down.png")
        self.width = 30
        self.height = 30
        self.box_collider = BoxCollider(self.width, self.height)
        self.dx = 0
        self.dy = 3

    def update(self):
        GameObject.update(self)

        self.box_collider.y = self.y + self.dy

        for game_object in game_objects:
            if type(game_object) == Wall:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.overlap = True
        if self.overlap:
            self.dy = - self.dy
        if self.dy > 0:
            self.renderer = ImageRenderer("assets/images/sprite/enemy/enemy1_down.png")

        else:

            self.renderer = ImageRenderer("assets/images/sprite/enemy/enemy1_up.png")

        self.y += self.dy
        self.overlap = False
        self.box_collider.y = self.y








    def render(self, canvas):
        GameObject.render(self,canvas)









