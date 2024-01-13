from lib.leaves import Leaves
import pygame

class Scene:

    def __init__(self):
        self.objects = []
        self.leaves = Leaves()

    def loop(self):
        for obj in self.objects:
            if hasattr(obj, "loop"):
                obj.loop()
        self.leaves.loop()

    def add(self, obj, behindplayer=False):
        if behindplayer and self.core.player in self.objects:
            playerindex = self.objects.index(self.core.player)
            self.objects.insert(playerindex, obj)
        else:
            self.objects.append(obj)

    def remove(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def positionplayer(self):
        if self.core.player.direction == "e":
            self.core.player.x = 0
            self.resetCamera(0, 0)
        elif self.core.player.direction == "w":
            self.core.player.x = self.core.scene.tilemanager.get_width() - self.core.player.w
            self.core.camera.x = pygame.display.get_surface().get_width() - self.core.camera.w
        if self.core.player.direction == "n":
            self.core.player.y = self.core.scene.tilemanager.get_height() - self.core.player.h
        elif self.core.player.direction == "s":
            self.core.player.y = 0

    def resetCamera(self, x, y):
        self.core.camera.x = x
        self.core.camera.lastx = x
        self.core.camera.playerlastx = x
        self.core.camera.y = y
        self.core.camera.lasty = y
        self.core.camera.playerlasty = y
