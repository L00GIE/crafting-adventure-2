from lib.animation import Animation
from lib.collider import Collider
import pygame, random

class Animal:

    def __init__(self, core, spritesheet, size):
        self.core = core
        self.size = size
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
        # self.checkBounds()
        self.collider.update()
        self.currentAnim.play()

    def checkBounds(self):
        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= self.core.scene.tilemanager.get_width() - self.w:
            self.x = self.core.scene.tilemanager.get_width() - self.w
        if self.y > self.core.scene.tilemanager.get_height() - self.h:
            self.y = self.y > self.core.scene.tilemanager.get_height() - self.h

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
            sprites.append(ss.subsurface((self.size * x, 0, self.size, self.size)))
        self.leftAnim = Animation(sprites, self)
        sprites = []
        for x in range(5):
            sprites.append(ss.subsurface((self.size * x, self.size, self.size, self.size)))
        self.rightAnim = Animation(sprites, self)