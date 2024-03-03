import pygame


pygame.init()


def create_frame(width, height, path):
    frame = pygame.image.load(path).convert_alpha()
    frame = pygame.transform.scale(frame, (width, height))
    return frame


#def health_bar(object1):
#    max_hp = 300
#    count_boxes = 20
#    width = max_hp / count_boxes * player.heart
#    if player.heart >= 14:
#        hp = pygame.image.load('Sprite/Game/Hp_line/Hp_line_Full.png').convert_alpha()
#        hp = pygame.transform.scale(hp, (width, 30))
#    elif player.heart >= 8:
#        hp = pygame.image.load('Sprite/Game/Hp_line/Hp_line_Medium.png').convert_alpha()
#        hp = pygame.transform.scale(hp, (width, 30))
#    elif player.heart < 8:
#        hp = pygame.image.load('Sprite/Game/Hp_line/Hp_line_low.png').convert_alpha()
#        hp = pygame.transform.scale(hp, (width, 30))
#    else:
#        hp = pygame.image.load('Sprite/Game/Hp_line/Hp_line_Full.png').convert_alpha()
#        hp = pygame.transform.scale(hp, (width, 30))
#    return hp


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
