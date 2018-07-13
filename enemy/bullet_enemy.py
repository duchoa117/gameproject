from game_object import GameObject, game_objects
import  game_object
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall
# from input.input_manager import InputManager
class BulletEnemy(GameObject):
    def __init__(self, x, y, velocityX, velocityY):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        # 1 load image
        self.renderer = None
        self.width = 25
        self.height = 25
        self.box_collider = BoxCollider(self.width, self.height)
        self.velocityX = velocityX
        self.velocityY = velocityY
    def update(self):
        self.x += self.velocityX
        self.y += self.velocityY
    def render(self, canvas):
        GameObject.render(self,canvas)










