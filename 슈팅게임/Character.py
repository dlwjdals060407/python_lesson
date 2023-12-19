import pygame
import time

class Character:
    def __init__(self, x, y, rad) -> None:
        self.x = x
        self.y = y
        self.rad = rad
        self.speed = 5
        
    def move(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] and self.x - self.speed >= 0:
            self.x -= self.speed  # 왼쪽으로 이동 (화면 왼쪽 경계 확인)
        if keys[pygame.K_RIGHT] and self.x + self.rad * 2 + self.speed <= screen_width:
            self.x += self.speed  # 오른쪽으로 이동 (화면 오른쪽 경계 확인)
        if keys[pygame.K_UP] and self.y - self.speed >= 0:
            self.y -= self.speed  # 위로 이동 (화면 위쪽 경계 확인)
        if keys[pygame.K_DOWN] and self.y + self.rad * 2 + self.speed <= screen_height:
            self.y += self.speed  # 아래로 이동 (화면 아래쪽 경계 확인)
