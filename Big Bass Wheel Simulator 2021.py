import pygame
import sys
import random
import Score
import Button
import Rect
import PopUp
import Bass
import time

from moviepy.editor import *

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Wheel Test')
screen.fill(pygame.Color('gray'))
clock = pygame.time.Clock()

image25 = pygame.image.load("25.jpg")
image40 = pygame.image.load("40.jpg")
image50 = pygame.image.load("50.jpg")
image75 = pygame.image.load("75.jpg")
image80 = pygame.image.load("80.jpg")
image150 = pygame.image.load("150.jpg")
image250 = pygame.image.load("250.jpg")
image1000 = pygame.image.load("1000.jpg")


def wheel_startup(c, luck):
    r = []
    l = 0
    for k in range(110):
        clock.tick(240)
        if l % (10 / c) == 0:
            r += [Rect.Rect(screen, random.random() * 100, 853, 270, c, luck)]

        for k in range(len(r)):
            r[k].draw()
            r[k].move()
            if k > 4:
                Back2 = r[k - 1]
                Back1 = r[k - 2]
                currentTile = r[k - 3]

        l += 1

    return r, Back2, Back1, currentTile


def wheel_spinning(r, i, l, c, luck):
    if l % (10 / c) == 0:
        if i > 10:
            i = 0
        r[i] = Rect.Rect(screen, random.random() * 100, 853, 270, c, luck)
        i += 1

    for k in range(len(r)):
        r[k].draw()
        r[k].move()
        if k > 5:
            if i - 2 < 0:
                backNum = 10 - (2 - i) + 1
            else:
                backNum = i - 2
            Back2 = r[backNum]
            if i - 3 < 0:
                backNum = 10 - (3 - i) + 1
            else:
                backNum = i - 3
            Back1 = r[backNum]
            if i - 4 < 0:
                backNum = 10 - (4 - i) + 1
            else:
                backNum = i - 4
            currentTile = r[backNum]
    return r, i, l, Back1, Back2, currentTile


