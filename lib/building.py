from lib.collider import Collider
import pygame

class Building:
    def __init__(self, core, image, pos, scene=None):
        self.core = core
        self.image = image
        self.scene = scene
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = pos[0]
        self.y = pos[1]
        self.collider = Collider(self)
        self.doorimg = pygame.image.load("data/assets/objects&items/spring and summer objects.png").subsurface((96, 128, 32, 32))
        self.doorimg = pygame.transform.scale_by(self.doorimg, 3)

    def loop(self):
        self.collider.update()
        if self.core.player.collider.colliding(self):
            if self.scene is not None:
                self.core.changeScene(self.scene)
            else:
                self.core.player.stop(self)
        pygame.display.get_surface().blit(self.image, (self.x, self.y))
        doory = (self.y + self.h) - self.doorimg.get_height()
        doorx = (self.x + (self.w / 3))
        pygame.display.get_surface().blit(self.doorimg, (doorx, doory))
