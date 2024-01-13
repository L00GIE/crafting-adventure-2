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
            self.core.player.lastx = 0
        if self.core.player.direction == "w":
            self.core.player.x = pygame.display.get_surface().get_width() - self.core.player.w
            self.core.player.lastx = pygame.display.get_surface().get_width() - self.core.player.w
