import pygame

class Toolbar:

    def __init__(self, core):
        self.core = core
        self.initSprites()
        self.w = self.emptyimg.get_width() * 10

    def loop(self):
        screen = pygame.display.get_surface()
        for x in range(10):
            xpos = (self.emptyimg.get_width() * x) + ((screen.get_width() / 2) - (self.w / 2))
            ypos = screen.get_height() - self.emptyimg.get_height()
            screen.blit(self.emptyimg, (xpos, ypos))

    def initSprites(self):
        ss = pygame.image.load("data/assets/ui/base.png")
        self.emptyimg = pygame.transform.scale2x(ss.subsurface((0, 144, 48, 48)))