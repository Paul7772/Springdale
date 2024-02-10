import pygame

pygame.init()


# the specified color is currently Black
COLOR_TXT = (0, 0, 0)


# class Button(pygame.sprite.Sprite):
#    def __init__(self, x: int, y: int, path: str):
#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.image.load(path).convert_alpha()
#        self.rect = self.image.get_rect(center=(x, y))
#
#
# def update(self):
#     mouse_pos = pygame.mouse.get_pos()
#     if self.rect.bottomleft <= mouse_pos <= self.rect.bottomright:

def text(texts: str, font):
    text_surfase = font.render(texts, False, COLOR_TXT)
    return text_surfase


def create_button(height: int, width: int):
    objects = pygame.image.load('Sprite/Menu/Button.png').convert_alpha()
    objects = pygame.transform.scale(objects, (width, height))
    return objects
