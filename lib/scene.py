from lib.leaves import Leaves

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
