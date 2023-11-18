import pygame
import math
from Bullet import Bullet

class Enemy:
    def __init__(self, x, y, xspeed, yspeed, rad, attr=0) -> None:
        self.x=x
        self.y=y
        self.rad=rad
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.attr = attr
        self.timetick = 0
        self.duration1 = 120
        self.duration2 = 100
        self.duration3 = 110
        self.duration4 = 60
        self.path = []
        
    def update(self):
        self.path.append((self.x, self.y))
        if self.attr == 0:
            self.move_pattern1()
        if self.attr == 1: # 가속도
            self.move_pattern2()
        if self.attr == 3:
            self.move_pattern3()
        if self.attr == 4:
            self.move_pattern4()
        if self.attr == 5:
            self.move_pattern5()
        if self.attr == 6:
            self.move_pattern6()

    def is_colliding_with_player(self, player):
        distance = math.sqrt((self.x - player.x)**2 + (self.x - player.y)**2)
        return distance < self.rad + player.rad
    
    def move_pattern1(self):
        self.x += self.xspeed
        self.y += self.yspeed
        
    def move_pattern2(self):
        self.yspeed += 0.05
        self.x += self.xspeed
        self.y += self.yspeed

    def move_pattern3(self): #일정거리 이동 후 정지
        self.timetick += 1

        if self.timetick <= self.duration1:
            self.y += self.yspeed
        else:
            self.yspeed = 0

    def move_pattern4(self): #일정거리 이동 후 정지
        self.timetick += 1

        if self.timetick <= self.duration2:
            self.y += self.yspeed
        else:
            self.yspeed = 0

    def move_pattern5(self): #일정거리 이동 후 정지
        self.timetick += 1

        if self.timetick <= self.duration3:
            self.y += self.yspeed
        else:
            self.yspeed = 0

    def move_pattern6(self): #일정거리 이동 후 정지
        self.timetick += 1

        if self.timetick <= self.duration4:
            self.y += self.yspeed
        else:
            self.yspeed = 0
    
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
        new.append(Bullet(self.x, self.y, 5, 5, 20, attr=3))
        return bulletList

    def pattern4(self, bulletList):
        new = bulletList
        new.append(Bullet(self.x, self.y, 0, 5, 10, attr=4))
        return bulletList

    def pattern5(self, bulletList):
        new = bulletList
        new.append(Bullet(self.x, self.y, 0, 5, 10, attr=5))
        return bulletList