#attack.py

#This is basically a file for the different attacking activities that happen.

import pygame, random

class fallingobj(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.randint(0, 1)
        size = random.randint(10, 30)
        self.image = pygame.surface.Surface([size, size])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = random.randint(0, 800-size), 0-size
        self.clicked = False
        self.speed = random.choice([0.25, 0.5, 1])
        if self.type == 0:
            self.image.fill([249, 255, 127])
        else:
            self.image.fill((255, 10, 0))
    def update(self, action, window, mouse):
        self.clicked = False

        if action == "fall":
            self.rect.top += self.speed

        if action == "draw":
            window.blit(self.image, [self.rect.left, self.rect.top])

        if action == "click" and self.rect.collidepoint(mouse):
            self.clicked = True