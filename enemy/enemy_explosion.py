from game_object import GameObject
from renderers.animation import Animation

class EnemyExplosion(GameObject):
    def __init__(self, x, y, dx, dy, _type):
        GameObject.__init__(self, x, y)
        self._type = _type
        if self._type == "normal":
            self.diedown = Animation(["assets/images/sprite/enemy/enemy1_down.png", "assets/images/sprite/enemy/enemydiedown/die1.png", "assets/images/sprite/enemy/enemydiedown/die2.png"], False)
            self.dieup = Animation(["assets/images/sprite/enemy/enemy1_up.png", "assets/images/sprite/enemy/enemydieup/die1.png", "assets/images/sprite/enemy/enemydieup/die2.png"], False)
            self.dieleft = Animation(["assets/images/sprite/enemy/enemy1_left.png", "assets/images/sprite/enemy/enemydieleft/die1.png", "assets/images/sprite/enemy/enemydieleft/die2.png"], False)
            self.dieright =  Animation(["assets/images/sprite/enemy/enemy1_right.png", "assets/images/sprite/enemy/enemydieright/die1.png", "assets/images/sprite/enemy/enemydieright/die2.png"], False)
        elif self._type == "invisible":
            self.diedown = Animation(["assets/images/sprite/enemy/enemy2_down.png", "assets/images/sprite/enemy/enemydiedown/die11.png", "assets/images/sprite/enemy/enemydiedown/die21.png"], False)
            self.dieup = Animation(["assets/images/sprite/enemy/enemy2_up.png", "assets/images/sprite/enemy/enemydieup/die11.png", "assets/images/sprite/enemy/enemydieup/die21.png"], False)
            self.dieleft = Animation(["assets/images/sprite/enemy/enemy2_left.png", "assets/images/sprite/enemy/enemydieleft/die11.png", "assets/images/sprite/enemy/enemydieleft/die21.png"], False)
            self.dieright =  Animation(["assets/images/sprite/enemy/enemy2_right.png", "assets/images/sprite/enemy/enemydieright/die11.png", "assets/images/sprite/enemy/enemydieright/die21.png"], False)
        elif self._type == "tank":
            self.diedown = Animation(["assets/images/sprite/enemy/enemy3_down.png", "assets/images/sprite/enemy/enemydiedown/die12.png", "assets/images/sprite/enemy/enemydiedown/die22.png"], False)
            self.dieup = Animation(["assets/images/sprite/enemy/enemy3_up.png", "assets/images/sprite/enemy/enemydieup/die12.png", "assets/images/sprite/enemy/enemydieup/die22.png"], False)
            self.dieleft = Animation(["assets/images/sprite/enemy/enemy3_left.png", "assets/images/sprite/enemy/enemydieleft/die12.png", "assets/images/sprite/enemy/enemydieleft/die22.png"], False)
            self.dieright =  Animation(["assets/images/sprite/enemy/enemy3_right.png", "assets/images/sprite/enemy/enemydieright/die12.png", "assets/images/sprite/enemy/enemydieright/die22.png"], False)


        self.dx = dx
        self.dy = dy
        if self.dy > 0:
            self.renderer = self.diedown
        elif self.dy < 0:
            self.renderer = self.dieup
        elif self.dx > 0:
            self.renderer = self.dieright
        elif self.dx < 0:
            self.renderer = self.dieleft