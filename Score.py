import pygame


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 100
        self.font = pygame.font.Font(None, 30)
        self.cost_word = ""

    def draw(self):
        score_string = "Score: " + self.num_to_word()
        score_image = self.font.render(score_string, True, (255, 255, 255))
        self.screen.blit(score_image, (5, 5))

    def givemoney(self):
        self.score += 100

    def num_to_word(self):
        if self.score < 10000:
            self.cost_word = str(round(self.score))
        elif self.score < 1000000:
            self.cost_word = str(round(self.score / 1000, 2)) + "K"
        elif self.score < 1000000000:
            self.cost_word = str(round(self.score / 1000000, 2)) + "M"
        elif self.score < 1000000000000:
            self.cost_word = str(round(self.score / 1000000000, 2)) + "B"
        elif self.score < 1000000000000000:
            self.cost_word = str(round(self.score / 1000000000000, 2)) + "T"
        elif self.score < 1000000000000000000:
            self.cost_word = str(round(self.score / 1000000000000000, 2)) + "Q"
        elif self.score < 10000000000000000000000000000000:
            self.cost_word = "Bruh"
        return self.cost_word
