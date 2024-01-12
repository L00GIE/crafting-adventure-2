import pygame

class Plant:

    def __init__(self, type, pos):
        self.type = type
        self.pos = pos
        self.initSprites()

    def loop(self):
        pygame.display.get_surface().blit(self.image, self.pos)

    def initSprites(self):
        ss = pygame.image.load("data/assets/objects&items/plants.png")
        if self.type == "pumpkin":
            self.image = pygame.transform.scale2x(ss.subsurface(16, 0, 16, 16))
