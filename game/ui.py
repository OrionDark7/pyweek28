#ui.py

import pygame

pygame.font.init()

font = pygame.font.Font("./font/8-BIT WONDER.TTF", 32)
color = [0, 0, 0]

def fontSize(size):
    global font
    font = pygame.font.Font("./font/8-BIT WONDER.TTF", int(size))

def text(message, position, window, centered = False):
    global font, color
    render = font.render(str(message), 1, list(color))
    if centered:
        rect = position[0] - render.get_rect().width/2  # centers around x vertical line
        window.blit(render, [rect, position[1]])
    else:
        window.blit(render, position)

class button(pygame.sprite.Sprite):  # takes global font and color
    def __init__(self, text, position, centered=False):
        global font, color
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(text), 1, color)
        self.rect = self.image.get_rect()
        if centered:
            self.rect.left, self.rect.top = position[0] - (self.rect.width/2), position[1]
        else:
            self.rect.left, self.rect.top = position

    def pos(self):  # saves me from writing a couple of characters
        return [self.rect.left, self.rect.top]

    def update(self, window):  # displays button, just named update for sprite group purposes
        window.blit(self.image, self.pos())

    def click(self, mouse):
        clicked = False
        if self.rect.collidepoint(mouse):
            clicked = True

        return clicked