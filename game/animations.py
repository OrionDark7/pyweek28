#animations.py

import pygame, random

class fire(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([random.randint(60, 120), random.randint(10, 40)])