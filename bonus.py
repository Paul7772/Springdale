from Settings import *


class Bonus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Game/bonus/bonus.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.value = random.randrange(11)

    def update_value(self):
        self.value = random.randrange(6)
