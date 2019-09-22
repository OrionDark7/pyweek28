#main.py

import pygame, random
from game import ui, entities

pygame.init()

window = pygame.display.set_mode([800, 600])
pygame.display.set_caption("PyWeek 28")
window.fill([255, 255, 255])

pygame.time.set_timer(pygame.USEREVENT, 1000)

mouse = [0,0]

attackcolors0 = [(255, 10, 0), (20, 120, 204)]
hit = True
effect = 1
indicator = 0
indicator1 = pygame.surface.Surface([200, 150])
indicator2 = pygame.surface.Surface([200, 150])
indicator3 = pygame.surface.Surface([200, 150])
indicator1.fill([249, 255, 127])
indicator2.fill([249, 255, 127])
indicator3.fill([249, 255, 127])

player = entities.Player()
mob = entities.Mob([256, 278])
mobs = pygame.sprite.Group()
mobs.add(mob)
amob = None
timechange = 0

screen = "game"

running = True

def update(action, group):
    global mobs, mouse
    if group == mobs:
        mobs.update(str(action), window, mouse)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed()
            mouse = event.pos[0], event.pos[1]
            if pressed[0] == 1:
                if screen == "game":
                    update("click", mobs)
                    for cmob in mobs:
                        if cmob.clicked:
                            amob = cmob
                            attack = 0
                            screen = "attack"
        if event.type == pygame.KEYDOWN:
            if screen == "attack":
                if attack == 0:
                    if event.key == pygame.K_1:
                        if indicator == 0:
                            hit = True
                            if effect == 0:
                                indicator1.fill([179, 24, 18])
                            else:
                                indicator1.fill([9, 101, 179])
                                amob.health -= 1
                            pygame.time.set_timer(pygame.USEREVENT, 100)
                            effect = 2
                            timechange += random.randint(1, 4) * 200
                    if event.key == pygame.K_2:
                        if indicator == 1:
                            hit = True
                            if effect == 0:
                                indicator2.fill([179, 24, 18])
                            else:
                                indicator2.fill([9, 101, 179])
                                amob.health -= 1
                            pygame.time.set_timer(pygame.USEREVENT, 100)
                            effect = 2
                            timechange += random.randint(1, 4) * 200
                    if event.key == pygame.K_3:
                        if indicator == 2:
                            hit = True
                            if effect == 0:
                                indicator3.fill([179, 24, 18])
                            else:
                                indicator3.fill([9, 101, 179])
                                amob.health -= 1
                            pygame.time.set_timer(pygame.USEREVENT, 100)
                            effect = 2
                            timechange += random.randint(1, 4) * 200

        if event.type == pygame.USEREVENT:
            if screen == "attack":
                print("in")
                if not hit and effect == 0:
                    player.health -= 1
                    print("in 1")
                if not hit:
                    indicator = random.randint(0,2)
                    print(indicator)
                    effect = random.randint(0, 1)

                    indicator1.fill([249, 255, 127])
                    indicator2.fill([249, 255, 127])
                    indicator3.fill([249, 255, 127])

                    if indicator == 0:
                        indicator1.fill(attackcolors0[effect])
                    elif indicator == 1:
                        indicator2.fill(attackcolors0[effect])
                    elif indicator == 2:
                        indicator3.fill(attackcolors0[effect])
                if hit and effect == 2:
                    indicator1.fill([249, 255, 127])
                    indicator2.fill([249, 255, 127])
                    indicator3.fill([249, 255, 127])

                if timechange > 2500: timechange = 2500

                pygame.time.set_timer(pygame.USEREVENT, random.randint(3000-timechange, 5000-timechange))
                hit=False


    if screen == "game":
        window.fill([255, 255, 255])
        render = pygame.surface.Surface([700, 100])
        render.fill([143, 72, 10])
        window.blit(render, [100, 300])
        player.draw(window)
        update("draw", mobs)

    if screen == "attack":
        window.fill([30, 30, 30])
        if attack == 0:
            ui.color = [255, 255, 255]

            ui.fontSize(64)
            ui.text("ATTACK", [400,5], window, centered=True)
            ui.text(player.health, [100, 520], window, centered=True)
            ui.text(amob.health, [690, 520], window, centered=True)

            ui.fontSize(32)
            window.blit(indicator1, [50, 225])
            ui.text("1", [150, 396], window, centered=True)
            window.blit(indicator2, [300, 225])
            ui.text("2", [400, 396], window, centered=True)
            window.blit(indicator3, [550, 225])
            ui.text("3", [650, 396], window, centered=True)

            ui.fontSize(16)
            ui.text("YOUR HEALTH", [100, 500], window, centered=True)
            ui.text("ENEMY HEALTH", [690, 500], window, centered=True)

            if amob.health <= 0:
                amob.kill()
                screen = "game"

    pygame.display.flip()

pygame.quit()