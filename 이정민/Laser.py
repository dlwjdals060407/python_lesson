import math

class Laser:
    def __init__(self, X, Y, width, height, duration):
        self.posX = X
        self.posY = Y
        self.width = width
        self.height = height
        self.duration = duration

    def update(self):
        self.duration -= 1

    def is_colliding_with_player(self, player):
        distance = math.sqrt((self.posX - player.posX)**2 + (self.posY - player.posY)**2)
        return distance < player.rad