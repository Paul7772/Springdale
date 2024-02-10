import pygame


pygame.init()

"""image"""

image = {
         2: 'Sprite/Game/Tower/Tower.png',
         17: 'Sprite/Menu/Button.png'}


def create_frame_health_bar():
    frame = pygame.image.load('Sprite/Game/UI_Game/frame.png')
    frame = pygame.transform.scale(frame, (310, 40))
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


# def create_sword(player, classes, all_sprite, group):
#    if player.see == 'left':
#        sword = classes(player.rect.midright[0], player.rect.midright[1], image[15], player.see)
#    elif player.see == 'right':
#        sword = classes(player.rect.midleft[0], player.rect.midleft[1], image[15], player.see)
#    elif player.see == 'down':
#        sword = classes(player.rect.midbottom[0], player.rect.midbottom[1], image[15], player.see)
#    elif player.see == 'up':
#        sword = classes(player.rect.midtop[0], player.rect.midtop[1], image[15], player.see)
#    else:
#        sword = classes(player.rect.midright[0], player.rect.midright[1], image[15], player.see)
#    group.add(sword)
#    all_sprite.add(sword)
#    return sword
#

def create_object(classes, all_sprite, group, x: int, y: int):
    objects = classes(x, y)
    group.add(objects)
    all_sprite.add(objects)
    return objects


list_weapon = ['sword', 'bow']
