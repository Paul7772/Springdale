import pygame

pygame.init()


class Tower(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Tower/Tower.png').convert_alpha()
        self.rect = self.image.get_rect(center=(1286, 450))
        self.heart = 1000
