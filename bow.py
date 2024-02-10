import pygame

pygame.init()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, path: str, see):
        pygame.sprite.Sprite.__init__(self)
        self.lvl = 1
        self.distance = 0
        self.damage = self.lvl * self.distance * 10
        self.image = pygame.image.load(path).convert_alpha()
        self.direction = 'none'
        if see == 'left':
            self.rect = self.image.get_rect(midleft=(x, y))

        elif see == 'right':
            self.rect = self.rect = self.image.get_rect(midright=(x, y))
        elif see == 'down':
            self.rect = self.image.get_rect(midbottom=(x, y))
        elif see == 'up':
            self.rect = self.rect = self.image.get_rect(midtop=(x, y))

    def update(self):
        pass
