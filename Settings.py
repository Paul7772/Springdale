
import pygame

W, H = 1324, 900

WHITE = (255, 255, 255)
GREEN = (0, 189, 0)

FPS = 120

FRAME_ICON = 'Sprite/Game/UI_Game/frame1.png'
FRAME_RESOURCE = 'Sprite/Game/UI_Game/frame2.png'

BLACK = (0, 0, 0)
pygame.init()
hp_font = pygame.font.SysFont('Comic Sans MS', 20)


def create_frame(width, height, path):
    frame = pygame.image.load(path).convert_alpha()
    frame = pygame.transform.scale(frame, (width, height))
    return frame


def resources_font_create(name, res, max_res):
    hp = hp_font.render(f'{name}: {res} / {max_res}', True, BLACK)
    return hp


def icon_weapon(player):
    if player.weapon == 'sword':
        icon = pygame.image.load('Sprite/Game/icon_weapon/sword.png').convert_alpha()
        icon = pygame.transform.scale(icon, (80, 80))
    else:
        icon = pygame.image.load('Sprite/Game/icon_weapon/bow.png').convert_alpha()
        icon = pygame.transform.scale(icon, (80, 80))
    return icon


def create_object(classes, all_sprite, group):
    objects = classes()
    group.add(objects)
    all_sprite.add(objects)
    return objects


list_weapon = ['sword', 'bow']




