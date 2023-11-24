import math
from Character import Character

class Bullet:
    def __init__(self, x, y, xspeed, yspeed, rad, attr=0) -> None:
        self.x=x
        self.y=y
        self.rad=rad
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.attr = attr
        self.timeTick = 0
        self.angle = 0
        
    def update(self, bulletList, player):
        self.x = min(self.x, 600)
        self.y = min(self.y, 1000)
        self.x = max(self.x, 0)
        self.y = max(self.y, 0)
        if self.attr == 0:
            self.move_default_pattern()
        if self.attr == 1:
            bulletList = self.move_pattern1(bulletList)
        if self.attr == 2:
            bulletList = self.move_pattern2(bulletList)
        if self.attr == 3:
            self.move_pattern3(player)
        if self.attr == 4:
            bulletList = self.move_pattern4(bulletList)
        if self.attr == 5:
            bulletList = self.move_pattern5(bulletList)
        if self.attr == 6:
            self.boss_move_pattern1(player)
        if self.attr == 7:
             self.boss_move_pattern2()
        if self.attr == 8:
             self.boss_move_pattern2()
        return bulletList
    
    def is_colliding_with_player(self, player):
        distance = math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        return distance < self.rad + player.rad

    # 직선
    def move_default_pattern(self, x=0, y=0):
        self.x += self.xspeed
        self.y += self.yspeed
    
    def move_pattern1(self, bulletList):
        self.timeTick += 1
        self.x += self.xspeed
        self.y += self.yspeed
        
        newList = bulletList
        if self.timeTick >= 120:
            angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
            for angle in angles:
                    seta = math.radians(angle)
                    bullet = Bullet(self.x, self.y, math.cos(seta)*3, math.sin(seta)*3, 6, attr=0)
                    newList.append(bullet)
            bulletList.remove(self) 
        return newList
    
    def move_pattern2(self, bulletList):
        self.timeTick += 1
        self.x += self.xspeed
        self.y += self.yspeed
        
        newList = bulletList
        if self.timeTick >= 120:
            angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
            for angle in angles:
                    seta = math.radians(angle)
                    newList.append(Bullet(self.x, self.y, math.cos(seta)*3, math.sin(seta)*3, 6, attr=3))
            bulletList.remove(self) 
        return newList
    
    def move_pattern3(self, player):
        self.timeTick += 1
        if self.timeTick == 120:
            self.xspeed = (player.x-self.x)//100
            self.yspeed = (player.y-self.y)//100
        
        self.x += self.xspeed
        self.y += self.yspeed
        
    def move_pattern4(self, bulletList):
        self.timeTick += 1
        self.x += self.xspeed
        self.y += self.yspeed
        
        newList = bulletList
        if self.timeTick >= 80:
            angles = [0, 30, 60, 90, 120, 150, 180]
            for angle in angles:
                    seta = math.radians(angle)
                    bullet = Bullet(self.x, self.y, math.cos(seta)*3, math.sin(seta)*3, 6, attr=0)
                    newList.append(bullet)
            bulletList.remove(self) 
        return newList

    def move_pattern5(self, bulletList):
        self.timeTick += 1
        self.x += self.xspeed
        self.y += self.yspeed
        
        newList = bulletList
        if self.timeTick >= 90:
            angles = [0, 30, 60, 90, 120, 150, 180]
            for angle in angles:
                    seta = math.radians(angle)
                    bullet = Bullet(self.x, self.y, math.cos(seta)*2, math.sin(seta)*2, 6, attr=0)
                    newList.append(bullet)
            bulletList.remove(self) 
        return newList
    
    def boss_move_pattern1(self, player):
        self.timeTick += 1
        if self.timeTick == 80:
            self.xspeed = (player.x-self.x)//25
            self.yspeed = (player.y-self.y)//25
        
        self.x += self.xspeed
        self.y += self.yspeed

    def boss_move_pattern2(self, bulletList):
        self.timeTick += 1
        self.x += self.xspeed
        self.y += self.yspeed
        
        newList = bulletList
        if self.timeTick >= 90:
            angles = [0, 30, 60, 90, 120, 150, 180]
            for angle in angles:
                    seta = math.radians(angle)
                    bullet = Bullet(self.x, self.y, math.cos(seta)*100, math.sin(seta)*100, 6, attr=8)
                    newList.append(bullet)
            bulletList.remove(self) 
        return newList
    def boss_move_pattern3(self):
        pass