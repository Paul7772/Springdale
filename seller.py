import pygame

pygame.init()


class Seller(pygame.sprite.Sprite):
    def __init__(self, path, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

