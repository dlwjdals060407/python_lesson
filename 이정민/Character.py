import pygame
import math
from Bullet import Bullet

class Character:
    def __init__(self, X, Y, xspeed, yspeed, rad, is_boss = False, spawn_frame=0) -> None:
        self.posX = X
        self.posY = Y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.rad = rad
        
    def update(self):
        self.posX += self.xspeed
        self.posY += self.yspeed    
        
    def move(self, keys):
        self.xspeed = 0
        self.yspeed = 0

        if keys[pygame.K_LEFT]:
            self.xspeed = -3  # 왼쪽으로 이동
        if keys[pygame.K_RIGHT]:
            self.xspeed = 3  # 오른쪽으로 이동
        if keys[pygame.K_UP]:
            self.yspeed = -3  # 위로 이동
        if keys[pygame.K_DOWN]:
            self.yspeed = 3  # 아래로 이동
    
    def is_colliding_with_player(self, player):
        distance = math.sqrt((self.posX - player.posX)**2 + (self.posY - player.posY)**2)
        return distance < self.rad + player.rad

class Boss(Character):
    def __init__(self, X, Y, xspeed, yspeed, rad) -> None:
        super().__init__(X, Y, xspeed, yspeed, rad)

