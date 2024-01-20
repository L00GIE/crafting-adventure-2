import pygame, random
from lib.collider import Collider

class Plant:

    def __init__(self, core, tile, item):
        self.core = core
        self.tile = tile
        self.item = item
        self.x = tile.x
        self.y = tile.y
        self.miny = self.y
        self.maxy = self.y - 20
        self.goingup = True
        self.initSprites()
        self.w = self.images[0].get_width()
        self.h = self.images[0].get_height()
        self.stage = 0
        self.timer = 0
        self.maxtimer = 1000
        self.collider = Collider(self)

    def loop(self):
        self.timer += 1
        if self.timer >= self.maxtimer:
            self.timer = 0
            if self.stage < len(self.images) - 1:
                self.stage += 1
        if self.stage >= len(self.images) - 1:
            self.float()
            if self.core.player.collider.colliding(self):
                self.incrementCropCount()
                self.item.count += random.randint(0, 2)
                self.tile.object = None
        self.collider.update()
        pygame.display.get_surface().blit(self.images[self.stage], (self.x, self.y))

    def incrementCropCount(self):
        for crop in self.core.player.inventory["crops"]:
            if crop.index == self.item.index:
                crop.count += 1

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
        ss = pygame.image.load("data/assets/objects&items/plants.png").convert_alpha()
        ss2 = pygame.image.load("data/assets/objects&items/items.png").convert_alpha()
        self.images = []
        if self.item.text == "Pumpkin Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 0, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(0, 0, 16, 16)))
        if self.item.text == "Strawberry Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 16, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(80, 0, 16, 16)))
        if self.item.text == "Carrot Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 32, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(32, 0, 16, 16)))
        if self.item.text == "Potato Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 48, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(64, 0, 16, 16)))
        if self.item.text == "Cabbage Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 64, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(16, 0, 16, 16)))
        if self.item.text == "Wheat Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 80, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(48, 0, 16, 16)))
        if self.item.text == "Tomato Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 96, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(96, 0, 16, 16)))
        if self.item.text == "Eggplant Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 112, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(112, 0, 16, 16)))
        if self.item.text == "Onion Seeds":
            for x in range(4):
                self.images.append(pygame.transform.scale2x(ss.subsurface(16 + (16 * x), 128, 16, 16)))
            self.images.append(pygame.transform.scale2x(ss2.subsurface(128, 0, 16, 16)))
