from game_object import GameObject, game_objects
import  game_object
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall
class BulletEnemy(GameObject):
    def __init__(self,x ,y, x_player, y_player):
        GameObject.__init__(self,x ,y)
        self.dam = 30
        self.x = x
        self.y = y
        self.overlap = False
        self.x_player = x_player
        self.y_player = y_player
        # 1 load image
        self.renderer = ImageRenderer("assets/images/sprite/enemy/tower/tower_bullet.png")
        self.width = 20
        self.height = 20
        self.box_collider = BoxCollider(self.width, self.height)
        self.vectorX = self.x_player - self.x
        self.vectorY =  self.y_player - self.y
        self.velocityX = self.vectorX/((self.vectorX**2 + self.vectorY**2)**(1/2))*10
        self.velocityY = self.vectorY/((self.vectorX**2 + self.vectorY**2)**(1/2))*10
    def update(self):
        GameObject.update(self)
        self.check_deactive()
        self.x += self.velocityX
        self.y += self.velocityY

    def render(self, canvas):
        GameObject.render(self,canvas)
    
    def check_deactive(self):
        if self.x > 640 or self.x < 0:
            self.deactivate()
        if self.y > 480 or self.y < 0:
            self.deactivate()










