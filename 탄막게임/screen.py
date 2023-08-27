import pygame

class screen:
    def __init__(self, width, height, caption):
        self.width = 600
        self.height = 800
        self.screen = pygame.display.set_caption((width, height))
    def fill(self, color):
        self.screen.fill(color)
    def flip(self):
            pygame.display.flip()

