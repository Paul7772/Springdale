# TODO: обязательно сделать анимацию
import pygame

import Ui_menu as ui
from Settings import *
from mobs import Zombie, Robber
from player import Player
from tower import Tower
from bonus import Bonus


pygame.init()

"""Music"""
pygame.mixer.music.load("Sound/Music.ogg")

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
pygame.time.set_timer(create_zombie, 10_000)

create_robber = pygame.USEREVENT + 2
pygame.time.set_timer(create_robber, 12_000)

create_bonus = pygame.USEREVENT + 3
pygame.time.set_timer(create_bonus, 15_000)

update_settings_enemy = pygame.USEREVENT + 4
pygame.time.set_timer(update_settings_enemy, 40_000)

"""Group"""
all_sprite = pygame.sprite.Group()

players = pygame.sprite.Group()

swords = pygame.sprite.Group()

zombies = pygame.sprite.Group()

arrows = pygame.sprite.Group()

ui_menu_settings = pygame.sprite.Group()

towers = pygame.sprite.Group()

sellers = pygame.sprite.Group()

npc_group = pygame.sprite.Group()

robbers = pygame.sprite.Group()

bonuses = pygame.sprite.Group()

"""Player"""
player = Player((1200, H - 70), swords, all_sprite, arrows, npc_group)
players.add(player)
all_sprite.add(player)

"""mob settings"""
mob_settings = {'hp_zombie': 10,
                'hp_robber': 5}
"""first zombie"""
zombie = create_object(Zombie, all_sprite, zombies, mob_settings['hp_zombie'])

"""First robber"""
robber = create_object(Robber, all_sprite, robbers, mob_settings['hp_robber'])

"""Menu Settings"""
name_game = ui.text('Springdale', name_font)
start_game_button = ui.Button(660, 440, 'Sprite/Menu/start_button.png', 275, 100)
ui_menu_settings.add(start_game_button)

music_button = ui.Button(65, 65, 'Sprite/Menu/music_button.png', 100, 100)
ui_menu_settings.add(music_button)

quit_button = ui.Button(660, 550, 'Sprite/Menu/quit_button.png', 275, 100)
ui_menu_settings.add(quit_button)

"""Tower"""
tower = Tower(1300, 400)
towers.add(tower)
all_sprite.add(tower)

"""Bonus"""
bonus = Bonus(-1_000, -1_000)
all_sprite.add(bonus)
bonuses.add(bonus)


def check_click(button):
    pos = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()
    if button.rect.x <= pos[0] <= button.rect.x + button.width:
        if button.rect.y <= pos[1] <= button.rect.y + button.height:
            if keys[0]:
                return True
    else:
        return False


def check_collision_with_bonus(players1, bonuses1):
    hit_list = pygame.sprite.groupcollide(players1, bonuses1, False, False)
    if hit_list:
        for obj1, obj2 in hit_list.items():
            obj1.number_of_arrows += obj2[0].value
            obj2[0].update_value()
            obj2[0].rect.x, obj2[0].rect.y = -1_000, -1_000


def check_hit_enemy(enemy_group, weapon_group):
    """check enemy"""
    global player
    hit_list = pygame.sprite.groupcollide(enemy_group, weapon_group, False, False)
    if hit_list:
        for enemy, weapon in hit_list.items():
            enemy.hp -= weapon[0].damage
            player.gold += 1


def check_theft(players1, robbers1):
    """check robber"""
    hit_list = pygame.sprite.groupcollide(players1, robbers1, False, True)
    if hit_list:
        for obj1, obj2 in hit_list.items():
            obj1.gold -= obj2[0].amount_of_theft


def check_hit_player(players1, zombies1):
    """check player"""
    hit_list = pygame.sprite.groupcollide(players1, zombies1, False, True)
    if hit_list:
        for player1, zombie2 in hit_list.items():
            player1.hp -= zombie2[0].damage
            player1.regeneration_time = pygame.time.get_ticks()
            player1.can_regeneration = False


def check_hit_tower(enemy_group, towers1):
    """Tower check"""
    hit_list = pygame.sprite.groupcollide(towers1, enemy_group, False, True)
    if hit_list:
        for tower1, enemy2 in hit_list.items():
            tower1.hp -= enemy2[0].damage


def create_ui_game():
    screen.blit(create_frame(90, 90, FRAME_ICON), (25, 780))
    screen.blit(icon_weapon(player), (30, 785))
    screen.blit(create_frame(200, 40, FRAME_RESOURCE), (11, 11))
    screen.blit(resources_font_create('HP', player.hp, player.max_hp), (48, 15))
    screen.blit(create_frame(200, 40, FRAME_RESOURCE), (215, 11))
    screen.blit(resources_font_create('Gold', player.gold, '+∞'), (265, 15))
    screen.blit(create_frame(300, 50, FRAME_RESOURCE), (630, 11))
    screen.blit(resources_font_create('base HP', tower.hp, tower.max_hp), (695, 15))
    screen.blit(create_frame(200, 40, FRAME_RESOURCE), (420, 11))
    screen.blit(resources_font_create('arrows', player.number_of_arrows, '+∞'), (450, 15))


def all_hit_checks():
    """check hit player"""
    check_hit_player(players, zombies)
    check_theft(players, robbers)
    """check hit enemy"""
    check_hit_enemy(zombies, swords)
    check_hit_enemy(zombies, arrows)
    check_hit_enemy(robbers, swords)
    check_hit_enemy(robbers, arrows)
    check_hit_enemy(npc_group, zombies)
    """check hit tower"""
    check_hit_tower(zombies, towers)
    check_hit_tower(robbers, towers)
    """check bonus"""
    check_collision_with_bonus(players, bonuses)


def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(bg_menu, (0, 0))
        screen.blit(name_game, (390, 200))
        ui_menu_settings.draw(screen)
        pygame.display.flip()
        if check_click(start_game_button):
            break
        if check_click(music_button):
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        if check_click(quit_button):
            exit()
    main()


def main():
    global zombie, robber
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == create_zombie:
                for i in range(3):
                    zombie = create_object(Zombie, all_sprite, zombies, mob_settings['hp_zombie'])
            if event.type == create_robber:
                robber = create_object(Robber, all_sprite, robbers, mob_settings['hp_robber'])
            if event.type == create_bonus:
                bonus.rect.x, bonus.rect.y = random.randrange(1212), random.randrange(850)
            if event.type == update_settings_enemy:
                for key in mob_settings:
                    mob_settings[key] += 5
        all_hit_checks()
        all_sprite.update()
        screen.fill(GREEN)
        all_sprite.draw(screen)
        create_ui_game()
        clock.tick(FPS)
        pygame.display.flip()


menu()

