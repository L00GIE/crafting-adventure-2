class Camera:

    def __init__(self, core):
        self.core = core
        self.x = 0
        self.y = 0
        self.lastplayerpos = None

    def loop(self):
        newplayerpos = (self.core.player.x, self.core.player.y)
        if self.lastplayerpos is not None:
            if self.core.player.moving:
                if newplayerpos[0] > self.lastplayerpos[0]:
                    self.x += self.core.player.speed
                elif newplayerpos[0] < self.lastplayerpos[0]:
                    self.x -= self.core.player.speed
                if newplayerpos[1] > self.lastplayerpos[1]:
                    self.y += self.core.player.speed
                elif newplayerpos[1] < self.lastplayerpos[1]:
                    self.y -= self.core.player.speed
                self.shiftobjects(newplayerpos)
        self.lastplayerpos = newplayerpos
    
    def shiftobjects(self, newplayerpos):
        for obj in self.core.scene.objects:
            if newplayerpos[0] > self.lastplayerpos[0]:
                obj.x -= self.core.player.speed
            elif newplayerpos[0] < self.lastplayerpos[0]:
                obj.x += self.core.player.speed
            if newplayerpos[1] > self.lastplayerpos[1]:
                obj.y -= self.core.player.speed
            elif newplayerpos[1] < self.lastplayerpos[1]:
                obj.y += self.core.player.speed
