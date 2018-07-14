from game_object import GameObject, game_objects
import  game_object
from enemy.enemy_animator import EnemyAnimator
from physics.box_collider import BoxCollider
from physics import box_collider
from map_titles.wall import Wall

# from input.input_manager import InputManager

class Enemy(GameObject):
    def __init__(self, x, y, _type):
        GameObject.__init__(self,x ,y)
        self._type = _type
        self.overlap = False
        self.die = False
        # 1 load image
        self.renderer = EnemyAnimator(self._type)
        self.width = 20
        self.height = 20
        self.box_collider = BoxCollider(self.width, self.height)
        self.dx = 0
        self.dy = 3
        self.hp = 10

    def update(self):
        GameObject.update(self)
        self.renderer.update(self.dx, self.dy, self.die)

        self.box_collider.y = self.y + self.dy

        for game_object in game_objects:
            if type(game_object) == Wall:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.overlap = True
        if self.overlap:
            self.dy = - self.dy
        
        self.y += self.dy
        self.overlap = False
        self.box_collider.y = self.y
        


    def render(self, canvas):
        GameObject.render(self,canvas)
        self.renderer.render(canvas, self.x , self.y)
        if self.die:
            self.deactivate()









