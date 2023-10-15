import math

class Bullet:
    def __init__(self, X, Y, xspeed, yspeed, rad) -> None:
        self.posX = X
        self.posY = Y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.rad = rad
        
    def update(self):
        self.posX += self.xspeed
        self.posY += self.yspeed
        
    def is_colliding_with_player(self, player):
        distance = math.sqrt((self.posX - player.posX)**2 + (self.posY - player.posY)**2)
        return distance < self.rad + player.rad
    
    def is_colliding_with_enemy(self, enemy):
        distance = math.sqrt((self.posX - enemy.posX)**2 + (self.posY - enemy.posY)**2)
        return distance < self.rad + enemy.rad
    
    def is_colliding_with_boss(self, boss):
        distance = math.sqrt((self.posX - boss.posX) ** 2 + (self.posY - boss.posY) ** 2)
        return distance < self.rad + boss.rad
    