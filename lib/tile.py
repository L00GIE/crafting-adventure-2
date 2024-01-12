import pygame
from lib.collider import Collider

class Tile:

    def __init__(self, manager, index):
        self.manager = manager
        self.imageindex = index
        self.updateImage()
        self.borderimage = pygame.transform.scale_by(pygame.image.load("data/assets/ui/ui elements.png").subsurface((4, 4, 24, 24)), 2)
        self.ogborderimage = self.borderimage
        self.x = 0
        self.y = 0
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.breatheval = 0.1
        self.breatheminval = 0.1
        self.breathemaxval = 1.0
        self.offset = 20
        self.growing = True
        self.collider = Collider(self, debug=False)
        self.showborder = False
        self.selected = False
        self.object = None

    def loop(self):
        self.collider.update()
        pygame.display.get_surface().blit(self.image, (self.x, self.y))
        if self.object is not None:
            self.object.loop()
        if self.imageindex == 98:
            if self.showborder or self.selected:
                if not self.selected:
                    pygame.display.get_surface().blit(self.borderimage, (self.x + self.offset, self.y + self.offset))
                    self.borderbreathe()
                else:
                    pygame.display.get_surface().blit(self.ogborderimage, (self.x, self.y))

    def borderbreathe(self):
        self.borderimage = pygame.transform.smoothscale_by(self.ogborderimage, self.breatheval)
        if not self.growing:
            self.breatheval -= 0.02
            self.offset += 20 / 50
            if self.breatheval <= self.breatheminval:
                self.growing = True
        else:
            self.breatheval += 0.02
            self.offset -= 20 / 50
            if self.breatheval >= self.breathemaxval:
                self.growing = False

    def updateImage(self):
        self.image = pygame.transform.scale_by(self.manager.tilepallet[self.imageindex], 3)
