import pygame

pygame.init()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.lvl = 1
        self.distance = 0
        self.damage = self.lvl * 10
        self.image = pygame.image.load('Sprite/Game/Arrow/arrow.png').convert_alpha()
        self.direction = 'none'
        self.speed = 4
        self.rect = self.image.get_rect(midleft=(x, y))

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x >= 1600:
            self.kill()
