import pygame

pygame.init()


class Exchanger(pygame.sprite.Sprite):
    def __init__(self, path: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.price = {'skin': 20, 'head': 50, 'weapon': 120}
