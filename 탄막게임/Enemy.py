import pygame

class Enemy:
    def __init__(self, x, y, screen) -> None:
        self.w = 25
        self.h = 25
        self.x = x
        self.y = y
        self.speed = 10

        self.screen = screen
    
    """ def update(self):
        self.x += self.speed """

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, self.w, self.h))

    def check_coliide(self, other_rect):
        return pygame.Rect(self.x, self.y ,self.w, self.y, ).colliderect(other_rect)

    