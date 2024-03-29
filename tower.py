
import pygame

pygame.init()


class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Tower/Tower.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.max_hp = 100
        self.hp = 100

    def update(self):
        if self.hp <= 0:
            exit()
