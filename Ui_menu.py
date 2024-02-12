import pygame

pygame.init()

# the specified color is currently Black
COLOR_TXT = (0, 0, 0)


class Button(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprite/Menu/Button.png').convert_alpha()
        self.width = 480
        self.height = 100
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=(x, y))


def text(texts: str, font):
    text_surfase = font.render(texts, False, COLOR_TXT)
    return text_surfase



