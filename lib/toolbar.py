import pygame

class Toolbar:

    def __init__(self, core):
        self.core = core
        self.initSprites()
        self.w = self.emptyimg.get_width() * 10
        self.selecteditem = 0

    def loop(self):
        for event in self.core.events:
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.selecteditem += 1
                    if self.selecteditem > 9:
                        self.selecteditem = 0
                else:
                    self.selecteditem -= 1
                    if self.selecteditem < 0:
                        self.selecteditem = 9
                
        screen = pygame.display.get_surface()
        index = 0
        for x in range(10):
            xpos = (self.emptyimg.get_width() * x) + ((screen.get_width() / 2) - (self.w / 2))
            ypos = screen.get_height() - self.emptyimg.get_height()
            screen.blit(self.emptyimg, (xpos, ypos))
            if index == self.selecteditem:
                screen.blit(self.border, (xpos, ypos))
            index += 1

    def initSprites(self):
        ss = pygame.image.load("data/assets/ui/base.png")
        self.emptyimg = pygame.transform.scale2x(ss.subsurface((0, 144, 48, 48)))
        self.border = pygame.transform.scale2x(ss.subsurface((48, 384, 48, 48)))