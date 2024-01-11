from lib.scene import Scene
import pygame

class Test(Scene):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.add(self.core.player)

    def loop(self):
        pygame.display.get_surface().fill([255, 255, 255])
        super().loop()