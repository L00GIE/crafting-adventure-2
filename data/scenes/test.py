from lib.scene import Scene
import pygame

class Test(Scene):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.add(self.core.player)
        self.initChicken()

    def loop(self):
        pygame.display.get_surface().fill([255, 255, 255])
        super().loop()

    def initChicken(self):
        ss = pygame.image.load("data/assets/animals/chicken/brown and white chicken sheet.png")
        sprites = []
        for x in range(5):
            