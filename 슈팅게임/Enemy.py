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
        
    def update(self,bl):
        self.path.append((self.x, self.y))
        self.x = min(self.x, 600)
        self.y = min(self.y, 1000)
        self.x = max(self.x, 0)
        self.y = max(self.y, 0)
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
        if self.attr == 9:
            self.boss_pattern_2()
        if self.attr == 10:
            self.boss_pattern_3()
        if self.attr == 11:
            self.move_around_boss()
        if self.attr == 12:
            self.move_around_boss_2()
        if self.attr == 13:
            bl = self.boss_pattern_4(bl)
        return bl


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

        if self.timetick == 400:
            self.xspeed = random.randint(-1,1)
            self.yspeed = random.randint(-1,1)

            self.x += self.xspeed
            self.y += self.yspeed
        
        if self.timetick == 440:
            self.xspeed = (self.xspeed)//2
            self.yspeed = (self.yspeed)//2

            self.x += self.xspeed
            self.y += self.yspeed
            
        if self.timetick == 450:
            self.xspeed = (self.xspeed)//2
            self.yspeed = (self.yspeed)//2

            self.x += self.xspeed
            self.y += self.yspeed

        if self.timetick == 455:
            self.xspeed = 0
            self.yspeed = 0

            self.x += self.xspeed
            self.y += self.yspeed

        if self.timetick == 900:
            self.x = 300
            self.y = 100
    
        if self.timetick == 2400:
            self.x = 300
            self.y = 300
        
        if self.timetick == 3350:
            self.x = 300
            self.y = 100

    def stop(self):
        self.x = 0
        self.y = 0
        
        self.x += self.xspeed
        self.y += self.yspeed

    def pattern1(self, bulletList):
        new = bulletList
        new.append(Bullet(self.x, self.y, 0, 5, 10, attr=1))
        return bulletList
    
    def pattern2(self, bulletList):
        new = bulletList
        new.append(Bullet(self.x, self.y, 0, 5, 10, attr=2))
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
    
    def boss_pattern_2(self):
        self.timetick +=1 
        if self.timetick <= 200:
            self.xspeed = 1
            self.yspeed = 0
            self.x += self.xspeed
            self.y += self.yspeed
        else:
            self.xspeed = 0
            self.yspeed = 2
            self.x += self.xspeed
            self.y += self.yspeed
    
    def boss_pattern_3(self):
        self.timetick +=1 
        if self.timetick <= 200:
            self.xspeed = -1
            self.yspeed = 0
            self.x += self.xspeed
            self.y += self.yspeed
        else:
            self.xspeed = 0
            self.yspeed = 2
            self.x += self.xspeed
            self.y += self.yspeed

    def move_around_boss(self):
        boss_x = 300  
        boss_y = 300  
        radius = 120  

        angle = math.radians(self.timetick)
        self.x = boss_x + int(radius * math.cos(angle))
        self.y = boss_y + int(radius * math.sin(angle))
        
        self.timetick += 2

    def move_around_boss_2(self):
        boss_x = 300  
        boss_y = 300  
        radius = 120  

        angle = math.radians(self.timetick)
        self.x = boss_x + int(radius * math.cos(angle))
        self.y = boss_y + int(radius * math.sin(angle))
        
        self.timetick -= 2
    
    # def boss_pattern_3(self, bulletList):
    #     new = bulletList
    #     if self.timetick % 20 == 0: 
    #         for angle in range(0, 360, 10):
    #             seta = math.radians(angle)
    #             new.append(Bullet(300, 300, math.cos(seta) * 2, math.sin(seta) * 2, 7, attr=7))
    #     return bulletList

    def boss_pattern_4(self, bulletList):
        self.timetick += 1
        new = bulletList
        if self.timetick % 20 == 0: 
            for angle in range(0, 360, 10):
                seta = math.radians(angle)
                new.append(Bullet(300, 300, math.cos(seta) * 2, math.sin(seta) * 2, 7, attr=8))
        return bulletList 