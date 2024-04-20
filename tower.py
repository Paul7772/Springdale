import pygame

pygame.init()


class Tower(pygame.sprite.Sprite):
    """class tower"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Tower/Tower.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.max_hp = 50
        self.hp = 50
