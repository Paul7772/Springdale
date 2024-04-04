import pygame

pygame.init()


class Sword(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, see, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.list_image = ['Sprite/Game/Sword/Sword_left_right.png', 'Sprite/Game/Sword/Sword_up_down.png']
        self.level = 1
        self.damage = self.level * 10
        if see == 'left':
            self.image = pygame.image.load(self.list_image[0]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect(midright=pos)
        elif see == 'right':
            self.image = pygame.image.load(self.list_image[0]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.rect = self.image.get_rect(midleft=pos)
        elif see == 'down':
            self.image = pygame.image.load(self.list_image[1]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect(midtop=pos)
        elif see == 'up':
            self.image = pygame.image.load(self.list_image[1]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.rect = self.image.get_rect(midbottom=pos)
        self.can_attack = True
        self.attack_time = None

        self.attack_duration_cooldown = 1000

        self.attack_duration_cooldown = 1000

