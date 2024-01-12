import pygame

class Plant:

    def __init__(self, type, pos):
        self.type = type
        self.x = pos[0]
        self.y = pos[1]
        self.miny = self.y
        self.maxy = self.y - 20
        self.goingup = True
        self.initSprites()
        self.stage = 0
        self.timer = 0
        self.maxtimer = 1000

    def loop(self):
        self.timer += 1
        if self.timer >= self.maxtimer:
            self.timer = 0
            if self.stage < len(self.images) - 1:
                self.stage += 1
        if self.stage >= len(self.images) - 1:
            self.float()
        pygame.display.get_surface().blit(self.images[self.stage], (self.x, self.y))

    def float(self):
        if self.goingup:
            self.y -= 1
            if self.y <= self.maxy:
                self.goingup = False
        else:
            self.y += 1
            if self.y >= self.miny:
                self.goingup = True

    def initSprites(self):
        ss = pygame.image.load("data/assets/objects&items/plants.png")
        self.images = []
        if self.type == "pumpkin":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 0, 16, 16)))
        if self.type == "strawberry":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 16, 16, 16)))
        if self.type == "carrot":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 32, 16, 16)))
        if self.type == "potato":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 48, 16, 16)))
        if self.type == "cabbage":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 64, 16, 16)))
        if self.type == "wheat":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 80, 16, 16)))
        if self.type == "tomato":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 96, 16, 16)))
        if self.type == "eggplant":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 112, 16, 16)))
        if self.type == "onion":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 128, 16, 16)))
