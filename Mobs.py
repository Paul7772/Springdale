import pygame
from random import randint

pygame.init()

W = 1324


class Enemy(pygame.sprite.Sprite):
<<<<<<< HEAD
    def __init__(self, x, y, image, weight, height, speed, damage, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'Sprite/Game/Enemy/{image}').convert_alpha()
=======
    def __init__(self, x, y, path, weight, height, speed, damage, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
>>>>>>> fc9b3ec3c353372b3ec2482b1b0f71acc087ed98
        self.image = pygame.transform.scale(self.image, (weight, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.damage = damage
        self.hp = hp
        self.speed = speed

    def update(self):
        if self.rect.x >= W + 25:
            self.kill()
        if self.hp <= 0:
            self.kill()
        self.rect.x += self.speed


class Zombie(Enemy):
    def __init__(self):
<<<<<<< HEAD
        super().__init__(10, randint(20, 850), 'Zombie.png', 48,
                         84, 1, 2, 20)


class Robber(Enemy):
    def __init__(self):
        super().__init__(10, randint(20, 850), 'robber.png', 48,
                         84, 3, 5, 10)
=======
        super().__init__(10, randint(20, 850), 'Sprite/Game/Enemy/Zombie.png', 94,
                         104, 1, 2, 20)


class Robbers(Enemy):
    def __init__(self):
        super().__init__(10, randint(20, 850), 'Sprite/Game/Enemy/robber.png', 94,
                         104, 1, 2, 20)

>>>>>>> fc9b3ec3c353372b3ec2482b1b0f71acc087ed98
