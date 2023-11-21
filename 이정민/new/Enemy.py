import pygame
import math
import random
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
        if self.attr == 7:
            self.boss_move_pattern1()
        if self.attr == 8:
            self.stop()

    def is_colliding_with_player(self, player):
        distance = math.sqrt((self.x - player.x)**2 + (self.x - player.y)**2)
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

    def boss_move_pattern1(self):
        self.timetick += 1

        self.x += self.xspeed
        self.y += self.yspeed

        if self.timetick <= 120:
            self.yspeed = 0.5

            self.x += self.xspeed
            self.y += self.yspeed
        
        if self.timetick <= 180:
            self.yspeed = 0.25

            self.x += self.xspeed
            self.y += self.yspeed
        
        if self.timetick <= 210:
            self.yspeed = 0

            self.x += self.xspeed
            self.y += self.yspeed

        # if  300 <= self.timetick <= 1000:
        #     new_x = random.randint(50, 550)  
        #     new_y = random.randint(50, 950)  

        #     delta_x = new_x - self.x
        #     delta_y = new_y - self.y
        #     distance = math.sqrt(delta_x**2 + delta_y**2)

        #     self.xspeed = (delta_x / distance) * 3 
        #     self.yspeed = (delta_y / distance) * 3 
        #     self.x += self.xspeed
        #     self.y += self.yspeed
    
    def stop(self):
        self.x = 0
        self.y = 0
        
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

    def boss_pattern_1(self, bulletList):
        new = bulletList
        if self.timetick % 20 == 0: 
            for angle in range(0, 360, 10):
                seta = math.radians(angle)
                new.append(Bullet(self.x, self.y, math.cos(seta) * 2, math.sin(seta) * 2, 7, attr=6))
        return bulletList
    