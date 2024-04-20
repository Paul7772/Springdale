from Settings import *
from Sword import Sword
from arrow import Arrow
from NPC import NPC

pygame.init()


class Player(pygame.sprite.Sprite):
    """class of the player's object """

    def __init__(self, pos, sword_group, all_sprite, arrow_group, npc_group):
        pygame.sprite.Sprite.__init__(self)
        self.image_dict = {
            'left': ['Walk_left/walk_left1.png', 'Walk_left/walk_left2.png',
                     'Walk_left/walk_left3.png', 'Walk_left/walk_left4.png'],
            'right': ['Walk_right/walk_right1.png', 'Walk_right/walk_right2.png',
                      'Walk_right/walk_right3.png', 'Walk_right/walk_right4.png'],
            'up': ['Walk_up/walk_up1.png', 'Walk_up/walk_up2.png',
                   'Walk_up/walk_up3.png', 'Walk_up/walk_up4.png'],
            'down': ['Walk_down/walk_down1.png', 'Walk_down/walk_down2.png',
                     'Walk_down/walk_down3.png', 'Walk_down/walk_down4.png']
        }
        self.index = 0
        self.see = 'left'
        self.image = pygame.image.load(f'Sprite/Game/Player/{self.image_dict[self.see][self.index]}').convert_alpha()
        self.image = pygame.transform.scale(self.image, (38, 74))
        self.rect = self.image.get_rect(center=pos)
        self.directions = pygame.math.Vector2()
        self.score = 0
        self.gold = 200
        self.speed = 3
        self.hp = 20
        self.max_hp = 20
        self.index_weapon = 0
        self.weapon = list_weapon[self.index_weapon]
        """Switch"""
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 1500
        """attack"""
        self.can_attack = True
        self.attack_time = None
        self.attack_duration_cooldown = 1000
        self.sword_group = sword_group
        self.arrow_group = arrow_group
        self.all_sprites = all_sprite
        self.npc_group = npc_group
        """break attack"""
        self.attack_break_time = 200
        """Create arrow"""
        self.can_arrow = True
        self.arrow_time = None
        self.arrow_duration_cooldown = 600
        self.number_of_arrows = 50
        """create npc"""
        self.can_npc_create = True
        self.npc_create_time = None
        self.npc_create_cooldown = 4000
        self.npc_count = 0
        """regenerations"""
        self.regeneration_time = None
        self.can_regeneration = True
        self.regeneration_cooldown = 1500
        self.next_index = 0

    def index_update(self):
        self.next_index += 10
        if self.next_index >= 100:
            self.index += 1
            self.next_index = 0
        for key in self.image_dict:
            if self.index >= len(self.image_dict[key]):
                self.index = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            """moving to the left"""
            if self.rect.x >= 0:
                self.directions.x = -1
                self.see = 'left'
            else:
                self.directions.x = 0
            self.index_update()

        elif keys[pygame.K_d]:
            """moving to the right"""
            if self.rect.x <= 1212:
                self.directions.x = 1
                self.see = 'right'
            else:
                self.directions.x = 0

            self.index_update()

        else:
            self.directions.x = 0

        if keys[pygame.K_s]:
            """upward movement"""
            if self.rect.y <= 812:
                self.directions.y = 1
                self.see = 'down'
            else:
                self.directions.y = 0

            self.index_update()

        elif keys[pygame.K_w]:
            """downward movement"""
            if self.rect.y >= 0:
                self.directions.y = -1
                self.see = 'up'
            else:
                self.directions.y = 0

            self.index_update()
        else:
            self.directions.y = 0

    def move(self, speed):
        self.rect.center += self.directions * speed

    def regeneration(self):
        if self.hp < self.max_hp:
            if self.can_regeneration:
                self.hp += 1
                self.regeneration_time = pygame.time.get_ticks()
                self.can_regeneration = False

    def create_sword(self):
        """function create sword"""
        direction_map = {
            'left': (self.rect.midleft[0], self.rect.midleft[1]),
            'right': (self.rect.midright[0], self.rect.midright[1]),
            'down': (self.rect.midbottom[0], self.rect.midbottom[1]),
            'up': (self.rect.midtop[0], self.rect.midtop[1])}
        if self.can_attack:
            self.can_attack = False
            self.attack_time = pygame.time.get_ticks()
            sword = Sword(direction_map[self.see][0], direction_map[self.see][1], self.see)
            self.sword_group.add(sword)
            self.all_sprites.add(sword)
            self.speed = 0

    def create_arrow(self):
        """function create arrow"""
        if self.can_arrow:
            if self.number_of_arrows > 0:
                self.can_arrow = False
                self.arrow_time = pygame.time.get_ticks()
                self.number_of_arrows -= 1
                arrow = Arrow(self.rect.x, self.rect.y + 40, self.rect.x, self.see)
                self.arrow_group.add(arrow)
                self.all_sprites.add(arrow)

    def create_npc(self):
        """function create npc"""
        if self.can_npc_create:
            if self.npc_count <= 25:
                if self.gold >= 65:
                    self.gold -= 65
                    self.can_npc_create = False
                    self.npc_create_time = pygame.time.get_ticks()
                    npc = NPC(self.rect.x, self.rect.y, self.all_sprites, self.arrow_group)
                    self.npc_group.add(npc)
                    self.all_sprites.add(npc)
                    self.npc_count += 1

    def switch_weapon(self, keys):
        """weapon change function"""
        if keys[pygame.K_q] and self.can_switch_weapon:
            self.can_switch_weapon = False
            self.weapon_switch_time = pygame.time.get_ticks()
            if self.index_weapon < len(list_weapon) - 1:
                self.index_weapon += 1
            else:
                self.index_weapon = 0
            self.weapon = list_weapon[self.index_weapon]

    def break_attack(self):
        current_time = pygame.time.get_ticks()
        if self.sword_group:
            if current_time - self.attack_time >= self.attack_break_time:
                for sword in self.sword_group:
                    sword.kill()
                    self.speed = 2
        else:
            self.directions.y = 0

    def cooldown(self, time, can, duration_cooldown):
        current_time = pygame.time.get_ticks()
        if not can:
            if current_time - time >= duration_cooldown:
                can = True
        return can

    def all_cooldown(self):
        self.can_switch_weapon = self.cooldown(self.weapon_switch_time, self.can_switch_weapon,
                                               self.switch_duration_cooldown)
        self.can_attack = self.cooldown(self.attack_time, self.can_attack, self.attack_duration_cooldown)
        self.can_arrow = self.cooldown(self.arrow_time, self.can_arrow, self.arrow_duration_cooldown)
        self.can_npc_create = self.cooldown(self.npc_create_time, self.can_npc_create, self.npc_create_cooldown)
        self.can_regeneration = self.cooldown(self.regeneration_time, self.can_regeneration, self.regeneration_cooldown)

    def update(self):
        keys = pygame.key.get_pressed()
        mouse_keys = pygame.mouse.get_pressed()
        self.input()
        self.move(self.speed)
        self.regeneration()
        self.switch_weapon(keys)
        self.all_cooldown()
        self.break_attack()
        if mouse_keys[0]:
            if self.weapon == 'sword':
                self.create_sword()
            else:
                self.create_arrow()
        if keys[pygame.K_r]:
            self.create_npc()
        self.image = pygame.image.load(f'Sprite/Game/Player/{self.image_dict[self.see][self.index]}').convert_alpha()
        self.image = pygame.transform.scale(self.image, (38, 74))
