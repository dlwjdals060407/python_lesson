import pygame

class Character:
    def __init__(self, x, y, rad) -> None:
        self.x=x
        self.y=y
        self.rad=rad
        self.speed = 5
        
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed  # 왼쪽으로 이동
        if keys[pygame.K_RIGHT]:
            self.x += self.speed  # 오른쪽으로 이동
        if keys[pygame.K_UP]:
            self.y -= self.speed  # 위로 이동
        if keys[pygame.K_DOWN]:
            self.y += self.speed  # 아래로 이동