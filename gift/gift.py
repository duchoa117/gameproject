from game_object import GameObject, game_objects
import  game_object
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall
# from input.input_manager import InputManager
class Gift(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        # 1 load image
        self.renderer = ImageRenderer("assets/images/sprite/gift/gift_close.png")
        self.width = 25
        self.height = 25
        self.box_collider = BoxCollider(self.width, self.height)
    def update(self):
        game_object.update()
    def render(self, canvas):
        GameObject.render(self,canvas)


