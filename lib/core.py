import pygame
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
        self.camera = Camera(self)
        self.ui = UI(self)

    def loop(self, events):
        pygame.display.get_surface().fill([165, 197, 67])
        self.events = events
        self.scene.loop()
        self.camera.loop()
        self.ui.loop()
        self.cursor.loop()

    def changeScene(self, scene):
        self.scene = scene

    def initScenes(self):
        self.scenes = [
            Home(self)
        ]
