#main.py

import pygame, random
from game import ui, entities
from game import attack as attackmod

pygame.init()

window = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Tower of Doom ")
window.fill([255, 255, 255])

pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.time.set_timer(pygame.USEREVENT+1, 200)

mouse = [0,0]

wall2 = pygame.image.load("./images/textures/wall2.png")
wall = pygame.image.load("./images/textures/wall.png")

surf = pygame.surface.Surface([640, 640])
for x in range(10):
    for y in range(10):
        surf.blit(wall2, [x*64, y*64])

side1 = pygame.surface.Surface([64, 640])
side2 = pygame.surface.Surface([64, 640])
for i in range(10):
    side1.blit(wall, [0, i * 64])
    side2.blit(wall, [0, i * 64])

attackcolors0 = [(255, 10, 0), (20, 120, 204), [249, 255, 127]]
hit = True
effect = 1
indicator = 0
hits = 1
starthits = 1
timechange = 0
indicator1 = pygame.surface.Surface([200, 150])
indicator2 = pygame.surface.Surface([200, 150])
indicator3 = pygame.surface.Surface([200, 150])
indicator1.fill([249, 255, 127])
indicator2.fill([249, 255, 127])
indicator3.fill([249, 255, 127])

cubes = pygame.sprite.Group()

player = entities.Player()
mobs = pygame.sprite.Group()
j = random.randint(1, 3)
for i in range(j):
    print(i)
    mob = entities.Mob([256 + ((i)*100), 278])
    mobs.add(mob)
amob = None
print(mobs)

screen = "game"

running = True

def update(action, group):
    global mobs, mouse, cubes
    if group == mobs:
        mobs.update(str(action), window, mouse)
    elif group == cubes:
        cubes.update(str(action), window, mouse)

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
                            timechange = 0
                            pygame.time.set_timer(pygame.USEREVENT, 1000)
                if screen == "attack":
                    if attack == 1:
                        update("click", cubes)
                        for i in cubes:
                            if i.clicked:
                                if i.type == 0:
                                    amob.health -= 1
        if event.type == pygame.KEYDOWN:
            if screen == "attack":
                if attack == 0:
                    if event.key == pygame.K_a:
                        if indicator == 0 and hits == 1:
                            hit = True
                            if effect == 0:
                                indicator1.fill([179, 24, 18])
                                indicator = -1
                            else:
                                indicator1.fill([9, 101, 179])
                                amob.health -= 1
                                indicator = -1
                            pygame.time.set_timer(pygame.USEREVENT, 100)
                            effect = 2
                            timechange += random.randint(1, 4) * 200
                        elif indicator == 0:
                            hits -=1
                            if effect == 0:
                                indicator1.fill([179, 24, 18])
                            else:
                                indicator1.fill([9, 101, 179])
                            pygame.time.set_timer(pygame.USEREVENT + 1, 100)
                    if event.key == pygame.K_s:
                        if indicator == 1 and hits == 1:
                            hit = True
                            if effect == 0:
                                indicator2.fill([179, 24, 18])
                                indicator = -1
                            else:
                                indicator2.fill([9, 101, 179])
                                indicator = -1
                                amob.health -= 1
                            pygame.time.set_timer(pygame.USEREVENT, 100)
                            effect = 2
                            timechange += random.randint(1, 4) * 200
                        elif indicator == 1:
                            hits -=1
                            if effect == 0:
                                indicator2.fill([179, 24, 18])
                            else:
                                indicator2.fill([9, 101, 179])
                            pygame.time.set_timer(pygame.USEREVENT + 1, 100)
                    if event.key == pygame.K_d:
                        if indicator == 2 and hits == 1:
                            hit = True
                            if effect == 0:
                                indicator3.fill([179, 24, 18])
                                indicator = -1
                            else:
                                indicator3.fill([9, 101, 179])
                                amob.health -= 1
                                indicator = -1
                            pygame.time.set_timer(pygame.USEREVENT, 100)
                            effect = 2
                            timechange += random.randint(1, 4) * 200
                        elif indicator == 2:
                            hits -=1
                            if effect == 0:
                                indicator3.fill([179, 24, 18])
                            else:
                                indicator3.fill([9, 101, 179])
                            pygame.time.set_timer(pygame.USEREVENT + 1, 100)

        if event.type == pygame.USEREVENT:
            if screen == "attack":
                if attack == 0:
                    print("in")
                    if not hit and effect == 0:
                        player.health -= 1
                        print("in 1")
                    if not hit:
                        indicator = random.randint(0,2)
                        print(indicator)
                        hits = random.randint(3, 7)
                        starthits = hits
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
                        hits = 0
                        indicator1.fill([249, 255, 127])
                        indicator2.fill([249, 255, 127])
                        indicator3.fill([249, 255, 127])

                    if timechange > 2500: timechange = 2500

                    pygame.time.set_timer(pygame.USEREVENT, random.randint(500, 2000))
                    hit=False
                if attack == 1:
                    cubes.add(attackmod.fallingobj())

        if event.type == pygame.USEREVENT + 1:
            if screen == "attack":
                if attack == 0 and not hits == 0:
                    if indicator == 0:
                        indicator1.fill(attackcolors0[effect])
                        indicator2.fill([249, 255, 127])
                        indicator3.fill([249, 255, 127])
                    elif indicator == 1:
                        indicator1.fill([249, 255, 127])
                        indicator2.fill(attackcolors0[effect])
                        indicator3.fill([249, 255, 127])
                    elif indicator == 2:
                        indicator1.fill([249, 255, 127])
                        indicator2.fill([249, 255, 127])
                        indicator3.fill(attackcolors0[effect])

    if screen == "game":
        window.fill([0, 200, 255])
        window.blit(surf, [80, 0])
        render = pygame.surface.Surface([700, 400])
        render.fill([143, 72, 10])
        window.blit(render, [50, 320])
        window.blit(side1, [32, 0])
        window.blit(side2, [704, 0])
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
            ui.text("Press A", [150, 396], window, centered=True)
            window.blit(indicator2, [300, 225])
            ui.text("Press S", [400, 396], window, centered=True)
            window.blit(indicator3, [550, 225])
            ui.text("Press D1", [650, 396], window, centered=True)

            print(indicator)

            if indicator >= 0:
                print("in")
                bar = pygame.surface.Surface([(hits / starthits) * 200, 5])
                bar2 = pygame.surface.Surface([200, 5])

                bar2.fill([100, 100, 100])
                bar.fill([255, 255, 255])

                window.blit(bar2, [50 + (indicator*250), 370])
                window.blit(bar, [50 + (indicator * 250), 370])

            ui.fontSize(16)
            ui.text("YOUR HEALTH", [100, 500], window, centered=True)
            ui.text("ENEMY HEALTH", [690, 500], window, centered=True)

            print(timechange)

            if amob.health <= 0:
                amob.kill()
                screen = "game"

        if attack == 1:
            ui.color = [255, 255, 255]

            ui.fontSize(64)
            ui.text("ATTACK", [400, 5], window, centered=True)

            surface = pygame.surface.Surface([800, 50])
            surface.fill((20, 120, 204))
            window.blit(surface, [0, 750])

            update("draw", cubes)
            update("fall", cubes)

    pygame.display.flip()

pygame.quit()