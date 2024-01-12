import pygame

class Camera:

    def __init__(self, core):
        self.core = core
        self.x = 0
        self.y = 0
        self.w = pygame.display.get_surface().get_width()
        self.h = pygame.display.get_surface().get_height()
        self.atedge = True
        self.shiftspeed = 4
        self.direction = "e"

    def loop(self):
        screen = self.core.scene.tilemanager
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.shiftspeed
            self.direction = "s"
            if self.y < 0:
                self.y = 0
                self.atedge = True
        elif keys[pygame.K_s]:
            self.y += self.shiftspeed
            self.direction = "n"
            if self.y > screen.get_height() - self.h:
                self.y = screen.get_height() - self.h
                self.atedge = True
        elif keys[pygame.K_a]:
            self.x -= self.shiftspeed
            self.direction = "w"
            if self.x < 0:
                self.x = 0
                self.atedge = True
        elif keys[pygame.K_d]:
            self.x += self.shiftspeed
            self.direction = "e"
            if self.x > screen.get_width() - self.w:
                self.x = screen.get_width() - self.w
                self.atedge = True
        if not self.atedge and self.core.player.moving:
            self.shiftobjects()
        self.atedge = False
    
    def shiftobjects(self):
        for obj in self.core.scene.objects:
            if obj == self.core.player: continue
            if self.direction == "e":
                obj.x -= self.shiftspeed
            if self.direction == "w":
                obj.x += self.shiftspeed
            if self.direction == "n":
                obj.y -= self.shiftspeed
            if self.direction == "s":
                obj.y += self.shiftspeed
        for tile in self.core.scene.tilemanager.tiles:
            if self.direction == "e":
                tile.x -= self.shiftspeed
            if self.direction == "w":
                tile.x += self.shiftspeed
            if self.direction == "n":
                tile.y -= self.shiftspeed
            if self.direction == "s":
                tile.y += self.shiftspeed
