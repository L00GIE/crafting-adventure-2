import pygame
from lib.animation import Animation
from lib.collider import Collider

class Player:

    def __init__(self, core):
        self.core = core
        self.x = 0
        self.y = 0
        self.w = 64
        self.h = 64
        self.speed = 3
        self.minspeed = 3
        self.maxspeed = 6
        self.direction = "e"
        self.initSprites()
        self.currentAnim = self.idleRightAnim
        self.collider = Collider(self)

    def loop(self):
        self.checkMovement()
        self.collider.update()
        self.currentAnim.play()

    def checkMovement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.speed = self.maxspeed
        else:
            self.speed = self.minspeed
        if keys[pygame.K_w]:
            self.move("n", self.walkLeftAnim)
        if keys[pygame.K_s]:
            self.move("s", self.walkRightAnim)
        if keys[pygame.K_a]:
            self.move("w", self.walkLeftAnim)
        if keys[pygame.K_d]:
            self.move("e", self.walkRightAnim)
        if not keys[pygame.K_w] and not keys[pygame.K_s] and not \
            keys[pygame.K_a] and not keys[pygame.K_d]:
            if self.direction == "s" or self.direction == "e":
                self.currentAnim = self.idleRightAnim
            elif self.direction == "n" or self.direction == "w":
                self.currentAnim = self.idleLeftAnim
            self.moving = False
        
    def move(self, newdir, anim):
        self.direction = newdir
        self.currentAnim = anim
        self.moving = True
        if newdir == "n": self.y -= self.speed
        if newdir == "e": self.x += self.speed
        if newdir == "s": self.y += self.speed
        if newdir == "w": self.x -= self.speed

    def initSprites(self):
        ss = pygame.image.load("data/assets/characters/main character/walk and idle.png")
        self.idleLeftAnim = Animation([ss.subsurface((0, 0, 24, 24)), ss.subsurface((24, 0, 24, 24))], self, delay= 10)
        self.idleRightAnim = Animation([ss.subsurface((48, 0, 24, 24)), ss.subsurface((72, 0, 24, 24))], self, delay= 10)
        walkleftsprites = []
        for x in range(8):
            walkleftsprites.append(ss.subsurface(24 * x, 24, 24, 24))
        self.walkLeftAnim = Animation(walkleftsprites, self)
        walkrightsprites = []
        for x in range(8):
            walkrightsprites.append(ss.subsurface(24 * x, 48, 24, 24))
        self.walkRightAnim = Animation(walkrightsprites, self)
        ss = pygame.image.load("data/assets/characters/main character/farming animations.png")
        self.waterLeftAnim = Animation([ss.subsurface(0, 0, 24, 24), ss.subsurface(24, 0, 24, 24)], self)
        self.waterRightAnim = Animation([ss.subsurface(48, 0, 24, 24), ss.subsurface(72, 0, 24, 24)], self)
        self.axeLeftAnim = Animation([ss.subsurface(0, 24, 24, 24), ss.subsurface(24, 24, 24, 24)], self)
        self.axeRightAnim = Animation([ss.subsurface(48, 24, 24, 24), ss.subsurface(72, 24, 24, 24)], self)
        self.hoeLeftAnim = Animation([ss.subsurface(0, 48, 24, 24), ss.subsurface(24, 48, 24, 24)], self)
        self.hoeRightAnim = Animation([ss.subsurface(48, 48, 24, 24), ss.subsurface(72, 48, 24, 24)], self)