def fade_in(object1, object2, speed, offset):
    if object2 is None:
        for a in range(255):
            object1.set_alpha(a)
            screen.blit(object1,
                        (((screen.get_width() // 2) - object1.get_width() // 2), (screen.get_height() // 2) - offset))
            pygame.display.update()
            time.sleep(speed)
    if object2:
        for a in range(255):
            object1.set_alpha(a)
            object2.set_alpha(a)
            screen.blit(object2, (((screen.get_width() // 2) - object1.get_width() * 1.5 // 2),
                                  ((screen.get_height() // 2) - (object1.get_height() * 0.5) // 2) - offset))
            screen.blit(object1,
                        (((screen.get_width() // 2) - object1.get_width() // 2), (screen.get_height() // 2) - offset))
            pygame.display.update()
            time.sleep(speed)


def main():
    while True:

        score = Score.Scoreboard(screen)

        multiplier = 1
        randStop = 0

        bassCount = 5

        bassMult = 1
        spawnMod = 0

        c = 1
        luck = 0
        coin_sound = pygame.mixer.Sound("coin.wav")
        coin_sound.set_volume(0.3)

        splash_sound = pygame.mixer.Sound("Water Splash (trimmed).wav")
        splash_sound.set_volume(3)

        ShopBack = pygame.image.load("Full Shop-01.png")
        ShopBack = pygame.transform.scale(ShopBack, (550, 700))

        LakeBack = pygame.image.load("LakeBack-placeholder.jpg")
        LakeBack = pygame.transform.scale(LakeBack, (750, 700))

        endscreen_img = pygame.image.load("endscreen.png")

        WheelState = "spin"

        r, Back2, Back1, currentTile = wheel_startup(c, luck)

        l = 0
        i = 0

        WheelState = "stop"
        GameState = "menu"

        popUps = []
        b = []

        buttonSpeed = Button.Button(screen, 32, 125, 3000)
        buttonLuck = Button.Button(screen, 32, 275, 8000)
        buttonStop = Button.Button(screen, 32, 425, 2500)
        buttonMult = Button.Button(screen, 32, 575, 5000)
        buttonSpawn = Button.Button(screen, 350, 125, 6000)
        buttonBassMult = Button.Button(screen, 350, 275, 7500)
        buttonBassCount = Button.Button(screen, 350, 425, 3000)
        buttonGoldenBass = Button.Button(screen, 350, 575, 100000000000)

        clip = VideoFileClip('final open p1.mp4')
        clip.preview()
        clip.close()

        # Variables for Main Menu
        menu_bg = pygame.Rect(200, 125, screen.get_width() // 1.5, screen.get_height() // 1.5)
        menu_bg_green = pygame.Surface((screen.get_width(), screen.get_height()))
        menu_bg_green.set_alpha(0)
        menu_bg_green.fill((50, 168, 82))

        menu_heading = "Big Bass Wheel Simulator 2021"
        menu_heading_color = (50, 168, 82)
        menu_heading_font = pygame.font.Font(None, 60)
        menu_heading_render = menu_heading_font.render(menu_heading, True, menu_heading_color)

        menu_play = "PLAY"
        menu_play_color = (122, 145, 255)
        menu_play_font = pygame.font.Font(None, 35)
        menu_play_render = menu_play_font.render(menu_play, True, menu_play_color)
        menu_play_box = pygame.Surface((menu_play_render.get_width() * 1.5, menu_play_render.get_height() * 1.5))
        menu_play_box.set_alpha(0)
        menu_play_box.fill((74, 74, 74))

        menu_help = "HELP"
        menu_help_color = (122, 145, 255)
        menu_help_font = pygame.font.Font(None, 35)
        menu_help_render = menu_help_font.render(menu_help, True, menu_help_color)
        menu_help_box = pygame.Surface((menu_help_render.get_width() * 1.5, menu_help_render.get_height() * 1.5))
        menu_help_box.set_alpha(0)
        menu_help_box.fill((74, 74, 74))

        menu_quit = "QUIT"
        menu_quit_color = (122, 145, 255)
        menu_quit_font = pygame.font.Font(None, 35)
        menu_quit_render = menu_quit_font.render(menu_quit, True, menu_quit_color)
        menu_quit_box = pygame.Surface((menu_quit_render.get_width() * 1.5, menu_quit_render.get_height() * 1.5))
        menu_quit_box.set_alpha(0)
        menu_quit_box.fill((74, 74, 74))

        menu_prompt = "Click any box to continue"
        menu_prompt_color = (168, 168, 168)
        menu_prompt_font = pygame.font.Font(None, 30)
        menu_prompt_render = menu_prompt_font.render(menu_prompt, True, menu_prompt_color)

        if GameState == "menu":
            clock.tick(240)
            screen.fill((0, 0, 0))
            pygame.display.update()
            time.sleep(0.5)

            # Menu Background Fade In
            for a in range(255):
                menu_bg_green.set_alpha(a)
                screen.blit(menu_bg_green, (0, 0))
                pygame.draw.rect(screen, (a, a, a), menu_bg)
                pygame.display.update()

            # Title Fade In
            fade_in(menu_heading_render, None, 0, 200)

            # Play Button Fade In
            fade_in(menu_play_render, menu_play_box, 0, 75)

            # Help Button Fade In
            fade_in(menu_help_render, menu_play_box, 0, 1)

            # Quit Button Fade In
            fade_in(menu_quit_render, menu_play_box, 0, -75)

            # Prompt Text at Bottom
            fade_in(menu_prompt_render, None, 0, -200)

            while GameState == "menu":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_position = event.pos

                        # Play Button
                        if mouse_position[0] >= 555 and mouse_position[0] <= 650 and mouse_position[1] >= 270 and \
                                mouse_position[1] <= 305:
                            GameState = "play"
                            break

                        # Help Button
                        if mouse_position[0] >= 555 and mouse_position[0] <= 650 and mouse_position[1] >= 345 and \
                                mouse_position[1] <= 380:
                            GameState = "help"
                            help_bg = pygame.Rect(200, 125, screen.get_width() // 1.5, screen.get_height() // 1.5)
                            pygame.draw.rect(screen, (255, 255, 255), help_bg)
                            help_text = "Big Bass Wheel Simulator 2021"
                            help_text_color = (50, 168, 82)
                            help_text_font = pygame.font.Font(None, 60)
                            help_text_render = help_text_font.render(help_text, True, help_text_color)
                            screen.blit(help_text_render, (
                            ((screen.get_width() // 2) - help_text_render.get_width() // 2),
                            (screen.get_height() // 2) - 200))

                            help_text1_color = (168, 168, 168)
                            help_text1_font = pygame.font.Font(None, 30)
                            help_text1 = "Welcome to our rendition of the Big Bass Wheel arcade game!"
                            help_text1_render = help_text1_font.render(help_text1, True, help_text1_color)
                            screen.blit(help_text1_render, (
                            ((screen.get_width() // 2) - help_text1_render.get_width() // 2),
                            (screen.get_height() // 2) - 150))

                            help_text2_color = (0, 0, 0)
                            help_text2_font = pygame.font.Font(None, 25)

                            help_text2 = "This game is based on pure luck at the start, but you can purchase upgrades that will"
                            help_text2_render = help_text2_font.render(help_text2, True, help_text2_color)
                            screen.blit(help_text2_render, (
                            ((screen.get_width() // 2) - help_text2_render.get_width() // 2),
                            (screen.get_height() // 2) - 85))

                            help_text3 = "increase your chance of winning with the more upgrades you buy. To play the game, simply"
                            help_text3_render = help_text2_font.render(help_text3, True, help_text2_color)
                            screen.blit(help_text3_render, (
                            ((screen.get_width() // 2) - help_text3_render.get_width() // 2),
                            (screen.get_height() // 2) - 65))

                            help_text4 = "press the up arrow key to spin the wheel. After coming to a stop, the wheel will display"
                            help_text4_render = help_text2_font.render(help_text4, True, help_text2_color)
                            screen.blit(help_text4_render, (
                            ((screen.get_width() // 2) - help_text4_render.get_width() // 2),
                            (screen.get_height() // 2) - 45))

                            help_text5 = "how many points you won for that spin. These points can be spent in the shop to add"
                            help_text5_render = help_text2_font.render(help_text5, True, help_text2_color)
                            screen.blit(help_text5_render, (
                            ((screen.get_width() // 2) - help_text5_render.get_width() // 2),
                            (screen.get_height() // 2) - 25))

                            help_text6 = "additional enhancements to the game, such as an increased spin speed, higher point values,"
                            help_text6_render = help_text2_font.render(help_text6, True, help_text2_color)
                            screen.blit(help_text6_render, (
                            ((screen.get_width() // 2) - help_text6_render.get_width() // 2),
                            (screen.get_height() // 2) - 5))

                            help_text7 = "and the \"Golden Bass\" which is how you win the game. In addition to the points won from"
                            help_text7_render = help_text2_font.render(help_text7, True, help_text2_color)
                            screen.blit(help_text7_render, (
                            ((screen.get_width() // 2) - help_text7_render.get_width() // 2),
                            (screen.get_height() // 2) + 15))

                            help_text8 = "spinning the wheel, points can also be acquired from clicking on fish that randomly swim"
                            help_text8_render = help_text2_font.render(help_text8, True, help_text2_color)
                            screen.blit(help_text8_render, (
                            ((screen.get_width() // 2) - help_text8_render.get_width() // 2),
                            (screen.get_height() // 2) + 35))

                            help_text9 = "across the screen. Thank you for playing our game and we hope you enjoy!"
                            help_text9_render = help_text2_font.render(help_text9, True, help_text2_color)
                            screen.blit(help_text9_render, (
                            ((screen.get_width() // 2) - help_text9_render.get_width() // 2),
                            (screen.get_height() // 2) + 55))

                            help_text10_color = (168, 168, 168)
                            help_text10_font = pygame.font.Font(None, 20)
                            help_text10 = "Created By: Ed, Swade, and Ryan."
                            help_text10_render = help_text10_font.render(help_text10, True, help_text10_color)
                            screen.blit(help_text10_render, (
                            ((screen.get_width() // 2) - help_text10_render.get_width() // 2),
                            (screen.get_height() // 2) + 200))

                            menu_back = "Let's Play!"
                            menu_back_color = (122, 145, 255)
                            menu_back_font = pygame.font.Font(None, 35)
                            menu_back_render = menu_back_font.render(menu_back, True, menu_back_color)
                            menu_back_box = pygame.Surface(
                                (menu_back_render.get_width() * 1.5, menu_back_render.get_height() * 1.5))
                            menu_back_box.set_alpha(255)
                            menu_back_box.fill((74, 74, 74))

                            # Back Button Fade In
                            fade_in(menu_back_render, menu_back_box, 0, -150)

                            pygame.display.update()
                            while GameState == "help":
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        mouse_position = event.pos
                                        print(mouse_position)
                                        if mouse_position[0] >= 550 and mouse_position[0] <= 650 and mouse_position[
                                            1] >= 500 and mouse_position[1] <= 530:
                                            GameState = "play"
                                            break

                        # Quit Button
                        if mouse_position[0] >= 555 and mouse_position[0] <= 650 and mouse_position[1] >= 425 and \
                                mouse_position[1] <= 455:
                            pygame.quit()
                            sys.exit()

        clip = VideoFileClip('final open p2.mp4')
        clip.preview()
        clip.close()
        pygame.mixer.music.load("BGM.mp3")
        pygame.mixer.music.play(-1, 3, 2000)
        pygame.mixer.music.set_volume(0.65)

        # Sets up exit button
        menu_exit = "EXIT"
        menu_exit_color = (219, 0, 0)
        menu_exit_font = pygame.font.Font(None, 35)
        menu_exit_render = menu_exit_font.render(menu_exit, True, menu_exit_color)
        menu_exit_box = pygame.Surface((menu_exit_render.get_width() * 1.5, menu_exit_render.get_height() * 1.5))
        menu_exit_box.fill((120, 120, 120))

        GameState = "play"

        while GameState == "play":
            clock.tick(240)

            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP and pressed[pygame.K_UP] and WheelState != "spin":
                    WheelState = "spin"
                    score.score -= 10
                    coin_sound.play(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    click_pos = event.pos
                    buttonSpeed.is_clicked(click_pos)
                    buttonLuck.is_clicked(click_pos)
                    buttonStop.is_clicked(click_pos)
                    buttonMult.is_clicked(click_pos)
                    buttonSpawn.is_clicked(click_pos)
                    buttonBassMult.is_clicked(click_pos)
                    buttonBassCount.is_clicked(click_pos)
                    buttonGoldenBass.is_clicked(click_pos)

                    if click_pos[0] >= 1135 and click_pos[0] <= 1200 and click_pos[1] >= 5 and click_pos[1] <= 30:
                        pygame.quit()
                        sys.exit()

                    if len(b) >= 1:
                        for k in range(len(b)):
                            b[k].is_clicked(click_pos, score)

            clock.tick(60)
            screen.fill(pygame.Color('gray'))

            screen.blit(LakeBack, (550, 0))

            screen.blit(ShopBack, (0, 0))

            screen.blit(menu_exit_box, (screen.get_width() - menu_exit_render.get_width() - 5, -10))
            screen.blit(menu_exit_render, (screen.get_width() - menu_exit_render.get_width(), 0))

            if WheelState == "spin":
                r, i, l, Back1, Back2, currentTile = wheel_spinning(r, i, l, c, luck)

                if l % ((300 - random.randint(0, randStop) * 10) / c) == 0 and l > 1:
                    WheelState = "stop"
                    popUps += [PopUp.PopUp(currentTile.value, screen, multiplier)]
                    score.score += currentTile.value * multiplier
                    for k in range(len(r)):
                        r[k].y -= (c - 1) * 6.5

                l += 1

            for k in range(len(r)):
                r[k].draw()

            if len(r) > 6:
                Back2.draw()
                Back1.draw()
                currentTile.draw()

            BassWheel = pygame.image.load("bigbasswheel.png")
            screen.blit(BassWheel, (817, 703 - BassWheel.get_height()))

            for k in range(len(popUps)):
                popUps[k].draw()
                popUps[k].move()

            if len(popUps) > 100:
                for k in range(len(popUps)):
                    popUps[k].draw()
                    popUps[k].move()
                popUps = []

            buttonSpeed.draw()
            buttonLuck.draw()
            buttonStop.draw()
            buttonMult.draw()
            buttonSpawn.draw()
            buttonBassMult.draw()
            buttonBassCount.draw()
            buttonGoldenBass.draw()

            if buttonSpeed.clicked:
                if buttonSpeed.activate(score):
                    if buttonSpeed.presscount == 1:
                        buttonSpeed.cost = 7000
                        c = 2
                    if buttonSpeed.presscount == 2:
                        buttonSpeed.cost = 20000
                        c = 2.5
                    if buttonSpeed.presscount == 3:
                        buttonSpeed.cost = 60000
                        c = 5
                    if buttonSpeed.presscount >= 4:
                        buttonSpeed.cost = 0
                        c = 10

            if buttonLuck.clicked:
                if buttonLuck.activate(score):
                    buttonLuck.cost = int(buttonLuck.cost * 1.3)
                    luck += .5

            if buttonStop.clicked:
                if buttonStop.activate(score):
                    if buttonStop.presscount < 28:
                        buttonStop.cost = int(buttonStop.cost * 1.2)
                        randStop += 1
                    if buttonStop.presscount == 28:
                        buttonStop.cost = 0
                        randStop += 1

            if buttonMult.clicked:
                if buttonMult.activate(score):
                    buttonMult.cost = int(buttonMult.cost * 2.2)
                    multiplier = multiplier * 2

            if buttonSpawn.clicked:
                if buttonSpawn.activate(score):
                    if buttonSpawn.presscount < 39:
                        buttonSpawn.cost = int(buttonSpawn.cost * 1.4)
                        spawnMod += .05
                    if buttonSpawn.presscount == 39:
                        buttonSpawn.cost = 0
                        spawnMod += .05

            if buttonBassMult.clicked:
                if buttonBassMult.activate(score):
                    buttonBassMult.cost = int(buttonBassMult.cost * 2.2)
                    bassMult = bassMult * 2

            if buttonBassCount.clicked:
                if buttonBassCount.activate(score):
                    buttonBassCount.cost = int(buttonBassCount.cost * 1.2)
                    bassCount += 1

            if buttonGoldenBass.clicked:
                if buttonGoldenBass.activate(score):
                    GameState = "End"

            if random.random() * 100 > (99.93):
                b = []
                splash_sound.play()
                for k in range(bassCount):
                    b += [Bass.Bass(screen, bassMult)]
            elif random.random() * 100 > (99.88 - spawnMod):
                b += [Bass.Bass(screen, bassMult)]

            if len(b) > (100 + bassCount):
                b = []

            if len(b) >= 1:
                for k in range(len(b)):
                    b[k].drawAndMove()

            score.draw()
            pygame.display.update()

        if GameState == "End":
            pygame.mixer.music.stop()
            clip = VideoFileClip("final cutscene.mp4")
            clip.preview()
            GameState = "Waiting"

        while GameState == "Waiting":
            clock.tick(60)
            screen.blit(endscreen_img, (0, 0))

            pressed_key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if pressed_key[pygame.K_SPACE]:
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    time.sleep(0.5)
                    GameState = "Play"

            pygame.display.update()


main()
