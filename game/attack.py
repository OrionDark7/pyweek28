#attack.py

#This is basically a file for the different attacking activities that happen.

import pygame, random

class hitbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([random.randint(40, 100), 50])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [random.randint(101, 700-self.rect.width), 275]
        self.type = random.randint(0, 1)
        colors = [(255, 10, 0), (249, 255, 127)]
        shaderect = pygame.surface.Surface([4, 50])
        shaderect.fill([0, 0, 0])
        shaderect.set_alpha(100)
        self.image.blit(shaderect, [self.rect.width-4, 0])
        self.image.fill(colors[self.type])
        self.clicked = False
    def update(self, crect, buttons):
        if self.rect.colliderect(crect):
            if self.type == 0 and (buttons[0] or buttons[2]):
                self.clicked = True
            elif self.type == 1 and buttons[0]:
                self.clicked = True

class cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([5, 60])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [100, 270]
        self.image.fill((20, 120, 204))
        self.direction = 1
    def draw(self, window):
        window.blit(self.image, [self.rect.left, self.rect.top])
    def update(self, draw, window):
        if self.rect.left <= 100:
            self.rect.left = 100
            if self.direction == -1:
                self.direction = 1
        elif self.rect.right >= 700:
            self.rect.right = 700
            if self.direction == 1:
                self.direction = -1
        self.rect.left += self.direction * 2
        if draw == "draw":
            self.draw(window)