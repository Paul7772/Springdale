
from Settings import *

pygame.init()

W = 1324


class Enemy(pygame.sprite.Sprite):
    def __init__(self, y, image, weight, height, speed, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'Sprite/Game/enemy/{image}').convert_alpha()
        self.image = pygame.transform.scale(self.image, (weight, height))
        self.rect = self.image.get_rect(center=(10, y))
        self.damage = damage
        self.hp = 20
        self.speed = speed
        self.time_update_hp = pygame.time.get_ticks()
        self.update_cooldown = 40000

    def update_hp(self):
        curent_time = pygame.time.get_ticks()
        if curent_time - self.update_cooldown >= self.time_update_hp:
            self.hp *= 2
            self.time_update_hp = pygame.time.get_ticks()

    def update(self):
        self.update_hp()
        if self.rect.x >= W + 25:
            self.kill()
        if self.hp <= 0:
            self.kill()
        self.rect.x += self.speed


class Zombie(Enemy):
    def __init__(self):
        super().__init__(random.randint(20, 850), 'Zombie.png', 48,
                         84, 1, 2)


class Robber(Enemy):
    def __init__(self):
        super().__init__(random.randint(20, 850), 'robber.png', 48,
                         84, 2, 1)
        self.amount_of_theft = 50
