import pygame
import sys
import random

pygame.init()


image25 = pygame.image.load("25.jpg")
image40 = pygame.image.load("40.jpg")
image50 = pygame.image.load("50.jpg")
image75 = pygame.image.load("75.jpg")
image80 = pygame.image.load("80.jpg")
image150 = pygame.image.load("150.jpg")
image250 = pygame.image.load("250.jpg")
image1000 = pygame.image.load("1000.jpg")



class Rect(object):

    def __init__(self, screen, random, x, y, c, luck):
        self.screen = screen
        rand = random
        self.x = x
        self.y = y
        self.scale = 1
        self.c = c
        if random < 25-luck:
            self.value = 25
            self.image = image25
        if random >= 25-luck and random < 45-luck:
            self.value = 40
            self.image = image40
        if random >= 45-luck and random < 65-luck:
            self.value = 50
            self.image = image50
        if random >= 65-luck and random < 75-luck:
            self.value = 75
            self.image = image75
        if random >= 75-luck and random < 85-luck:
            self.value = 80
            self.image = image80
        if random >= 85-luck and random < 92.5-luck:
            self.value = 150
            self.image = image150
        if random >= 92.5-luck and random < 98.5-luck:
            self.value = 250
            self.image = image250
        if random >= 98.5-luck:
            self.value = 1000
            self.image = image1000


    def draw(self):
        #g = pygame.draw.rect(self.screen,(0,0,0),(self.x,self.y-2*self.scale*.5,126,2*self.scale))
        self.image = pygame.transform.scale(self.image,(126,70))
        self.screen.blit(self.image,(self.x,self.y-130))


    def move(self):
        #self.y += ((.05*self.scale)+5)
        self.y += 7*self.c
        self.scale = (350 - ((self.y-350)**2)**.5)*.15