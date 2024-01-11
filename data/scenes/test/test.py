from lib.animal import Animal
from lib.building import Building
from lib.clutter import Clutter
from lib.scene import Scene
from lib.tilemanager import TileManager
import pygame

class Test(Scene):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.add(self.core.player)
        self.initChicken()
        self.initObjects()
        self.tilemanager = TileManager("data/scenes/test/export.json", "data/assets/tilemaps/spring farm tilemap.png")

    def loop(self):
        self.tilemanager.loop()
        super().loop()

    def initChicken(self):
        self.add(Animal(self.core, "data/assets/animals/chicken/brown and white chicken sheet.png"))
    
    def initObjects(self):
        ss = pygame.image.load("data/assets/objects&items/spring and summer objects.png")
        self.add(Building(self.core, pygame.transform.scale_by(ss.subsurface((0, 112, 96, 96)), 3), (1000, 200)), behindplayer=True)
        self.add(Clutter(pygame.transform.scale_by(ss.subsurface((144, 0, 32, 48)), 3), (1250, 350)), behindplayer=True)

        