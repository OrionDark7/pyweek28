#main.py

import pygame
from game import ui

pygame.init()

window = pygame.display.set_mode([1080, 640])
window.fill([255, 255, 255])

screen = "game"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if screen == "game":
        ui.text("test123", [540, 5], window, centered=True)

    pygame.display.flip()

pygame.quit()