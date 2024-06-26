import sys
import pygame
import Ui_menu as ui
from Settings import *
from bonus import Bonus
from database import sqlupdate, printsql, printsql_by_name
from mobs import Zombie, Robber
from player import Player
from tower import Tower
from InputBox import InputBox

pygame.init()

"""Music"""
pygame.mixer.music.load("Sound/Music.ogg")

"""font"""
pygame.font.init()
name_font = pygame.font.SysFont('Comic Sans MS', 90)
button_font = pygame.font.SysFont('Comic Sans MS', 70)
leaderboard_font = pygame.font.SysFont('Comic Sans MS', 25)
name_leaderboard_font = pygame.font.SysFont('Comic Sans MS', 50)

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

score_update = pygame.USEREVENT + 5
pygame.time.set_timer(score_update, 1_000)

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

pause_ui = pygame.sprite.Group()

"""Player"""
player = Player((1200, H - 70), swords, all_sprite, arrows, npc_group)
players.add(player)
all_sprite.add(player)

"""mob settings"""
mob_hp = {'zombie': 10,
          'robber': 5}
mob_speed = {'zombie': 1,
             'robber': 2}

"""first zombie"""
zombie = create_enemy(Zombie, all_sprite, zombies, mob_hp['zombie'], mob_speed['zombie'])

"""First robber"""
robber = create_enemy(Robber, all_sprite, robbers, mob_hp['robber'], mob_speed['robber'])

"""Menu Settings"""
name_game = ui.text('Springdale', name_font)
start_game_button = ui.Button(660, 550, 'Sprite/Menu/start_button.png', 275, 100)
ui_menu_settings.add(start_game_button)

music_button = ui.Button(65, 65, 'Sprite/Menu/music_button.png', 100, 100)
ui_menu_settings.add(music_button)

quit_button = ui.Button(660, 660, 'Sprite/Menu/quit_button.png', 275, 100)
ui_menu_settings.add(quit_button)

"""Pause settings"""
text_leaderboard = ui.text('Leaderboard', name_leaderboard_font)
quit_button_for_pause = ui.Button(660, 750, 'Sprite/Menu/quit_button.png', 275, 100)
pause_ui.add(quit_button_for_pause)

"""Tower"""
tower = Tower(1_300, 400)
towers.add(tower)
all_sprite.add(tower)

"""Bonus"""
bonus = Bonus(-1_000, -1_000)
all_sprite.add(bonus)
bonuses.add(bonus)


def check_click(button):
    """Checking the click on the button in the menu"""
    pos = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()
    if button.rect.collidepoint(pos):
        if keys[0]:
            return True
    else:
        return False


def check_collision_with_bonus(players1, bonuses1):
    """ Checking the bonus selection """
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


def check_hit_tower(enemy, towers1):
    """Tower check"""
    global tower
    hit_list = pygame.sprite.spritecollide(enemy, towers1, False)
    if hit_list:
        tower.hp -= enemy.damage
        enemy.kill()


def create_ui_game():
    """Rendering the game interface"""
    screen.blit(create_frame(90, 90, FRAME['weapon']), (25, 780))
    screen.blit(icon_weapon(player), (30, 785))
    screen.blit(create_frame(200, 40, FRAME['hp']), (11, 11))
    screen.blit(resources_font_create('HP', player.hp, player.max_hp), (48, 15))
    screen.blit(create_frame(200, 40, FRAME['gold_and_score']), (215, 11))
    screen.blit(resources_font_create('Gold', player.gold, '+∞'), (265, 15))
    screen.blit(create_frame(300, 50, FRAME['hp']), (630, 11))
    screen.blit(resources_font_create('base HP', tower.hp, tower.max_hp), (695, 15))
    screen.blit(create_frame(200, 40, FRAME['hp']), (420, 11))
    screen.blit(resources_font_create('arrows', player.number_of_arrows, '+∞'), (450, 15))
    screen.blit(create_frame(200, 40, FRAME['gold_and_score']), (950, 11))
    screen.blit(resources_font_create('score', player.score, '+∞'), (990, 15))


def all_hit_checks():
    """All collision checks"""
    check_hit_player(players, zombies)
    check_theft(players, robbers)
    check_hit_enemy(zombies, swords)
    check_hit_enemy(zombies, arrows)
    check_hit_enemy(robbers, swords)
    check_hit_enemy(robbers, arrows)
    check_hit_enemy(npc_group, zombies)
    for z in zombies:
        check_hit_tower(z, towers)
    for r in robbers:
        check_hit_tower(r, towers)
    check_collision_with_bonus(players, bonuses)


def create_leaderboard_text():
    """A function for outputting text from a database"""
    y = 200
    num = 1
    for column in printsql():
        text = ui.text(f'{num}. name: {column[0]} - score {column[1]}', leaderboard_font)
        screen.blit(text, (500, y))
        num += 1
        y += 25
    return y


def pause(name):
    """ Pause cycle function """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        sqlupdate(name, player.score)
        screen.blit(bg_menu, (0, 0))
        screen.blit(text_leaderboard, (500, 80))
        y = create_leaderboard_text()
        you_in_leaderboard = ui.text(f'you. name: {printsql_by_name(name)[0]} - score {printsql_by_name(name)[1]}',
                                     leaderboard_font)
        screen.blit(you_in_leaderboard, (500, y))
        pause_ui.draw(screen)
        pygame.display.flip()
        if check_click(quit_button_for_pause):
            exit()


input_box = InputBox(560, 420, 50, 40, '')


def menu():
    """ Menu cycle function """
    name = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if name == None:
                name = input_box.handle_event(event)
            else:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if input_box.rect.collidepoint(mouse_pos):
                        name = input_box.handle_event(event)

        screen.blit(bg_menu, (0, 0))
        screen.blit(name_game, (430, 200))
        ui_menu_settings.draw(screen)
        input_box.update()
        input_box.draw(screen)
        pygame.display.flip()
        if check_click(start_game_button):
            if name != None:
                break
        if check_click(music_button):
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        if check_click(quit_button):
            exit()
    return True, name


def main():
    """The main cycle of the game"""
    global zombie, robber, player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == create_zombie:
                for i in range(6):
                    zombie = create_enemy(Zombie, all_sprite, zombies, mob_hp['zombie'], mob_speed['zombie'])
            if event.type == create_robber:
                robber = create_enemy(Robber, all_sprite, robbers, mob_hp['robber'], mob_speed['robber'])
            if event.type == create_bonus:
                bonus.rect.x, bonus.rect.y = random.randrange(1212), random.randrange(850)
            if event.type == score_update:
                player.score += 1
            if event.type == update_settings_enemy:
                for key in mob_hp:
                    mob_hp[key] += 10
                for key in mob_speed:
                    mob_speed[key] += 1
        all_hit_checks()
        all_sprite.update()
        screen.fill(GREEN)
        all_sprite.draw(screen)
        create_ui_game()
        clock.tick(FPS)
        pygame.display.flip()
        if player.hp <= 0 or tower.hp <= 0:
            break
    return True


if __name__ == '__main__':
    finish_game = True
    start_game, name = menu()
    if start_game:
        finish_game = main()
    if finish_game:
        pause(name)
