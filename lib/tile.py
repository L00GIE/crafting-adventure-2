import pygame

class Tile:

    def __init__(self, manager, index):
        self.manager = manager
        self.imageindex = index
        self.updateImage()
        self.x = 0
        self.y = 0

    def loop(self):
        pygame.display.get_surface().blit(self.image, (self.x, self.y))

    def updateImage(self):
        self.image = pygame.transform.scale_by(self.manager.tilepallet[self.imageindex], 3)
