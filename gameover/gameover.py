from renderers.image_renderer import ImageRenderer
from game_object import GameObject



class GameOver(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("assets/images/sprite/tải xuống.png")
