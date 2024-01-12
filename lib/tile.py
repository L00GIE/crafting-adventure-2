import pygame
from lib.collider import Collider

class Tile:

    def __init__(self, manager, index):
        self.manager = manager
        self.imageindex = index
        self.updateImage()
        self.borderimage = pygame.transform.scale_by(pygame.image.load("data/assets/ui/ui elements.png").subsurface((0, 0, 32, 32)), 2)
        self.x = 0
        self.y = 0
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.breatheval = 1.0
        self.breatheminval = 0.2
        self.breathemaxval = 1.0
        self.growing = False
        self.collider = Collider(self, debug=True)
        self.showborder = False

    def loop(self):
        self.collider.update()
        pygame.display.get_surface().blit(self.image, (self.x, self.y))
        if self.showborder:
            pygame.display.get_surface().blit(self.borderimage, (self.x - 10, self.y - 10))
            self.borderbreathe()

    def borderbreathe(self):
        self.borderimage = pygame.transform.scale_by(self.borderimage, self.breatheval)
        if not self.growing:
            self.breatheval -= 0.1
            if self.breatheval <= self.breatheminval:
                self.growing = True
        else:
            self.breatheval += 0.1
            if self.breatheval >= self.breathemaxval:
                self.growing = False
        print(self.breatheval)

    def updateImage(self):
        self.image = pygame.transform.scale_by(self.manager.tilepallet[self.imageindex], 3)
