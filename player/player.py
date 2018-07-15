from game_object import GameObject, game_objects, gamelevel
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from map_titles.wall import Wall
import game_object
from player.bullet_player import BulletPlayer
from frame_counter import FrameCounter
from enemy.enemy import Enemy
from enemy.enemy1 import Enemy1
from enemy.bullet_tank import BulletTank
from enemy.bullet_enemy import BulletEnemy
import pygame
from scenes.game_over_scene import GameOverScene
from scenes.scene_manager import global_scene_manager
# from input.input_manager import global_input_manager


# from input.input_manager import InputManager

class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self,x ,y)
        self.overlap = False
        # 1 load image
        self.renderer = ImageRenderer("assets/images/sprite/player_left.png")
        self.width = 15
        self.height = 15
        self.box_collider = BoxCollider(self.width, self.height)
        self.speed = 4
        self.dx = 0
        self.dy = 0
        self.shootX = -6
        self.shootY = 0
        self.frame_counter = FrameCounter(10)
        self.shoot_lock = True
        self.can_shoot = False
        self.hp = 100
        self.count_coin = 0
        self.count_enemy = 0
        self.input_manager = input_manager


    def update(self):
        if len(gamelevel) == 8:
            self.lose()

        self.move()
        self.shoot()
        self.check_overlap_with_enemy()


    def render(self, canvas):
        GameObject.render(self,canvas)
        pygame.draw.rect(canvas, (173, 1, 1), pygame.Rect(200,10 , self.hp, 10))


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
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("music/player/player_move.wav"))
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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("music/player/player_move.wav"))
            
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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("music/player/player_move.wav"))
            
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
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("music/player/player_move.wav"))

            
            self.shootX = 6
            self.shootY = 0
            self.renderer = ImageRenderer("assets/images/sprite/player_right.png")

            self.box_collider.x = self.x + self.speed
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
        if len(gamelevel) == 3:
            enemy = Enemy1(6*16, 13.5*16, 5, 0, 5, "tank")
            enemy.hp = 50
            enemy1 = Enemy1(10*16, 3*16, -2, 0, 2, "tank")
            enemy1.hp = 50
            game_object.add(enemy)
            game_object.add(enemy1)
            gamelevel.append("*")
            

    def shoot(self):
        if self.can_shoot:
            if self.input_manager.x_pressed and not self.shoot_lock:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("music/player/player_shoot.wav"))
                bullet_player = BulletPlayer(self.x, self.y, self.shootX, self.shootY)
                game_object.add(bullet_player)
                self.shoot_lock = True
            if self.shoot_lock:
                self.frame_counter.run()
                if self.frame_counter.expired:
                    self.shoot_lock = False
                    self.frame_counter.reset()
            
    def lose(self):
        global_scene_manager.change_scene(GameOverScene())
        gamelevel.clear()

    def check_overlap_with_enemy(self):
        for game_object in game_objects:
            if type(game_object) == Enemy or type(game_object) == Enemy1:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.lose()
        for game_object in game_objects:
            if type(game_object) == BulletEnemy or type(game_object) == BulletTank:
                overlap = BoxCollider.overlap(self.box_collider, game_object.box_collider)
                if overlap:
                    self.hp += - game_object.dam
                    game_object.deactivate()
                    if self.hp <= 0 :
                        self.lose()



                
        
                    
            