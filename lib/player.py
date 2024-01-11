import pygame
from lib.animation import Animation
from lib.collider import Collider

class Player:

    def __init__(self, core):
        self.core = core
        self.cowsuit = True
        self.w = 64
        self.h = 64
        self.x = (pygame.display.get_surface().get_width() / 2) - (self.w / 2)
        self.y = (pygame.display.get_surface().get_height() / 2) - (self.h / 2)
        self.speed = 3
        self.minspeed = 3
        self.maxspeed = 6
        self.stopped = False
        self.direction = "e"
        self.initSprites()
        self.initCowSuitSprites()
        self.currentAnim = self.idleRightAnim
        self.cowAnim = self.cowIdleRightAnim
        self.collider = Collider(self)

    def loop(self):
        self.checkInput()
        self.collider.update()
        self.currentAnim.play()
        if self.cowsuit:
            self.updatecowsuit()
            self.cowAnim.play()

    def checkInput(self):
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
            if self.direction == "n" or self.direction == "w":
                self.currentAnim = self.idleLeftAnim
            self.moving = False
        for event in self.core.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.cowsuit = not self.cowsuit
    
    def stop(self):
        self.stopped = True

    def stop(self, obj):
        if self.x > obj.x:
            self.x += self.speed
        if self.x < obj.x:
            self.x -= self.speed
        if self.y > obj.y:
            self.y += self.speed
        if self.y < obj.y:
            self.y -= self.speed
        
    def move(self, newdir, anim):
        if self.stopped and newdir == self.direction:
            return
        self.stopped = False
        self.direction = newdir
        self.currentAnim = anim
        self.moving = True
        if newdir == "n": self.y -= self.speed
        if newdir == "e": self.x += self.speed
        if newdir == "s": self.y += self.speed
        if newdir == "w": self.x -= self.speed

    def updatecowsuit(self):
        if self.direction == "n":
            if self.moving: self.cowAnim = self.cowWalkLeftAnim
            else: self.cowAnim = self.cowIdleLeftAnim
        if self.direction == "s":
            if self.moving: self.cowAnim = self.cowWalkRightAnim
            else: self.cowAnim = self.cowIdleRightAnim
        if self.direction == "w":
            if self.moving: self.cowAnim = self.cowWalkLeftAnim
            else: self.cowAnim = self.cowIdleLeftAnim
        if self.direction == "e":
            if self.moving: self.cowAnim = self.cowWalkRightAnim
            else: self.cowAnim = self.cowIdleRightAnim

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

    def initCowSuitSprites(self):
        ss = pygame.image.load("data/assets/characters/main character/cow kigurumi walk and idle.png")
        self.cowIdleLeftAnim = Animation([ss.subsurface((0, 0, 24, 24)), ss.subsurface((24, 0, 24, 24))], self, delay= 10)
        self.cowIdleRightAnim = Animation([ss.subsurface((48, 0, 24, 24)), ss.subsurface((72, 0, 24, 24))], self, delay= 10)
        walkleftsprites = []
        for x in range(8):
            walkleftsprites.append(ss.subsurface(24 * x, 24, 24, 24))
        self.cowWalkLeftAnim = Animation(walkleftsprites, self)
        walkrightsprites = []
        for x in range(8):
            walkrightsprites.append(ss.subsurface(24 * x, 48, 24, 24))
        self.cowWalkRightAnim = Animation(walkrightsprites, self)
        ss = pygame.image.load("data/assets/characters/main character/cow kigurumi farming animations.png")
        self.cowWaterLeftAnim = Animation([ss.subsurface(0, 0, 24, 24), ss.subsurface(24, 0, 24, 24)], self)
        self.cowWaterRightAnim = Animation([ss.subsurface(48, 0, 24, 24), ss.subsurface(72, 0, 24, 24)], self)
        self.cowAxeLeftAnim = Animation([ss.subsurface(0, 24, 24, 24), ss.subsurface(24, 24, 24, 24)], self)
        self.cowAxeRightAnim = Animation([ss.subsurface(48, 24, 24, 24), ss.subsurface(72, 24, 24, 24)], self)
        self.cowHoeLeftAnim = Animation([ss.subsurface(0, 48, 24, 24), ss.subsurface(24, 48, 24, 24)], self)
        self.cowHoeRightAnim = Animation([ss.subsurface(48, 48, 24, 24), ss.subsurface(72, 48, 24, 24)], self)
