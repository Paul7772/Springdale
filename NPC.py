import pygame
from arrow import Arrow

pygame.init()


class NPC(pygame.sprite.Sprite):
    """class npc"""

    def __init__(self, x, y, all_sprite, arrow_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Npc/npc.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.hp = 2
        self.can_arrow = True
        self.arrow_time = None
        self.arrow_duration_cooldown = 1500
        self.arrow_group = arrow_group
        self.all_sprite = all_sprite

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_arrow:
            if current_time - self.arrow_time >= self.arrow_duration_cooldown:
                self.can_arrow = True

    def create_arrow(self):
        """function create arrow"""
        if self.can_arrow:
            self.can_arrow = False
            self.arrow_time = pygame.time.get_ticks()
            arrow = Arrow(self.rect.x, self.rect.y + 40, self.rect.x, 'left')
            self.arrow_group.add(arrow)
            self.all_sprite.add(arrow)
            return arrow

    def update(self):
        if self.hp <= 0:
            self.kill()
        self.create_arrow()
        self.cooldown()
