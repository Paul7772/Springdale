import pygame

pygame.init()

W = 1324


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Zombie/Zombie.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (94, 104))
        self.rect = self.image.get_rect(center=(x, y))
        self.lvl = 1
        self.damage = self.lvl * 2
        self.heart = self.lvl * 20
        self.speed = 1
        self.can_attack = True
        self.attack_time = None
        self.attack_duration_cooldown = 2000

    def attack(self, player):
        if self.can_attack:
            self.can_attack = False
            self.attack_time = pygame.time.get_ticks()
            player.heart -= self.damage
            if player.heart <= 0:
                player.kill()

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_duration_cooldown:
                self.can_attack = True

    def update(self):
        self.cooldown()
        if self.rect.x >= W + 25:
            self.kill()
        self.rect.x += self.speed
