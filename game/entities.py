#entities.py

import pygame, random

moblist = ["goo", "ghost", "deathorb", "darkghost"]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/player/character.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [128, 278]

        self.health = 10

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, [self.rect.left, self.rect.top])


class Mob(pygame.sprite.Sprite):
    def __init__(self, pos, level):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(moblist[0:len(moblist)-((2*level)+1)])
        self.image = pygame.image.load("./images/"+ self.type + "/" + self.type + ".png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos

        self.health = random.randint(5 + (2*(level-1)), 10 + (2*(level-1)))

        self.clicked = False

    def update(self, action, window, mouse):
        if action == "draw":
            window.blit(self.image, [self.rect.left, self.rect.top])
        if action == "click":
            self.clicked = False
            if self.rect.collidepoint(mouse):
                self.clicked = True
