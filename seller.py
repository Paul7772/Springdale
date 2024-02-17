import pygame

pygame.init()


class Seller(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Player/idle/Idle_left/idle left2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (38, 74))
        self.rect = self.image.get_rect(center=(x, y))

