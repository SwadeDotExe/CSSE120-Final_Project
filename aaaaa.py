import pygame
import sys
import random


class Wheel:
    def __init__(self, screen, width, height):
        self.tiles = []
        self.screen = screen
        self.width = width
        self.height = height
        for k in range(5):
            centerx = screen.get_width() / 2
            centery = screen.get_height() / 2
            x1 = centerx - width / 2
            x2 = width
            y1 = centery - (height / 2) + (height * (k) / 5)
            y2 = height / 5
            color = (random.randint(0, 255), random.randint(0, 1), random.randint(0, 255))
            tile = Tile(screen, color, x1, y1, x2, y2)
            self.tiles.append(tile)

    def draw(self):
        for k in range(len(self.tiles)):
            self.tiles[k].draw()

    def spin(self, speed):
        for k in range(len(self.tiles)):
            self.tiles[k].move(k, self.width, self.height, speed)

    def start(self):
        pass


class Tile:
    def __init__(self, screen, color, x1, y1, x2, y2):
        self.screen = screen
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x1, self.y1, self.x2, self.y2))

    def move(self, k, width, height, speed):
        self.y1 -= 0.3 * k
        self.y2 = self.y2 - 0.1







def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('wheel test')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    screen.get_width()
    wheel = Wheel(screen, 100, 300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        wheel.draw()
        wheel.spin(10)
        pygame.display.update()


main()

