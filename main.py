"""to do"""
# TODO: Написать класс магазина с оружием и магазина с броней
# TODO: написать класс обменника ресурсов на деньги
# TODO: (по возможности) написать класс нпс которые будут помогать в убийстве зомби
# TODO: обязательно сделать анимацию



import pygame
import random
from Settings import health_bar, create_frame_health_bar, create_object
from Ui_menu import create_button, text
from Mobs import Zombie
from player import Player


pygame.init()

W, H = 1324, 900

WHITE = (255, 255, 255)
GREEN = (0, 189, 0)

FPS = 120
"""Music"""
pygame.mixer.music.load('Sound/Music.ogg')

"""font"""
pygame.font.init()
name_font = pygame.font.SysFont('Comic Sans MS', 110)
button_font = pygame.font.SysFont('Comic Sans MS', 70)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Springdale')

clock = pygame.time.Clock()

"""Background"""
# bg_surf = pygame.image.load('Sprite/bg.png').convert_alpha()
# bg_surf = pygame.transform.scale(bg_surf, (W, H))

bg_menu = pygame.image.load('Sprite/Menu/bg.png').convert_alpha()
bg_menu = pygame.transform.scale(bg_menu, (W, H))

"""user event"""
create_zombie = pygame.USEREVENT + 1
pygame.time.set_timer(create_zombie, 4500)

"""Group"""
all_sprite = pygame.sprite.Group()

players = pygame.sprite.Group()

swords = pygame.sprite.Group()

zombies = pygame.sprite.Group()

"""Player"""
player = Player(1250, H - 70, swords, all_sprite)
players.add(player)
all_sprite.add(player)

"""first mob"""
mob = create_object(Zombie, all_sprite, zombies, 10, random.randint(20, 850))

"""Text and button"""
name_game = text('Springdale', name_font)
start_game_button = create_button(400, 500)
start_game_text = text('New Game', button_font)


def check_hit(obj1, obj2, class_obj2):
    hit_list = pygame.sprite.spritecollide(obj1, class_obj2, False)
    if hit_list:
        obj1.attack()


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#     screen.blit(bg_menu, (0, 0))
#     screen.blit(name_game, (390, 200))
#     screen.blit(start_game_button, (410, 250))
#     screen.blit(start_game_text, (495, 380))
#     pygame.display.flip()

pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == create_zombie:
            for i in range(5):
                mob = create_object(Zombie, all_sprite, zombies, 10, random.randint(20, 850))

    # check_hit(mob, player, players)
    # check_hit(mob, swords[0], swords)
    pygame.mouse.set_visible(False)
    all_sprite.update()
    clock.tick(FPS)
    screen.fill(GREEN)
    screen.blit(create_frame_health_bar(), (11, 11))
    screen.blit(health_bar(player), (15, 15))
    all_sprite.draw(screen)
    pygame.display.flip()
