import pygame

pygame.init()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, positions: int, see):
        pygame.sprite.Sprite.__init__(self)
        self.lvl = 1
        self.damage = self.lvl * 10
        self.image = pygame.image.load('Sprite/Game/Arrow/arrow.png').convert_alpha()
        self.speed = 4
        if see == 'left':
            self.rect = self.image.get_rect(midright=(x, y))
            self.direction = 'left'
        elif see == 'right':
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.rect = self.image.get_rect(midleft=(x, y))
            self.direction = 'right'
        elif see == 'down':
            self.rect = self.image.get_rect(midtop=(x, y))
            self.direction = 'down'
        elif see == 'up':
            self.rect = self.rect = self.image.get_rect(midbottom=(x, y))
            self.direction = 'up'
        self.positions_shot = (x, y)
        self.distance = 600

    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'up':
            self.rect.y -= self.speed
        if self.direction == 'down':
            self.rect.y += self.speed
        if (self.rect.x + self.distance <= self.positions_shot[0] or
                self.rect.y + self.distance <= self.positions_shot[1]):
            self.kill()
