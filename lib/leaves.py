import pygame, random

class Leaves:

    def __init__(self):
        ss = pygame.image.load("data/assets/objects&items/items.png")
        self.images = [ss.subsurface((64, 32, 16, 16)), ss.subsurface((80, 32, 16, 16))]
        self.leaves = []

    def loop(self):
        for leaf in self.leaves:
            leaf.loop()
            if leaf.y >= pygame.display.get_surface().get_height():
                self.leaves.remove(leaf)
        if len(self.leaves) < 20 and random.randint(1, 40) == 1:
            randx = random.randint(0, pygame.display.get_surface().get_width())
            self.leaves.append(Leaf(random.choice(self.images), (randx, 0)))


class Leaf:

    def __init__(self, img, pos):
        self.img = img
        self.x = pos[0]
        self.startx = self.x
        self.y = pos[1]
        self.speed = 1
        self.goingleft = False

    def loop(self):
        self.y += self.speed
        if self.goingleft:
            self.x -= self.speed
            if self.x <= self.startx - 50:
                self.goingleft = False
        else:
            self.x += self.speed
            if self.x >= self.startx + 50:
                self.goingleft = True
        if self.y < pygame.display.get_surface().get_height():
            pygame.display.get_surface().blit(self.img, (self.x, self.y))
