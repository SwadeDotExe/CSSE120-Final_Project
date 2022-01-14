import pygame
import sys
import Score
import random
import PopUp
import Score

class Bass:
    def __init__(self, screen, multiplier):
        self.screen = screen
        self.multiplier = multiplier
        self.width = 80
        self.height = 40
        self.speed = 10 + random.randint(-3,5)
        self.x = -50
        self.y = random.randint(20,630)
        self.alive = True
        f = random.randint(1,6)
        if f == 1 or f == 2:
            self.image = pygame.image.load("BaseBass.png")
        if f == 3:
            self.image = pygame.image.load("Blue_Bass.png")
        if f == 4:
            self.image = pygame.image.load("Tan_Bass.png")
        if f == 5:
            self.image = pygame.image.load("Red_Bass.png")
        if f == 6:
            self.image = pygame.image.load("Purple_Bass.png")
        self.image = pygame.transform.scale(self.image,(80,50))


    def drawAndMove(self):
        self.x += self.speed
        if self.alive == True:
            #pygame.draw.rect(self.screen, (0,255,0), (self.x,self.y,self.width,self.height))
            self.screen.blit(self.image,(self.x,self.y))
        else:
            self.pop.move()
            self.pop.draw()



    def is_clicked(self, clickpos, scoreboard):
        hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        if hitbox.collidepoint(clickpos) and self.alive == True:
            self.alive = False
            scoreboard.score += 250*self.multiplier
            self.pop = PopUp.PopUp(250, self.screen, self.multiplier)
            self.pop.x = self.x
            self.pop.y = self.y

