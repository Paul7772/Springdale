import pygame


pygame.init()

"""image"""

image = {
         2: 'Sprite/Game/Tower/Tower.png',
         17: 'Sprite/Menu/Button.png'}


def create_frame(width, height):
    frame = pygame.image.load('Sprite/Game/UI_Game/frame.png')
    frame = pygame.transform.scale(frame, (width, height))
    return frame


def health_bar(player):
    max_hp = 300
    count_boxes = 20
    width = max_hp / count_boxes * player.heart
    if player.heart >= 14:
        hp = pygame.image.load('Sprite/Game/Hp_line/hp_Line_Full.png').convert_alpha()
        hp = pygame.transform.scale(hp, (width, 30))
    elif player.heart >= 8:
        hp = pygame.image.load('Sprite/Game/Hp_line/hp_line_Medium.png').convert_alpha()
        hp = pygame.transform.scale(hp, (width, 30))
    elif player.heart < 8:
        hp = pygame.image.load('Sprite/Game/Hp_line/hp_line_low.png').convert_alpha()
        hp = pygame.transform.scale(hp, (width, 30))
    else:
        hp = pygame.image.load('Sprite/Game/Hp_line/hp_Line_Full.png').convert_alpha()
        hp = pygame.transform.scale(hp, (width, 30))
    return hp


def icon_weapon(player):
    if player.weapon == 'sword':
        icon = pygame.image.load('Sprite/Game/icon_weapon/sword.png').convert_alpha()
        icon = pygame.transform.scale(icon, (80, 80))
    else:
        icon = pygame.image.load('Sprite/Game/icon_weapon/bow.png').convert_alpha()
        icon = pygame.transform.scale(icon, (80, 80))
    return icon


def create_object(classes, all_sprite, group, x: int, y: int):
    objects = classes(x, y)
    group.add(objects)
    all_sprite.add(objects)
    return objects


list_weapon = ['sword', 'bow']
