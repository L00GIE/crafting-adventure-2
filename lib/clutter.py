import pygame

class Clutter:

    def __init__(self, image, pos):
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.w = self.image.get_width()
        self.h = self.image.get_height()

    def loop(self):
        pygame.display.get_surface().blit(self.image, (self.x, self.y))
