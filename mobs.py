
from Settings import *

pygame.init()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, images: list, pos: tuple, speed: int, hp: int, damage: int, size: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image_list: list = images
        self.index = 0
        self.size = size
        self.image = pygame.image.load(f'Sprite/Game/enemy/{self.image_list[self.index]}')
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=pos)
        self.speed: int = speed
        self.hp: int = hp
        self.damage: int = damage
        self.next_index = 0

    def update(self):
        self.rect.x += self.speed
        if self.hp <= 0 or self.rect.x > 1300:
            self.kill()
        self.next_index += 10
        if self.next_index >= 100:
            self.index += 1
            self.next_index = 0
        if self.index >= len(self.image_list):
            self.index = 0
        self.image = pygame.image.load(f'Sprite/Game/enemy/{self.image_list[self.index]}')
        self.image = pygame.transform.scale(self.image, self.size)


class Zombie(Enemy):
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(['zombie/Zombie_walk1.png', 'zombie/Zombie_walk2.png'], (5, random.randint(10, 880)),
                         1, hp, 2, (48, 84))


class Robber(Enemy):
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(['robber/robber_walk1.png', 'robber/robber_walk2.png'],
                         (5, random.randint(10, 880)), 2, hp, 1, (38, 84))
        self.amount_of_theft = 25
