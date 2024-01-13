from lib.animal import Animal
from lib.building import Building
from lib.clutter import Clutter
from lib.scene import Scene
from lib.tilemanager import TileManager
import pygame

class House(Scene):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.initObjects()
        self.tilemanager = TileManager("data/scenes/house/house.json", "data/assets/tilemaps/spring farm tilemap.png")
        self.add(self.core.player)

    def loop(self):
        if self.core.player.y >= pygame.display.get_surface().get_height():
            self.core.changeScene(self.core.scenes[0])
        self.checkbounds()
        self.tilemanager.loop()
        super().loop()

    def checkbounds(self):
        if self.core.player.x <= 0:
            self.core.player.x = 0
    
    def initObjects(self):
        pass

        