import random
import pygame

class Boss:
  def __init__(self, x, y, screen, screen_height):
    self.width = 200
    self.height = 200
    self.x = x
    self.y = 0
    self.speed = 3
    self.screen = screen
    self.active = True
    self.shoot_timer = 0
    self.shoot_interval = 50
    self.screen_height = screen_height
    self.min_y = 100
    self.max_y = 150
    self.min_x = 0
    self.max_x = 400
    self.move_direction_x = random.choice([-1, 1])
    self.move_direction_y = random.choice([-1, 1])
    self.color = (0,0,0)
    self.health = 50

  def move(self):
    if self.active:
        self.x += self.speed * self.move_direction_x

        self.x = max(self.min_x, min(self.x, self.max_x))
        self.y = max(self.min_y, min(self.y, self.max_y))

        if self.x <= self.min_x or self.x >= self.max_x:
            self.move_direction_x *= -1
        elif self.y <= self.min_y or self.y >= self.max_y:
            self.move_direction_y *= -1
  
  def pattern_1(self):
    pass
  
  def update(self):
    self.move()
    self.attack()
  
  def draw(self):
    if self.active:
      pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

  def check_collision(self, bullet):
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        Boss_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(Boss_rect)
  

     