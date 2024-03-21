
from Settings import *
from Sword import Sword
import bow
from NPC import NPC


pygame.init()


class Player(pygame.sprite.Sprite):
    """class of the player's object """

    def __init__(self, x: int, y: int, sword_group, all_sprite, arrow_group, npc_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Player/Walk_left/walk left1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (38, 74))
        self.rect = self.image.get_rect(center=(x, y))
        self.gold = 1000
        self.speed = 2
        self.see = 'left'
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

    def walk(self, keys):
        if keys[pygame.K_a]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed
                self.see = 'left'
            else:
                self.rect.x = 0
        if keys[pygame.K_d]:
            if self.rect.x <= 1212:
                self.rect.x += self.speed
                self.see = 'right'
            else:
                self.rect.x = 1212
        if keys[pygame.K_s]:
            if self.rect.y <= 826:
                self.rect.y += self.speed
                self.see = 'down'
            else:
                self.rect.y = 826
        if keys[pygame.K_w]:
            if self.rect.y >= 0:
                self.rect.y -= self.speed
                self.see = 'up'
            else:
                self.rect.y = 0

    def regeneration(self):
        if self.hp < self.max_hp:
            if self.can_regeneration:
                self.hp += 1
                self.regeneration_time = pygame.time.get_ticks()
                self.can_regeneration = False

    def create_sword(self):
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
        if self.can_arrow:
            if self.number_of_arrows > 0:
                self.can_arrow = False
                self.arrow_time = pygame.time.get_ticks()
                self.number_of_arrows -= 1
                arrow = bow.Arrow(self.rect.x, self.rect.y + 40, self.rect.x)
                self.arrow_group.add(arrow)
                self.all_sprites.add(arrow)

    def create_npc(self):
        if self.can_npc_create:
            if self.npc_count <= 25:
                if self.gold >= 200:
                    self.gold -= 200
                    self.can_npc_create = False
                    self.npc_create_time = pygame.time.get_ticks()
                    npc = NPC(self.rect.x, self.rect.y, self.all_sprites, self.arrow_group)
                    self.npc_group.add(npc)
                    self.all_sprites.add(npc)
                    self.npc_count += 1

    def switch_weapon(self, keys):
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
            self.speed = 2

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
        if self.hp <= 0:
            exit()
        keys = pygame.key.get_pressed()
        mouse_keys = pygame.mouse.get_pressed()
        self.walk(keys)
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

