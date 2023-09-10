import pygame
import sys
import random
import math 

class Player:
    def __init__(self, x, y, screen_width, screen_height):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.speed = 5
        self.health = 3
        self.screen_width =screen_width
        self.screen_height = screen_height

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.x = max(0, min(self.x, self.screen_width - self.width))
        self.y = max(0, min(self.y, self.screen_height - self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
    
    def check_collision(self, bullet):
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        return player_rect.colliderect(bullet_rect)