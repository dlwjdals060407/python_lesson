import pygame
import sys
import random
import math 

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 2
        self.height = 12
        self.color = (0, 255, 0)
        self.speed = 10

    def move(self):
        self.y -= self.speed

    def is_offscreen(self):
        return self.y < 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))