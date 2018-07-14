from renderers.animation import Animation
class EnemyAnimator:
    def __init__(self, _type):
        self._type = _type
        if self._type == "normal":
            self.down = Animation(["assets/images/sprite/enemy/enemy1_down.png","assets/images/sprite/enemy/enemy1_down1.png" ], True)
            self.up =  Animation(["assets/images/sprite/gift/coinup.png", "assets/images/sprite/gift/coinup_2.png", "assets/images/sprite/gift/coin_down1.png", "assets/images/sprite/gift/coin_down.png"], True)
            self.right = Animation(["assets/images/sprite/gift/coinup.png", "assets/images/sprite/gift/coinup_2.png", "assets/images/sprite/gift/coin_down1.png", "assets/images/sprite/gift/coin_down.png"], True)
            self.left = Animation(["assets/images/sprite/enemy/enemy1_left.png", "assets/images/sprite/enemy/enemy1_left1.png"], True)
        elif self._type == "invisible":
            self.down = Animation(["assets/images/sprite/enemy/enemy2_down.png","assets/images/sprite/enemy/enemy2_down1.png" ], True)
            self.up =  Animation(["assets/images/sprite/enemy/enemy2_up.png","assets/images/sprite/enemy/enemy2_down1.png" ], True)
            self.right = Animation(["assets/images/sprite/enemy/enemy2_right.png","assets/images/sprite/enemy/enemy2_right1.png" ], True)
            self.left = Animation(["assets/images/sprite/enemy/enemy2_left.png", "assets/images/sprite/enemy/enemy2_left1.png"], True)
        elif self._type == "tank":
            self.down = Animation(["assets/images/sprite/enemy/enemy3_down.png" ], True)
            self.up =  Animation(["assets/images/sprite/enemy/enemy3_up.png"], True)
            self.right = Animation(["assets/images/sprite/enemy/enemy3_right.png"], True)
            self.left = Animation(["assets/images/sprite/enemy/enemy3_left.png"], True)


        self.current_animation = self.down
    def render(self, canvas, x, y):
        self.current_animation.render(canvas, x, y)
    def update(self, dx, dy, die):
        if dy > 0:
            self.current_animation = self.down
        elif dy < 0:
            self.current_animation = self.up
        elif dx > 0:
            self.current_animation = self.right
        elif dx < 0:
            self.current_animation = self.left

            

            
