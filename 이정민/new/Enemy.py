import pygame
from Bullet import Bullet

class Enemy:
    def __init__(self, x, y, xspeed, yspeed, rad, attr=0) -> None:
        self.x=x
        self.y=y
        self.rad=rad
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.attr = attr
        
    def update(self):
        if self.attr == 0:
            self.move_pattern1()
        if self.attr == 1: # 가속도
            self.move_pattern2()
    
    def move_pattern1(self):
        self.x += self.xspeed
        self.y += self.yspeed
        
    def move_pattern2(self):
        self.yspeed += 0.05
        self.x += self.xspeed
        self.y += self.yspeed
    
    def pattern1(self, bulletList):
        new = bulletList
        new.append(Bullet(self.x, self.y, 0, 5, 20, attr=1))
        return bulletList
    
    def pattern2(self, bulletList):
        new = bulletList
        new.append(Bullet(self.x, self.y, 0, 5, 20, attr=2))
        return bulletList
    
    def pattern3(self, bulletList):
        new = bulletList
        new.append(Bullet(self.x, self.y, 5, 5, 20, attr=4))
        return bulletList
    