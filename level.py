import pygame
from player import Player


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        self.create_objects()

    def create_objects(self):
        self.player = Player((1200, 830), [self.visible_sprites], self.enemy_sprites)

    def create_attack(self):
        pass

    def run(self):
        # update and draw sprite
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
