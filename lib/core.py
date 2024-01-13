import pygame
from data.scenes.farms.farms import Farms
from data.scenes.home.home import Home
from lib.camera import Camera
from lib.cursor import Cursor
from lib.player import Player
from lib.ui import UI

class Core:

    def __init__(self):
        self.cursor = Cursor(self)
        self.player = Player(self)
        self.initScenes()
        self.scene = self.scenes[0]
        self.ui = UI(self)

    def loop(self, events):
        pygame.display.get_surface().fill([165, 197, 67])
        self.events = events
        self.scene.loop()
        self.ui.loop()
        self.cursor.loop()

    def changeScene(self, scene):
        self.scene.remove(self.player)
        self.scene = scene
        self.scene.add(self.player)
        self.scene.positionplayer()

    def initScenes(self):
        self.scenes = [
            Home(self),
            Farms(self)
        ]
