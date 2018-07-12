from game_object import GameObject
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider

class Wall(GameObject):
    def __init__(self, x, y, path):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer(path)
        self.box_collider = BoxCollider(16,16)

    def render(self, canvas):
        GameObject.render(self, canvas)
