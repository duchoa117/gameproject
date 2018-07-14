from game_object import GameObject
from renderers.image_renderer import ImageRenderer

class Background(GameObject):
    def __init__(self):
        GameObject.__init__(self, 320, 240)
        self.renderer = ImageRenderer("assets/images/36987938_870119473192633_6676325747356860416_n.png")
    