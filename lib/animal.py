from lib.animation import Animation

class Animal:

    def __init__(self, sprites):
        self.x = 400
        self.y = 400
        self.h = 16
        self.w = 16
        self.anim = Animation(sprites)

    def loop(self):
        self.anim.play()