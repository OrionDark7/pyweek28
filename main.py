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
pygame.time.set_timer(pygame.USEREVENT+2, 1000)

mouse = [0,0]
pressed = [0, 0, 0]

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

attackcolors0 = [(255, 10, 0), (20, 120, 204), (249, 255, 127)]
icons = [pygame.image.load("./images/icons/block.png"), pygame.image.load("./images/icons/attack.png"), ]
hit = True
effect = 1
indicator = -1
hits = 1
time = 0
starthits = 1
timechange = 0
indicator1 = pygame.surface.Surface([200, 150])
indicator2 = pygame.surface.Surface([200, 150])
indicator3 = pygame.surface.Surface([200, 150])
indicator1.fill([249, 255, 127])
indicator2.fill([249, 255, 127])
indicator3.fill([249, 255, 127])

ui.fontSize(32)
ui.color = [255, 255, 255]
returntomenu = ui.button("RETURN TO MENU", [400, 290], centered=True)

menubuttons = pygame.sprite.Group()
play = ui.button("PLAY", [400, 290], centered=True)
menubuttons.add(play)
howto = ui.button("HOW TO PLAY", [400, 340], centered=True)
menubuttons.add(howto)
quitbutton = ui.button("QUIT", [400, 390], centered=True)
menubuttons.add(quitbutton)

cursor = attackmod.cursor()
boxgrp = pygame.sprite.Group()

power = 0
enemypower = 0
ups = 0
min = 60
max = 90

level = 1
animation = 0

sequence = "1234567890"
newsequence = ""
characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

player = entities.Player()
mobs = pygame.sprite.Group()
j = random.randint(1, 3)
for i in range(j):
    mob = entities.Mob([256 + ((i)*100), 278], level)
    mobs.add(mob)
amob = None

screen = "menu"

running = True

def generateSequence():
    global characters
    newstring = ""
    for i in range(random.randint(4, 7)):
        newstring = newstring + random.choice(characters)
    return newstring

