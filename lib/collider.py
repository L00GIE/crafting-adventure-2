import pygame

class Collider:

    def __init__(self, parent, debug=True):
        self.parent = parent
        self.rect = pygame.Rect((self.parent.x, self.parent.y, self.parent.w, self.parent.h))
        self.debug = debug

    def update(self):
        self.rect.x = self.parent.x
        self.rect.y = self.parent.y
        self.rect.w = self.parent.w
        self.rect.h = self.parent.h
        if self.debug:
            colliderrect = pygame.Rect(self.rect.x - 2, self.rect.y - 2, self.rect.w + 4, self.rect.h + 4)
            pygame.draw.rect(pygame.display.get_surface(), [255, 0, 0], colliderrect, width=2) # draw red rectangle around collider

    def colliding(self, obj):
        if hasattr(obj, "collider"):
            if self.rect.colliderect(obj.collider.rect):
                return True
        return False
