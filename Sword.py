import pygame

pygame.init()


class Sword(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, see):
        pygame.sprite.Sprite.__init__(self)
        self.level = 1
        self.damage = self.level * 10
        self.image = pygame.image.load('Sprite/Game/Sword/Sword.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        if see == 'left':
            self.rect = self.image.get_rect(midright=(x, y))
        elif see == 'right':
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.rect = self.image.get_rect(midleft=(x, y))
        elif see == 'down':
            self.image = pygame.transform.flip(self.image, True, True)
            self.rect = self.image.get_rect(midtop=(x, y))
        elif see == 'up':
            self.rect = self.rect = self.image.get_rect(midbottom=(x, y))
        self.can_attack = True
        self.attack_time = None

        self.attack_duration_cooldown = 1000

        self.attack_duration_cooldown = 1000

