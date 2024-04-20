import pygame

pygame.init()


class Arrow(pygame.sprite.Sprite):
    """Class arrow"""

    def __init__(self, x: int, y: int, positions: int, see):
        pygame.sprite.Sprite.__init__(self)
        self.lvl = 1
        self.damage = self.lvl * 10
        self.image_list = [pygame.image.load('Sprite/Game/Arrow/arrow_left_right.png').convert_alpha(),
                           pygame.image.load('Sprite/Game/Arrow/arrow_up_down.png').convert_alpha()]
        self.speed = 4
        if see == 'left':
            self.image = self.image_list[0]
            self.rect = self.image.get_rect(midright=(x, y))
            self.direction = 'left'
        elif see == 'right':
            self.image = self.image_list[0]
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.rect = self.image.get_rect(midleft=(x, y))
            self.direction = 'right'
        elif see == 'down':
            self.image = self.image_list[1]
            self.rect = self.image.get_rect(midtop=(x, y))
            self.direction = 'down'
        elif see == 'up':
            self.image = self.image_list[1]
            self.rect = self.rect = self.image.get_rect(midbottom=(x, y))
            self.direction = 'up'
        self.positions_shot = (x, y)
        self.distance = 600

    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        if (self.rect.x + self.distance <= self.positions_shot[0] or
                self.rect.y + self.distance <= self.positions_shot[1]):
            self.kill()
