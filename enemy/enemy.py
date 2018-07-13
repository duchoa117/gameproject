from game_object import GameObject, game_objects
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from map_titles.wall import Wall

# from input.input_manager import InputManager

class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        # 1 load image
        self.input_manager = input_manager
        self.renderer = ImageRenderer("assets/images/sprite/player_left.png")
        self.width = 20
        self.height = 20
        self.box_collider = BoxCollider(self.width, self.height)
        self.dx = 0
        self.dy = 0

    def update(self):
        self.dx = 0
        self.dy = 0
        GameObject.update(self)
        if self.input_manager.up_pressed:
            self.renderer = ImageRenderer("assets/images/sprite/player_up.png")
            self.box_collider.y = self.y - 2
            check_overlap()
            if self.overlap:
                self.dy += 0
            else:
                self.dy += -2
        elif self.input_manager.down_pressed:
            self.renderer = ImageRenderer("assets/images/sprite/player_down.png")
            self.box_collider.y = self.y + 2
            check_overlap()
            if self.overlap:
                self.dy += 0
            else:
                self.dy += +2
        elif self.input_manager.left_pressed:
            self.renderer = ImageRenderer("assets/images/sprite/player_left.png")
            self.box_collider.x = self.x - 2
            check_overlap()
            if self.overlap:
                self.dx += 0
            else:
                self.dx += -2
        elif self.input_manager.right_pressed:
            self.renderer = ImageRenderer("assets/images/sprite/player_right.png")
            self.box_collider.x = self.x + 2
            check_overlap()
            if self.overlap:
                self.dx += 0
            else:
                self.dx += 2
        reset_overlap()
    def render(self, canvas):
        GameObject.render(self,canvas)

    def check_overlap(self):
        for game_object in game_objects:
            if type(game_object) == Wall:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.overlap = True
    def reset_overlap(self):
        self.x += self.dx
        self.y += self.dy
        self.box_collider.x = self.x
        self.box_collider.y = self.y
        self.overlap = False







