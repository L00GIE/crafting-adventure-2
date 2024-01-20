from lib.animal import Animal
from lib.building import Building
from lib.clutter import Clutter
from lib.scene import Scene
from lib.tilemanager import TileManager
import pygame

class Farms(Scene):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.initChicken()
        self.initObjects()
        self.tilemanager = TileManager("data/scenes/farms/farms.json", "data/assets/tilemaps/spring farm tilemap.png")

    def loop(self):
        if self.core.player.x < self.core.player.w * -1:
            self.core.changeScene(self.core.scenes[0])
        self.checkbounds()
        self.tilemanager.loop()
        super().loop()

    def checkbounds(self):
        if self.core.player.y <= 0:
            self.core.player.y = 0
        if self.core.player.y >= pygame.display.get_surface().get_height() - self.core.player.h:
            self.core.player.y = pygame.display.get_surface().get_height() - self.core.player.h

    def initChicken(self):
        self.add(Animal(self.core, "data/assets/animals/chicken/brown and white chicken sheet.png", 16))
        self.add(Animal(self.core, "data/assets/animals/cow/black cow sheet.png", 26))
        self.add(Animal(self.core, "data/assets/animals/sheep/fluffy white sheep sheet.png", 26))
    
    def initObjects(self):
        ss = pygame.image.load("data/assets/objects&items/spring and summer objects.png").convert_alpha()
        self.add(Building(self.core, pygame.transform.scale_by(ss.subsurface((0, 112, 96, 96)), 3), (450, 100)), behindplayer=True)
        self.add(Clutter(pygame.transform.scale_by(ss.subsurface((144, 0, 32, 48)), 3), (1250, 350)), behindplayer=True)

        