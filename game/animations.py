#animations.py

import pygame, random

class fire(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([random.randint(120, 240), random.randint(40, 100)])
        self.image.fill([random.randint(200, 255), random.randint(0, 165), 0])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = random.randint(800, 1200), random.randint(-100, 600)
        self.speed = random.randint(12, 24)
    def update(self, stop):
        if self.rect.right >= 0:
            self.rect.left -= self.speed
        elif self.rect.right < 0 and not stop:
            self.rect.left = random.randint(800, 900)
            self.image.fill([random.randint(200, 255), random.randint(0, 165), 0])
        elif self.rect.right < 0 and stop:
            self.image.fill([random.randint(200, 255), random.randint(0, 165), 0])
            self.kill()