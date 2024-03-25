from Settings import *

pygame.init()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, images: list, pos: tuple, speed: int, hp: int, damage: int):
        pygame.sprite.Sprite.__init__(self)
        self.image_list: list = images
        self.index = 0
        self.image = pygame.image.load(f'Sprite/Game/enemy/{self.image_list[self.index]}')
        self.image = pygame.transform.scale(self.image, (48, 84))
        self.rect = self.image.get_rect(center=pos)
        self.speed: int = speed
        self.hp: int = hp
        self.damage: int = damage

    def update(self):
        self.rect.x += self.speed
        if self.hp <= 0 or self.rect.x > 1300:
            self.kill()
        self.index += 1
        if self.index >= len(self.image_list):
            self.index = 0
        self.image = pygame.image.load(f'Sprite/Game/enemy/{self.image_list[self.index]}')
        self.image = pygame.transform.scale(self.image, (48, 84))


class Zombie(Enemy):
    def __init__(self, hp, speed):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(['zombie/Zombie_walk1.png', 'zombie/Zombie_walk2.png'], (10, 100),
                         speed, hp, 2)
