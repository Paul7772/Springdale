import pygame
from bow import Arrow
pygame.init()


class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, all_sprite, arrow_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Npc/npc_sprite.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.hp = 2
        self.can_arrow = True
        self.arrow_time = None
        self.arrow_duration_cooldown = 1500
        self.ARROW_GROUP = arrow_group
        self.ALL_SPRITES = all_sprite

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_arrow:
            if current_time - self.arrow_time >= self.arrow_duration_cooldown:
                self.can_arrow = True

    def create_arrow(self):
        if self.can_arrow:
            self.can_arrow = False
            self.arrow_time = pygame.time.get_ticks()
            arrow = Arrow(self.rect.x, self.rect.y + 40)
            self.ARROW_GROUP.add(arrow)
            self.ALL_SPRITES.add(arrow)
            return arrow

    def update(self):
        if self.hp <= 0:
            self.kill()
        self.create_arrow()
        self.cooldown()