def update(action, group):
    global mobs, mouse, pressed, cursor
    if group == mobs:
        mobs.update(str(action), window, mouse)
    if group == boxgrp:
        boxgrp.update(cursor.rect, pressed)

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
                            attack = random.randint(0, 3)
                            screen = "attack"
                            timechange = 0
                            pygame.time.set_timer(pygame.USEREVENT, 1000)
                            if attack == 2:
                                effect = random.randint(0, 1)
                                pygame.time.set_timer(pygame.USEREVENT + 1, 2)
                            elif attack == 1:
                                player.health += 1
                            elif attack == 3:
                                sequence = generateSequence()
                                pygame.time.set_timer(pygame.USEREVENT + 1, 2)
                                time = random.randint(5, 9)
                                pygame.time.set_timer(pygame.USEREVENT, time * 1000)
                            else:
                                pygame.time.set_timer(pygame.USEREVENT + 1, 100)
                elif screen == "game over":
                    if returntomenu.click(mouse):
                        screen = "menu"
                elif screen == "menu":
                    if play.click(mouse):
                        screen = "game"
                    elif quitbutton.click(mouse):
                        running = False
                    elif howto.click(mouse):
                        screen = "how to play"
            if pressed[0] == 1 or pressed[2] == 1:
                if screen == "attack":
                    if attack == 1:
                        update("click", boxgrp)
                        clicked = False
                        for bx in boxgrp:
                            if bx.clicked:
                                clicked = True
                                if bx.type == 0 and pressed[0]:
                                    player.health -= 1
                                elif bx.type == 1 and pressed[0]:
                                    amob.health -= 1
                                elif bx.type == 0 and pressed[1]:
                                    bx.kill()
                                bx.kill()
                                break
                        if not clicked:
                            player.health -= 1
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
                elif attack == 2:
                    if event.key == pygame.K_SPACE:
                        pygame.time.set_timer(pygame.USEREVENT+1, 2)
                        ups = 10
                    elif (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) and power >= enemypower and enemypower >= min:
                        enemypower = 0
                        if effect == 1:
                            amob.health -= 1
                        effect = random.randint(0, 1)
                        min = random.randint(50, 80)
                        max = random.randint(min + 15, 100)
                elif attack == 3:
                    if pygame.key.name(event.key) in characters and len(newsequence) < 10:
                        newsequence = newsequence + pygame.key.name(event.key)
                    elif event.key == pygame.K_BACKSPACE and len(newsequence) > 0:
                        newsequence = newsequence[0:len(newsequence)-1]
        if event.type == pygame.USEREVENT:
            if screen == "attack":
                if attack == 0:
                    if not hit and effect == 0:
                        player.health -= 1
                    if not hit:
                        indicator = random.randint(0,2)
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

                    pygame.time.set_timer(pygame.USEREVENT, random.randint(800, 1600))
                    hit=False
                if attack == 1:
                    boxgrp.add(attackmod.hitbox())
                    pygame.time.set_timer(pygame.USEREVENT, random.randint(1000, 2000))
                if attack == 3:
                    if effect == 0:
                        player.health -= 1
                        effect = random.randint(0, 1)
                        time = random.randint(5, 9)
                        pygame.time.set_timer(pygame.USEREVENT+2, time * 1000)

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
                elif attack == 2:
                    if enemypower < 100:
                        if random.randint(1, 4) == 1:
                            enemypower += random.choice([0.25, 0.5, 1])
                    if enemypower >= 100:
                        if effect == 0:
                            player.health -= 1
                        enemypower = 0
                        effect = random.randint(0, 1)
                        max = random.randint(min + 15, 100)

                    if power > 0:
                        power -= 1
                    if power >= 100:
                        power = 100

                    if ups > 0:
                        ups -= 1
                        power += 2
            if screen == "enemy defeated":
                a += 1
        if event.type == pygame.USEREVENT+2:
            if screen == "attack":
                if attack == 3:
                    time -= 1


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
        if player.health <= 0:
            screen = "game over"
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
            ui.text("Press D", [650, 396], window, centered=True)


            if indicator >= 0:
                bar = pygame.surface.Surface([(hits / starthits) * 200, 5])
                bar2 = pygame.surface.Surface([200, 5])

                bar2.fill([100, 100, 100])
                bar.fill([255, 255, 255])

                window.blit(bar2, [50 + (indicator*250), 370])
                window.blit(bar, [50 + (indicator * 250), 370])

                window.blit(icons[effect], [86 + (indicator * 250), 237])

            ui.fontSize(16)
            ui.text("YOUR HEALTH", [100, 500], window, centered=True)
            ui.text("ENEMY HEALTH", [690, 500], window, centered=True)

            if amob.health <= 0:
                amob.kill()
                screen = "enemy defeated"
                animation = 0
                a = 1
                pygame.time.set_timer(pygame.USEREVENT + 1, 2)

        if attack == 1:
            ui.color = [255, 255, 255]

            ui.fontSize(64)
            ui.text("ATTACK", [400, 5], window, centered=True)
            ui.text(player.health, [100, 520], window, centered=True)
            ui.text(amob.health, [690, 520], window, centered=True)

            surface = pygame.surface.Surface([600, 10])
            surface.fill((255, 255, 255))
            window.blit(surface, [100, 295])

            boxgrp.draw(window)
            cursor.update("draw", window)

            ui.fontSize(16)
            ui.text("YOUR HEALTH", [100, 500], window, centered=True)
            ui.text("ENEMY HEALTH", [690, 500], window, centered=True)

            if amob.health <= 0:
                amob.kill()
                screen = "enemy defeated"
                animation = 0
                a = 1
                pygame.time.set_timer(pygame.USEREVENT + 1, 2)

        if attack == 2:
            ui.color = [255, 255, 255]
            ui.fontSize(64)
            ui.text("ATTACK", [400, 5], window, centered=True)
            ui.text(player.health, [100, 520], window, centered=True)
            ui.text(amob.health, [690, 520], window, centered=True)

            ui.fontSize(16)
            ui.text("YOUR HEALTH", [100, 500], window, centered=True)
            ui.text("ENEMY HEALTH", [690, 500], window, centered=True)

            powerbar = pygame.surface.Surface([600, 50])
            powerbar2 = pygame.surface.Surface([(power/100) * 600, 50])

            powerbar.fill([216, 174, 245])
            powerbar2.fill([175, 64, 245])

            enemybar = pygame.surface.Surface([600, 50])
            enemybar2 = pygame.surface.Surface([(enemypower/100) * 600, 50])

            if effect == 0:
                enemybar2.fill((255, 10, 0))
                enemybar.fill((255, 110, 100))
            elif effect == 1:
                enemybar2.fill((20, 120, 204))
                enemybar.fill((120, 220, 255))

            window.blit(enemybar, [100, 340])
            window.blit(enemybar2, [100, 340])

            window.blit(powerbar, [100, 410])
            window.blit(powerbar2, [100, 410])

            minbar = pygame.surface.Surface([5, 60])
            minbar.fill([255, 255, 255])
            window.blit(minbar, [100 + ((min / 100) * 600), 335])

            maxbar = pygame.surface.Surface([5, 60])
            maxbar.fill((255, 10, 0))
            window.blit(maxbar, [100 + ((max / 100) * 600), 405])

            ui.text("POWER", [100, 465], window)
            ui.text("ENEMY POWER", [100, 320], window)

            if power > max:
                #min = random.randint(60, 80)
                #max = random.randint(min+10, 100)
                #effect = random.randint(0, 1)
                power = 0

            if amob.health <= 0:
                amob.kill()
                screen = "enemy defeated"
                animation = 0
                a = 1
                pygame.time.set_timer(pygame.USEREVENT + 1, 2)

        if attack == 3:
            ui.color = [255, 255, 255]
            ui.fontSize(64)
            ui.text("ATTACK", [400, 5], window, centered=True)
            ui.text(player.health, [100, 520], window, centered=True)
            ui.text(amob.health, [690, 520], window, centered=True)

            ui.fontSize(16)
            ui.text("YOUR HEALTH", [100, 500], window, centered=True)
            ui.text("ENEMY HEALTH", [690, 500], window, centered=True)

            if  len(newsequence) == len(sequence) and newsequence == sequence:
                if effect == 1:
                    amob.health -= 1
                newsequence = ""
                sequence = generateSequence()
                time = random.randint(5, 9)
                pygame.time.set_timer(pygame.USEREVENT, time*1000)
                pygame.time.set_timer(pygame.USEREVENT + 2, 1000)
            elif len(newsequence) == len(sequence) and not newsequence == sequence:
                player.health -= 1
                newsequence = ""
                sequence = generateSequence()
                time = random.randint(5, 9)
                pygame.time.set_timer(pygame.USEREVENT, time * 1000)
                pygame.time.set_timer(pygame.USEREVENT + 2, 1000)

            ui.fontSize(32)
            if effect == 0:
                ui.color = attackcolors0[0]
            elif effect == 1:
                ui.color = attackcolors0[1]
            ui.text(sequence, [400, 250], window, centered=True)
            ui.color = [255, 255, 255]
            ui.text(newsequence, [400, 300], window, centered=True)

            if time <= 0:
                print("in")
                if effect == 0:
                    player.health -= 1
                newsequence = ""
                sequence = generateSequence()
                time = random.randint(5, 9)
                pygame.time.set_timer(pygame.USEREVENT, time * 1000)
                pygame.time.set_timer(pygame.USEREVENT + 2, 1000)

            ui.text("time left  " + str(time), [400, 400], window, centered=True)

            if amob.health <= 0:
                amob.kill()
                screen = "enemy defeated"
                animation = 0
                a = 1
                pygame.time.set_timer(pygame.USEREVENT + 1, 2)

    if screen == "game over":
        window.fill([30, 30, 30])

        ui.fontSize(64)
        ui.text("GAME OVER", [400, 5], window, centered=True)

        returntomenu.update(window)

    if screen == "menu":
        window.fill([30, 30, 30])

        ui.fontSize(60)
        ui.text("TOWER OF DOOM", [400, 5], window, centered=True)

        menubuttons.draw(window)

    if screen == "how to play":
        window.fill([30, 30, 30])

    if screen == "enemy defeated":
        if animation == 0:
            surface = pygame.surface.Surface([8*a, 6*a])
            surface.fill([30, 30, 30])
            window.blit(surface, [396 - (4*a), 297 - (3*a)])
            if a >= 100:
                animation = 1
                a = 0
        if animation == 1:
            surface = pygame.surface.Surface([800, 600])
            surface.fill([30, 30, 30])
            window.blit(surface, [0, 0])
            ui.color = [255, 255, 255]
            ui.fontSize(48)
            ui.text("ENEMY DEFEATED", [400, (a*a)/2], window, centered = True)
            if (a*a)/2 >= 290:
                animation = 2
                a = 0
        if animation == 2:
            surface = pygame.surface.Surface([800, 600])
            surface.fill([30, 30, 30])
            window.blit(surface, [0, 0])
            ui.color = [255, 255, 255]
            ui.fontSize(48)
            ui.text("ENEMY DEFEATED", [400, 290], window, centered=True)
            if a >= 1000:
                animation = 3
                a = 0
        if animation == 3:
            surface = pygame.surface.Surface([800, 600])
            surface.fill([30, 30, 30])
            window.blit(surface, [0, 0])
            ui.color = [255, 255, 255]
            ui.fontSize(48)
            ui.text("ENEMY DEFEATED", [400, 290], window, centered=True)


    pygame.display.flip()

pygame.quit()