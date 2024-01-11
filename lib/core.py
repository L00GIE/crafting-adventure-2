import pygame
from data.scenes.test import Test
from lib.camera import Camera
from lib.player import Player

class Core:

    def __init__(self):
        self.player = Player(self)
        self.scene = Test(self)
        self.camera = Camera(self)

    def loop(self, events):
        self.events = events
        self.scene.loop()
        self.camera.loop()
