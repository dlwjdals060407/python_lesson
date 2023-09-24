import pygame
import math
import random
from modules.Enemy import EnemyBullet

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
        self.shoot_interval = 100
        self.screen_height = screen_height
        self.min_y = 50
        self.max_y = 150
        self.min_x = 0
        self.max_x = 400
        self.move_direction_x = random.choice([-1, 1])
        self.move_direction_y = random.choice([-1, 1])
        self.color = (0, 0, 0)
        self.health = 50
        self.pattern_active = False
        self.pattern_timer = 0
        self.pattern_interval = 10
        self.bullet_list = []

        self.pattern = BossPattern(self)  # 보스 객체에 대한 패턴 객체 생성

    def move(self):
        if self.active:
            self.x += self.speed * self.move_direction_x
            self.y += self.speed * self.move_direction_y

            self.x = max(self.min_x, min(self.x, self.max_x))
            self.y = max(self.min_y, min(self.y, self.max_y))

            if self.x <= self.min_x or self.x >= self.max_x:
                self.move_direction_x *= -1
            elif self.y <= self.min_y or self.y >= self.max_y:
                self.move_direction_y *= -1

    def activate_pattern(self):
        self.pattern.activate()

    def deactivate_pattern(self):
        self.pattern.deactivate()

    def update(self, player_x, player_y):
        self.shoot_timer += 1
        self.pattern_timer += 1
        boss_bullet = []

        if self.shoot_timer >= self.shoot_interval:
            player_dx = player_x - self.x
            player_dy = player_y - self.y
            angle = math.atan2(player_dy, player_dx)

            bullet_x = self.x + self.width // 2 - 1
            bullet_y = self.y + self.height
            boss_bullet.append(EnemyBullet(bullet_x, bullet_y, angle, self.screen_height))

            self.shoot_timer = 0

        for bullet in boss_bullet:
            bullet.draw(self.screen)

        if self.pattern_active:
            if self.pattern_timer >= self.pattern_interval:
                self.pattern.execute_pattern(player_x, player_y)
                self.pattern_timer = 0

        if self.shoot_timer >= self.shoot_interval:
            player_dx = player_x - self.x
            player_dy = player_y - self.y
            angle = math.atan2(player_dy, player_dx)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def check_collision(self, bullet):
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        boss_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(boss_rect)
    
    def draw_pattern(self):
        for bullet in self.bullet_list:
            bullet.update()
            bullet.draw(self.screen)
    
    def move_bullets(self):
        for bullet in  self.bullet_list:
            bullet.update()
            bullet.draw(self.screen)

class BossPattern:
    
    def __init__(self, boss):
      self.boss = boss
      self.pattern_active = False
      self.pattern_timer = 0
      self.pattern_interval = 10
      self.bullet_angle = 0

    def activate(self):
        self.pattern_active = True
        self.pattern_timer = 0
        self.bullet_angle = 0
    
    def deactivate(self):
        self.pattern_active = False

    def update(self, player_x, player_y):
        self.pattern_timer += 1

        if self.pattern_active and self.pattern_timer >= self.pattern_interval:
            self.excute_pattern(player_x, player_y)
            self.pattern_timer = 0

    def excute_pattern(self, player_x, player_y):
        self.boss.bullet_list = []
        bullets_to_remove = []
        bullet_speed = 5
        for i in range(0, 360, 12):
            angle_radians = math.radians(i)

            bullet_x = self.boss.x + self.boss.width // 2 - 1
            bullet_y = self.boss.y + self.boss.height
            bullet = EnemyBullet(bullet_x ,bullet_y, angle_radians, self.boss.screen_height)
            bullet.speed = bullet_speed
            self.boss.bullet_list.append(bullet)        
    
        if bullet.is_offscreen():
            bullets_to_remove.append(bullet)

            for bullet in bullets_to_remove:
                self.boss.bullet_list.remove(bullet)

    def update(self):
        self.x += self.speed * math.cos(self.bullet_angle)
        self.y += self.speed * math.sin(self.bullet_angle)