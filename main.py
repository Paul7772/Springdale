"""to do"""
# TODO: обязательно сделать анимацию
import random

import Ui_menu as ui
from Settings import *
from Mobs import Zombie, Robber
from player import Player
from tower import Tower
from NPC import NPC

pygame.init()

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
create_robber = pygame.USEREVENT + 2
pygame.time.set_timer(create_robber, 6000)

"""Group"""
all_sprite = pygame.sprite.Group()

players = pygame.sprite.Group()

swords = pygame.sprite.Group()

zombies = pygame.sprite.Group()

arrows = pygame.sprite.Group()

ui_menu = pygame.sprite.Group()

ui_game = pygame.sprite.Group()

towers = pygame.sprite.Group()

sellers = pygame.sprite.Group()

npc_group = pygame.sprite.Group()

robbers = pygame.sprite.Group()

"""Player"""
player = Player(1200, H - 70, swords, all_sprite, arrows, npc_group)
players.add(player)
all_sprite.add(player)

"""first mob"""
zombie = create_object(Zombie, all_sprite, zombies)

"""First robber"""
robber = create_object(Robber, all_sprite, robbers)

"""Menu Settings"""
name_game = ui.text('Springdale', name_font)
start_game_button = ui.Button(660, 440, 'Sprite/Menu/start_button.png', 275, 100)
ui_menu.add(start_game_button)

music_button = ui.Button(65, 65, 'Sprite/Menu/music_button.png', 100, 100)
ui_menu.add(music_button)

quit_button = ui.Button(660, 550, 'Sprite/Menu/quit_button.png', 275, 100)
ui_menu.add(quit_button)

"""Tower"""
tower = Tower(1300, 400)
towers.add(tower)
all_sprite.add(tower)

"""UI Game"""
pause_button = ui.Button(1290, 30, 'Sprite/Game/UI_Game/pause_button.png', 50, 50)
all_sprite.add(pause_button)


def check_click(button):
    pos = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()
    if button.rect.x <= pos[0] <= button.rect.x + button.width:
        if button.rect.y <= pos[1] <= button.rect.y + button.height:
            if keys[0]:
                return True
    else:
        return False


def check_hit(group1, group2):
    hit_list = pygame.sprite.groupcollide(group1, group2, False, True)
    if hit_list:
        for obj1, obj2 in hit_list.items():
            obj1.hp -= obj2[0].damage


def check_theft(robbers1, players1):
    hit_list = pygame.sprite.groupcollide(players, robbers, False, True)
    if hit_list:
        for player1, robber1 in hit_list.items():
            player1.gold -= robber1[0].amount_of_theft


def create_ui_game():
    screen.blit(create_frame(90, 90, FRAME_ICON), (25, 780))
    screen.blit(icon_weapon(player), (30, 785))
    screen.blit(create_frame(200, 40, FRAME_RESOURCE), (11, 11))
    screen.blit(resources_font_create('HP', player.hp, player.max_hp), (48, 15))
    screen.blit(create_frame(200, 40, FRAME_RESOURCE), (215, 11))
    screen.blit(resources_font_create('Gold', player.gold, '+∞'), (265, 15))
    screen.blit(create_frame(300, 50, FRAME_RESOURCE), (515, 11))
    screen.blit(resources_font_create('base HP', tower.hp, 1000), (555, 15))


def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(bg_menu, (0, 0))
        screen.blit(name_game, (390, 200))
        ui_menu.draw(screen)
        pygame.display.flip()
        if check_click(start_game_button):
            break
        if check_click(music_button):
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        if check_click(quit_button):
            exit()
    main()


def all_hit_checks():
    check_hit(players, zombies)
    check_hit(zombies, swords)
    check_hit(zombies, arrows)
    check_hit(npc_group, zombies)
    check_hit(towers, zombies)
    check_theft(robbers, players)


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
                        zombie = create_object(Zombie, all_sprite, zombies)
                else:
                    exit()
        all_hit_checks()
        all_sprite.update()
        screen.fill(GREEN)
        all_sprite.draw(screen)
        create_ui_game()
        clock.tick(FPS)
        pygame.display.flip()


menu()
