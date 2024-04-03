import pygame
from player import Player


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group

    def create_object(self):
        player = Player((100, 100), None, None, None, None)
        self.visible_sprites.add(player)

    def run(self):
        # update and draw sprite
        self.create_object()
        self.visible_sprites.draw(self.display_surface)