#entities.py

import pygame, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/player/character.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [64, 278]

        self.health = 10
        self.gear = {"weapon" : None, "sheild" : None,
                     "headgear" : None, "chestgear" : None, "leggings" : None, "boots" : None}

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, [self.rect.left, self.rect.top])


class Mob(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/goo/goo.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos

        self.health = random.randint(5, 10)

        self.clicked = False

    def update(self, action, window, mouse):
        if action == "draw":
            window.blit(self.image, [self.rect.left, self.rect.top])
        if action == "click":
            self.clicked = False
            if self.rect.collidepoint(mouse):
                self.clicked = True
