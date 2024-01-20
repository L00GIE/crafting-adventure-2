import pygame, random

class Clouds:

    def __init__(self):
        self.initImages()
        self.clouds = []

    def loop(self):
        if random.randint(1, 2000) == 1:
            self.clouds.append(Cloud(self, random.choice(self.images)))
        for cloud in self.clouds:
            cloud.loop()

    def initImages(self):
        self.images = [
            pygame.image.load("data/assets/objects&items/cloud1.png").convert_alpha(),
            pygame.image.load("data/assets/objects&items/cloud2.png").convert_alpha(),
            pygame.image.load("data/assets/objects&items/cloud3.png").convert_alpha(),
            pygame.image.load("data/assets/objects&items/cloud4.png").convert_alpha()
        ]


class Cloud:

    def __init__(self, clouds, image):
        self.clouds = clouds
        self.image = image
        self.x = pygame.display.get_surface().get_width()
        self.y = random.randint(0, pygame.display.get_surface().get_height() - self.image.get_height())
    
    def loop(self):
        self.x -= 1
        if self.x <= 0 - self.image.get_width():
            if self in self.clouds.clouds:
                self.clouds.clouds.remove(self)
        pygame.display.get_surface().blit(self.image, (self.x, self.y))