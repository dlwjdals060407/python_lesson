import math

class Laser:
    def __init__(self, X, Y, width, height, xspeed, yspeed, lifespan):
        self.posX = X
        self.posY = Y
        self.width = width
        self.height = height
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.lifespan = lifespan  # 레이저 수명

    def update(self):
        self.posX += self.xspeed
        self.posY += self.yspeed
        self.lifespan -= 1  # 수명 감소
