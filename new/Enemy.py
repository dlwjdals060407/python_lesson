import pygame
import math
from Bullet import Bullet

class Enemy:
    def __init__(self, x, y, xspeed, yspeed, rad, health, attr=0) -> None:
        self.x=x
        self.y=y
        self.rad=rad
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.health = health
        self.attr = attr
        self.timetick = 0
        
    def update(self):
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
        if self.attr == 7:
            self.move_pattern7()
        if self.attr == 8:
            self.boss_move_pattern1()

    def is_colliding_with_player(self, player):
        distance = math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        return distance < self.rad + player.rad
    
    def is_colliding_with_bullet(self, bullet):
        distance = math.sqrt((self.x - bullet.x)**2 + (self.y - bullet.y)**2)
        if distance < self.rad + bullet.rad:
            self.health -= 1
            return True
        return False
    
    def move_pattern1(self):
        self.x += self.xspeed
        self.y += self.yspeed
        
    def move_pattern2(self):
        self.yspeed += 0.05
        self.x += self.xspeed
        self.y += self.yspeed

    def move_pattern3(self): #일정거리 이동 후 정지
        self.timetick += 1

        if self.timetick <= 120:
            self.y += self.yspeed
        else:
            self.yspeed = 0

    def move_pattern4(self): #일정거리 이동 후 정지
        self.timetick += 1

        if self.timetick <= 100:
            self.y += self.yspeed
        else:
            self.yspeed = 0

    def move_pattern5(self): #일정거리 이동 후 정지
        self.timetick += 1

        if self.timetick <= 110:
            self.y += self.yspeed
        else:
            self.yspeed = 0

    def move_pattern6(self): #일정거리 이동 후 정지
        self.timetick += 1

        if self.timetick <= 60:
            self.y += self.yspeed
        else:
            self.yspeed = 0

    def move_pattern7(self): #일정거리 이동 후 정지
        self.timetick += 1

        self.yspeed = 0
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
    
    def pattern6(self, bulletList):
        new = bulletList
        angles = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 278, 290, 312, 324, 336, 348, 360]
        for angle in angles:
            seta = math.radians(angle)
            new.append(Bullet(self.x, self.y, math.cos(seta)*3, math.sin(seta)*3, 6, attr=6))
        # new.append(Bullet(self.x, self.y, 0, 5, 10, attr=5))
        return bulletList
    
    def boss_move_pattern1(self):
        self.timetick += 1
        self.xspeed = 0

        if self.timetick <= 60:
            self.x += self.xspeed
            self.y += self.yspeed
        if 61 <= self.timetick <= 80:
            self.yspeed = 0.7
            self.x += self.xspeed
            self.y += self.yspeed
        if 81 <= self.timetick <= 100:
            self.yspeed = 0.4
            self.x += self.xspeed
            self.y += self.yspeed
        if 101 <= self.timetick <= 120:
            self.yspeed = 0.1
            self.x += self.xspeed
            self.y += self.yspeed
        if self.timetick >= 121:
            self.yspeed = 0
            self.x += self.xspeed
            self.y += self.yspeed