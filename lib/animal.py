from lib.animation import Animation
from lib.collider import Collider
import pygame, random

class Animal:

    def __init__(self, core, spritesheet):
        self.core = core
        self.x = 400
        self.y = 400
        self.h = 32
        self.w = 32
        self.speed = 2
        self.direction = "e"
        self.initAnim(spritesheet)
        self.currentAnim = self.rightAnim
        self.collider = Collider(self)

    def loop(self):
        self.checkCollision()
        self.wander()
        self.collider.update()
        self.currentAnim.play()

    def checkCollision(self):
        if self.core.player.collider.colliding(self):
            self.core.player.stop(self)

    def wander(self):
        if random.randint(0, 100) == 1:
            self.changeDirection()
        if self.direction == "n":
            self.y -= self.speed
            self.currentAnim = self.leftAnim
        if self.direction == "s":
            self.y += self.speed
            self.currentAnim = self.rightAnim
        if self.direction == "e":
            self.x += self.speed
            self.currentAnim = self.rightAnim
        if self.direction == "w":
            self.x -= self.speed
            self.currentAnim = self.leftAnim

    def changeDirection(self):
        self.direction = random.choice(["n", "e", "s", "w"])

    def initAnim(self, spritesheet):
        ss = pygame.image.load(spritesheet)
        sprites = []
        for x in range(5):
            sprites.append(ss.subsurface((16 * x, 0, 16, 16)))
        self.leftAnim = Animation(sprites, self)
        sprites = []
        for x in range(5):
            sprites.append(ss.subsurface((16 * x, 16, 16, 16)))
        self.rightAnim = Animation(sprites, self)