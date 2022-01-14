import pygame
import sys
import random

pygame.init()



class PopUp(object):
    def num_to_word(self):
        if self.trueVal < 10000:
            self.trueVal_word = str(round(self.trueVal))
        elif self.trueVal < 1000000:
            self.trueVal_word = str(round(self.trueVal / 1000, 2)) + "K"
        elif self.trueVal < 1000000000:
            self.trueVal_word = str(round(self.trueVal / 1000000, 2)) + "M"
        elif self.trueVal < 1000000000000:
            self.trueVal_word = str(round(self.trueVal / 1000000000, 2)) + "B"
        elif self.trueVal < 1000000000000000:
            self.trueVal_word = str(round(self.trueVal / 1000000000000, 2)) + "T"
        elif self.trueVal < 1000000000000000000:
            self.trueVal_word = str(round(self.trueVal / 1000000000000000, 2)) + "Q"
        elif self.trueVal < 1000000000000000000000000000000000000:
            self.trueVal_word = "Bruh"



    def __init__(self, value, screen, multiplier):
        self.x = random.randint(560, 1000)
        self.y = random.randint(5, 550)
        self.screen = screen
        self.value = value
        self.trueVal = value * multiplier
        self.num_to_word()
        self.text = ("+" + self.trueVal_word)
        if self.value < 250:
            self.point_sound = pygame.mixer.Sound("point_get.wav")
            self.point_sound.play(0)
        elif self.value < 1000:
            self.point_sound = pygame.mixer.Sound("250point.wav")
            self.point_sound.play(0)
        elif self.value >= 1000:
            self.point_sound = pygame.mixer.Sound("1000point.wav")
            self.point_sound.play(0)
        self.font = pygame.font.Font(None, 100)
        self.image = self.font.render(self.text, True, (0,100+random.randint(-30, 60),0))
        self.move_count = 0




    def draw(self):
        if self.value >= 1000:
            self.image = self.font.render(self.text, True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if self.move_count < 25:
            self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        if self.move_count < 25:
            self.y -= 3
            self.move_count += 1