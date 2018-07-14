from game_object import GameObject, game_objects
from player.player import Player
import  game_object
from renderers.image_renderer import ImageRenderer
from renderers.animation import Animation
from physics.box_collider import BoxCollider


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
        GameObject.update(self)
        if not self.overlap:
            for game_object in game_objects:
                if type(game_object) == Player:
                    self.overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                    if self.overlap:
                        game_object.can_shoot = True
            if self.overlap:
                image_urls = ["assets/images/sprite/gift/gift_close.png", "assets/images/sprite/gift/gift_opening.png", "assets/images/sprite/gift/gift_open.png"]
                self.renderer = Animation(image_urls,False)
                self.renderer = ImageRenderer("assets/images/sprite/gift/gift_open.png")


    def render(self, canvas):
        GameObject.render(self,canvas)


