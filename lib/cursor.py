import pygame
from lib.collider import Collider

class Cursor:
    def __init__(self, core):
        self.core = core
        pygame.mouse.set_visible(False)
        self.initSprites()
        self.cursor = self.default
        self.w = self.cursor.get_width()
        self.h = self.cursor.get_height()
        self.x = 0
        self.y = 0
        self.collider = Collider(self, debug=False)

    def loop(self):
        mousepos = pygame.mouse.get_pos()
        self.x = mousepos[0]
        self.y = mousepos[1]
        self.collider.update()
        self.checkCollision()
        pygame.display.get_surface().blit(self.cursor, (self.x, self.y))

    def checkCollision(self):
        for tile in self.core.scene.tilemanager.tiles:
            if self.collider.colliding(tile):
                tile.showborder = True
                for event in self.core.events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 and tile.imageindex == 98:
                            tile.selected = not tile.selected
            else:
                tile.showborder = False

    def initSprites(self):
        ss = pygame.image.load("data/assets/ui/ui elements.png")
        self.default = ss.subsurface((0, 112, 16, 16))