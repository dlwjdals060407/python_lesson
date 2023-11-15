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
        return bulletList
    
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
        
    def move_pattern4(self,bulletList):
        
        self.timeTick += 1
        angle_increase = 5
        num_bullets = 36
        if self.timeTick >= 90:
            for i in range(num_bullets):
                angle = math.radians(i * angle_increase)
                bulletList.append(Bullet(self.x, self.y, math.cos(angle) * 3, math.sin(angle) * 3, 6, attr=4))
        return bulletList
        