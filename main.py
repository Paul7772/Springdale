"""to do"""
# TODO: Написать класс магазина с оружием и магазина с броней
# TODO: написать класс обменника ресурсов на деньги
# TODO: (по возможности) написать класс нпс которые будут помогать в убийстве зомби
# TODO: обязательно сделать анимацию

import pygame
import random
import Ui_menu as ui
import Settings as set
from Mobs import Zombie
from player import Player
from tower import Tower

pygame.init()

W, H = 1324, 900

WHITE = (255, 255, 255)
GREEN = (0, 189, 0)

FPS = 120
"""Music"""
pygame.mixer.music.load("Sound/Music.ogg")

zombie_wave_count = 0

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

towers = pygame.sprite.Group()

sellers = pygame.sprite.Group()

"""Player"""
player = Player(1250, H - 70, swords, all_sprite, arrows)
players.add(player)
all_sprite.add(player)

"""first mob"""
zombie = set.create_object(Zombie, all_sprite, zombies, 10, random.randint(20, 850))

"""Tower"""
tower = Tower(1286, 450)
all_sprite.add(tower)
towers.add(tower)

"""Menu Settings"""
name_game = ui.text('Springdale', name_font)
start_game_button = ui.Button(660, 440)
ui_g.add(start_game_button)
start_game_text = ui.text('New Game', button_font)
music_button_text = ui.text('Music', button_font)
music_button = ui.Button(660, 550)
ui_g.add(music_button)
exit_button_text = ui.text('Exit', button_font)
exit_button = ui.Button(660, 660)
ui_g.add(exit_button)


def check_click(button):
    pos = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()
    if button.rect.x <= pos[0] <= button.rect.x + button.width:
        if button.rect.y <= pos[1] <= button.rect.y + button.height:
            if keys[0]:
                return True
    else:
        return False


def get_a_weapon(group):
    weapon = None
    for item in group:
        weapon = item
    return weapon


def check_hit(group1, group2, obj1, obj2):
    hit_list = pygame.sprite.groupcollide(group1, group2, False, False)
    if hit_list:
        obj1.heart -= obj2.damage


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
        screen.blit(exit_button_text, (595, 605))
        pygame.display.flip()
        if check_click(start_game_button):
            break
        if check_click(music_button):
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        if check_click(exit_button):
            exit()
    main()


def main():
    global zombie_wave_count, zombie
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == create_zombie:
                if zombie_wave_count < 25:
                    zombie_wave_count += 1
                    for i in range(3):
                        zombie = set.create_object(Zombie, all_sprite, zombies, 10, random.randint(20, 850))
                else:
                    exit()
        check_hit(zombies, players, player, zombie)
        # check_hit(zombies, swords, zombie, get_a_weapon(swords))
        pygame.mouse.set_visible(False)
        all_sprite.update()

        screen.fill(GREEN)
        all_sprite.draw(screen)
        screen.blit(set.create_frame(90, 90), (25, 780))
        screen.blit(set.icon_weapon(player), (30, 785))
        screen.blit(set.create_frame(310, 40), (11, 11))
        screen.blit(set.health_bar(player), (15, 15))
        clock.tick(FPS)
        pygame.display.flip()


menu()
