import pygame

class Camera:

    def __init__(self, core):
        self.core = core
        self.x = 0
        self.lastx = 0
        self.playerlastx = 0
        self.y = 0
        self.lasty = 0
        self.playerlasty = 0
        self.w = pygame.display.get_surface().get_width()
        self.h = pygame.display.get_surface().get_height()
        self.atedge = True
        self.shiftspeed = 4
        self.direction = "e"

    def loop(self):
        self.x -= self.playerlastx - self.core.player.x
        self.y -= self.playerlasty - self.core.player.y
        self.checkBounds()
        self.shiftobjects()
        self.playerlastx = self.core.player.x
        self.playerlasty = self.core.player.y
        self.lastx = self.x
        self.lasty = self.y

    def checkBounds(self):
        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= self.core.scene.tilemanager.get_width() - self.w:
            self.x = self.core.scene.tilemanager.get_width() - self.w
        if self.y >= self.core.scene.tilemanager.get_height() - self.h:
            self.y = self.core.scene.tilemanager.get_height() - self.h
    
    def shiftobjects(self):
        deltax = self.lastx - self.x
        deltay = self.lasty - self.y
        for obj in self.core.scene.objects:
            if obj == self.core.player: continue
            obj.x += deltax
            obj.y += deltay
        for tile in self.core.scene.tilemanager.tiles:
            tile.x += deltax
            tile.y += deltay
            if tile.object is not None:
                tile.object.x += deltax
                tile.object.y += deltay
                if hasattr(tile.object, "miny") and hasattr(tile.object, "maxy"):
                    tile.object.miny += deltay
                    tile.object.maxy += deltay
        for leaf in self.core.scene.leaves.leaves:
            leaf.x += deltax
            leaf.y += deltay
            leaf.startx += deltay
