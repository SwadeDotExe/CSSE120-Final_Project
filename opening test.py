from moviepy.editor import *
import sys
import pygame
import Button as b
import Score


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("button test")
    screen = pygame.display.set_mode((500, 500))
    button = b.Button(screen, 100, 100, 500)
    scoreboard = Score.Scoreboard(screen)
    clip = VideoFileClip('final open p1.mp4')
    print("video start")
    clip.preview()
    clip.close()
    clip = VideoFileClip('final open p2.mp4')
    clip.preview()
    clip.close()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            press = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                click_pos = event.pos
                button.is_clicked(click_pos)
            if press[pygame.K_LEFT]:
                scoreboard.givemoney()
                button.cost = button.cost * 2.1035

        screen.fill((0, 0, 0))

        if button.clicked:
            button.activate(scoreboard)
        scoreboard.draw()
        button.draw()
        pygame.display.update()

main()