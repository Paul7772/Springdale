from Settings import *
from Sword import Sword
import bow
from NPC import NPC


pygame.init()


class Player(pygame.sprite.Sprite):
    """class of the player's object """

    def __init__(self, x: int, y: int, sword_group, all_sprite, arrow_group, npc_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/Player/idle/Idle_left/idle left1.png').convert_alpha()
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
        """create npc"""
        self.can_npc_create = True
        self.npc_create_time = None
        self.npc_create_cooldown = 4000
        self.npc_count = 0

    def walk(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.see = 'left'
        if keys[pygame.K_d]:
            if self.rect.x <= 1286:
                self.rect.x += self.speed
                self.see = 'right'
            else:
                self.rect.x = 1286
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
            self.can_arrow = False
            self.arrow_time = pygame.time.get_ticks()
            arrow = bow.Arrow(self.rect.x, self.rect.y + 40)
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

    def update(self):
        if self.hp <= 0:
            exit()
        keys = pygame.key.get_pressed()
        mouse_keys = pygame.mouse.get_pressed()

        self.walk(keys)
        self.switch_weapon(keys)
        self.can_switch_weapon = self.cooldown(self.weapon_switch_time, self.can_switch_weapon,
                                               self.switch_duration_cooldown)
        self.can_attack = self.cooldown(self.attack_time, self.can_attack, self.attack_duration_cooldown)
        self.can_arrow = self.cooldown(self.arrow_time, self.can_arrow, self.arrow_duration_cooldown)
        self.can_npc_create = self.cooldown(self.npc_create_time, self.can_npc_create, self.npc_create_cooldown)
        self.break_attack()
        if mouse_keys[0]:
            if self.weapon == 'sword':
                self.create_sword()
            else:
                self.create_arrow()
        if keys[pygame.K_r]:
            self.create_npc()