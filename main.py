"""to do"""
# TODO: Написать класс магазина с оружием и магазина с броней
# TODO: написать класс обменника ресурсов на деньги
# TODO: (по возможности) написать класс нпс которые будут помогать в убийстве зомби
# TODO: обязательно сделать анимацию

import pygame
import random
import Settings as set
import Ui_menu as ui
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

arrows = pygame.sprite.Group()

ui_g = pygame.sprite.Group()
"""Player"""
player = Player(1250, H - 70, swords, all_sprite, arrows)
players.add(player)
all_sprite.add(player)

"""first mob"""
mob = set.create_object(Zombie, all_sprite, zombies, 10, random.randint(20, 850))

"""Text and button"""
name_game = ui.text('Springdale', name_font)
start_game_button = ui.Button(660, 440)
ui_g.add(start_game_button)
start_game_text = ui.text('New Game', button_font)
music_button_text = ui.text('Music', button_font)
music_button = ui.Button(660, 550)
ui_g.add(music_button)


def check_click(button):
    pos = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()
    if button.rect.x <= pos[0] <= button.rect.x + button.width:
        if button.rect.y <= pos[1] <= button.rect.y + button.height:
            if keys[0]:
                return True
    else:
        return False


def check_hit(obj1, obj2, class_obj2):
    hit_list = pygame.sprite.spritecollide(obj1, class_obj2, False)
    if hit_list:
        obj1.attack()


def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(bg_menu, (0, 0))
        screen.blit(name_game, (390, 200))
        ui_g.draw(screen)
        screen.blit(start_game_text, (495, 380))
        screen.blit(music_button_text, (560, 485))

        pygame.display.flip()
        if check_click(start_game_button):
            break
        if check_click(music_button):
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
    main()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == create_zombie:
                for i in range(5):
                    mob = set.create_object(Zombie, all_sprite, zombies, 10, random.randint(20, 850))

        # check_hit(mob, player, players)
        # check_hit(mob, swords[0], swords)
        pygame.mouse.set_visible(False)
        all_sprite.update()
        clock.tick(FPS)
        screen.fill(GREEN)
        all_sprite.draw(screen)
        screen.blit(set.create_frame(90, 90), (25, 780))
        screen.blit(set.icon_weapon(player), (30, 785))
        screen.blit(set.create_frame(310, 40), (11, 11))
        screen.blit(set.health_bar(player), (15, 15))
        pygame.display.flip()


menu()
