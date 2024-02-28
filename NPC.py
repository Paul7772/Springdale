import pygame

pygame.init()


class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('NPC.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.heart = 20

    def create_arrow(self):
        pass

    def update(self):
        pass

