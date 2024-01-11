import pygame

class Cursor:
    def __init__(self):
        pygame.mouse.set_visible(False)
        self.initSprites()
        self.cursor = self.default

    def loop(self):
        pygame.display.get_surface().blit(self.cursor, pygame.mouse.get_pos())

    def initSprites(self):
        ss = pygame.image.load("data/assets/ui/ui elements.png")
        self.default = ss.subsurface((0, 112, 16, 16))