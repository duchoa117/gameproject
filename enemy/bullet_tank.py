from game_object import GameObject, game_objects
import  game_object
from renderers.animation import Animation
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall
class BulletTank(GameObject):
    def __init__(self,x ,y, dx, dy):
        GameObject.__init__(self,x ,y)
        self.dam = 30
        self.x = x
        self.y = y
        self.overlap = False
        self.dx = dx
        self.dy = dy
        # 1 load image
        self.renderer = Animation(["assets/images/sprite/enemy/bullet_tank/bullet_tank1.png", "assets/images/sprite/enemy/bullet_tank/bullet_tank2.png", "assets/images/sprite/enemy/bullet_tank/bullet_tank3.png"],True)
        self.width = 20
        self.height = 20
        self.box_collider = BoxCollider(self.width, self.height)
        
    def update(self):
        GameObject.update(self)
        self.check_deactive()
        self.x += self.dx*2
        self.y += self.dy*2
    def render(self, canvas):
        GameObject.render(self,canvas)
    
    def check_deactive(self):
        if self.x > 640 or self.x < 0:
            self.deactivate()
        if self.y > 480 or self.y < 0:
            self.deactivate()