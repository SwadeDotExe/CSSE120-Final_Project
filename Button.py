import pygame
import sys
import Score

class Button:
    def __init__(self, screen, x, y, cost):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 150
        self.height = 75
        self.cost = cost
        self.cost_word = cost
        self.presscount = 0
        self.clicked = False
        self.green = 0
        self.im = pygame.image.load("BlueButton.png")
        self.imGreen = pygame.image.load("GreenButton.png")
        self.im = pygame.transform.scale(self.im,(self.width,self.height))
        self.imGreen = pygame.transform.scale(self.imGreen, (self.width, self.height))
        self.sound = pygame.mixer.Sound("Money.wav")

    def num_to_word(self):
        if self.cost == 0:
            self.cost_word = "Max"
        elif self.cost < 10000:
            self.cost_word = str(round(self.cost))
        elif self.cost < 1000000:
            self.cost_word = str(round(self.cost / 1000, 2)) + "K"
        elif self.cost < 1000000000:
            self.cost_word = str(round(self.cost / 1000000, 2)) + "M"
        elif self.cost < 1000000000000:
            self.cost_word = str(round(self.cost / 1000000000, 2)) + "B"
        elif self.cost < 1000000000000000:
            self.cost_word = str(round(self.cost / 1000000000000, 2)) + "T"
        elif self.cost < 1000000000000000000:
            self.cost_word = str(round(self.cost / 1000000000000000, 2)) + "Q"
        elif self.cost < 10000000000000000000000000000000:
            self.cost_word = "Bruh"
        return self.cost_word

    def render(self):
        font = pygame.font.Font(None, 60)
        font_img = font.render(self.num_to_word(), True, (255, 255, 255))
        q = 0
        while font_img.get_width() > self.width - 10:
            font = pygame.font.Font(None, 60 - q)
            font_img = font.render(self.num_to_word(), True, (255, 255, 255))
            q = q + 1
        return font_img

    def draw(self):
        if not self.green == 0:
             # pygame.draw.rect(self.screen, (0, 200, 0), (self.x, self.y, self.width, self.height))
            self.screen.blit(self.imGreen,(self.x,self.y))
            self.green -= 1
        else:
            # pygame.draw.rect(self.screen, (200, 0, 0), (self.x, self.y, self.width, self.height))
            self.screen.blit(self.im, (self.x, self.y))
            cost_image = self.render()
            self.screen.blit(cost_image, (self.x + ((self.width - cost_image.get_width()) / 2),
                                          self.y + (self.height - cost_image.get_height()) / 2))

    def is_clicked(self, clickpos):
        hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        if hitbox.collidepoint(clickpos):
            self.clicked = True

    def activate(self, scoreboard):
        self.clicked = False
        self.presscount += 1
        if not self.cost == 0:
            if self.cost <= scoreboard.score:
                # do what it needs to do
                scoreboard.score -= self.cost
                self.green = 10
                self.sound.play()
                return True
        else:
            return False



# def main():
#     pygame.init()
#     clock = pygame.time.Clock()
#     pygame.display.set_caption("button test")
#     screen = pygame.display.set_mode((500, 500))
#     button = Button(screen, 100, 100, 500)
#     scoreboard = Score.Scoreboard(screen)
#
#     while True:
#         clock.tick(60)
#         for event in pygame.event.get():
#             press = pygame.key.get_pressed()
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONUP:
#                 click_pos = event.pos
#                 button.is_clicked(click_pos)
#             if press[pygame.K_LEFT]:
#                 scoreboard.givemoney()
#                 button.cost = button.cost * 2.1035
#
#         screen.fill((0, 0, 0))
#
#         if button.clicked:
#             button.activate(scoreboard)
#         scoreboard.draw()
#         button.draw()
#         pygame.display.update()
#
# main()