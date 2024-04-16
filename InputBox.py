import pygame
import sys

pygame.init()
display = pygame.display.set_mode((400, 300))


class TextInput():
    def __init__(self, x, y, width=100, height=50, color=(10, 25, 8),
                 bgcolor=(0, 255, 0), selectedColor=(0, 0, 255)):
        super().__init__()
        self.text_value = ""
        self.isSelected = False
        self.color = color
        self.bgcolor = bgcolor
        self.selectedColor = selectedColor
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(self.text_value, True, self.color)
        self.bg = pygame.Rect(x, y, width, height)

    def render(self, display):
        self.pos = self.text.get_rect(center=(self.bg.x + self.bg.width / 2,
                                              self.bg.y + self.bg.height / 2))
        if self.isSelected:
            pygame.draw.rect(display, self.selectedColor, self.bg)
        else:
            pygame.draw.rect(display, self.bgcolor, self.bg)
        display.blit(self.text, self.pos)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.bg.collidepoint(event.pos):
                self.isSelected = True
            else:
                self.isSelected = False
        if event.type == pygame.KEYDOWN:
            if self.isSelected:
                if event.key == pygame.K_RETURN:
                    return self.text_value  # Возвращаем введенный текст
                elif event.key == pygame.K_BACKSPACE:
                    self.text_value = self.text_value[:-1]
                else:
                    self.text_value += event.unicode
                self.text = self.font.render(self.text_value, True, self.color)

    def draw(self, screen):
        text_surface = self.font.render(self.text_value, True, self.selectedColor)
        screen.blit(text_surface, (self.x, self.y))


text_input = TextInput(50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        entered_text = text_input.update(event)
        if entered_text:
            print(entered_text)

    display.fill((0,0,0))
    text_input.draw(display)
    pygame.display.flip()
