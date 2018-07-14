from game_object import GameObject, game_objects
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from map_titles.wall import Wall
import game_object
from player.bullet_player import BulletPlayer
from frame_counter import FrameCounter

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
        self.speed = 4
        self.dx = 0
        self.dy = 0
        self.shootX = -6
        self.shootY = 0
        self.frame_counter = FrameCounter(10)
        self.shoot_lock = True
        self.can_shoot = False


    def update(self):
        self.move()
        self.shoot()

    def render(self, canvas):
        GameObject.render(self,canvas)

    def check_overlap(self):
        for game_object in game_objects:
            if type(game_object) == Wall:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.overlap = True

    def move(self):
        self.dx = 0
        self.dy = 0
        GameObject.update(self)
        if self.input_manager.up_pressed:
            self.shootX = 0
            self.shootY = -6
            self.renderer = ImageRenderer("assets/images/sprite/player_up.png")
            self.box_collider.y = self.y - self.speed
            self.check_overlap()
            if self.overlap:
                self.dy += 0
            else:
                self.dy += -self.speed
        elif self.input_manager.down_pressed:
            self.shootX = 0
            self.shootY = 6
            self.renderer = ImageRenderer("assets/images/sprite/player_down.png")
            self.box_collider.y = self.y + self.speed
            self.check_overlap()
            if self.overlap:
                self.dy += 0
            else:
                self.dy += self.speed
        elif self.input_manager.left_pressed:
            self.shootX = -6
            self.shootY = 0
            self.renderer = ImageRenderer("assets/images/sprite/player_left.png")
            self.box_collider.x = self.x - self.speed
            self.check_overlap()

            if self.overlap:
                self.dx += 0
            else:
                self.dx += -self.speed
        elif self.input_manager.right_pressed:
            self.shootX = 6
            self.shootY = 0
            self.renderer = ImageRenderer("assets/images/sprite/player_right.png")

            self.box_collider.x = self.x + 2
            self.check_overlap()
            if self.overlap:
                self.dx += 0
            else:
                self.dx += self.speed
        self.x += self.dx
        self.y += self.dy
        self.box_collider.x = self.x
        self.box_collider.y = self.y
        self.overlap = False

    def shoot(self):
        print(self.can_shoot)
        if self.can_shoot:
            if self.input_manager.x_pressed and not self.shoot_lock:
                bullet_player = BulletPlayer(self.x, self.y, self.shootX, self.shootY)
                game_object.add(bullet_player)
                self.shoot_lock = True
            if self.shoot_lock:
                self.frame_counter.run()
                if self.frame_counter.expired:
                    self.shoot_lock = False
                    self.frame_counter.reset()
                    
            