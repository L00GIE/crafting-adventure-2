from lib.animal import Animal
from lib.building import Building
from lib.clutter import Clutter
from lib.scene import Scene
from lib.tilemanager import TileManager
import pygame

class Home(Scene):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.initChicken()
        self.objectsinit = False
        self.tilemanager = TileManager("data/scenes/home/home.json", "data/assets/tilemaps/spring farm tilemap.png")
        self.add(self.core.player)

    def loop(self):
        if not self.objectsinit:
            self.objectsinit = True
            self.initObjects()
        if self.core.player.x >= pygame.display.get_surface().get_width():
            self.core.changeScene(self.core.scenes[1])
        self.checkbounds()
        self.tilemanager.loop()
        super().loop()

    def checkbounds(self):
        if self.core.player.x <= 0:
            self.core.player.x = 0
        if self.core.player.y >= pygame.display.get_surface().get_height() - self.core.player.h:
            self.core.player.y = pygame.display.get_surface().get_height() - self.core.player.h

    def initChicken(self):
        self.add(Animal(self.core, "data/assets/animals/chicken/brown and white chicken sheet.png", 16))
        self.add(Animal(self.core, "data/assets/animals/cow/black cow sheet.png", 26))
        self.add(Animal(self.core, "data/assets/animals/sheep/fluffy white sheep sheet.png", 26))
    
    def initObjects(self):
        ss = pygame.image.load("data/assets/objects&items/spring and summer objects.png").convert_alpha()
        self.add(Building(self.core, pygame.transform.scale_by(ss.subsurface((0, 112, 96, 96)), 3), (1000, 200)), behindplayer=True)
        self.add(Clutter(pygame.transform.scale_by(ss.subsurface((144, 0, 32, 48)), 3), (1250, 350)), behindplayer=True)

        