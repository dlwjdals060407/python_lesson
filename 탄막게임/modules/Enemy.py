import pygame
import math
import random

red = (255, 0, 0)

class Enemy:
    def __init__(self, x, y, screen, screen_height):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = 0
        self.speed = 3
        self.screen = screen
        self.active = True
        self.shoot_timer = 0
        self.shoot_interval = random.randint(100, 300)  # 랜덤한 발사 간격 설정
        self.screen_height = screen_height
        self.min_y = 100
        self.max_y = 300
        self.min_x = 50
        self.max_x = 550
        self.move_direction_x = random.choice([-1, 1])
        self.move_direction_y = random.choice([-1, 1])

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

    def check_collision(self, bullet):
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(enemy_rect)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, red, (self.x, self.y, self.width, self.height))

    def update(self, player_x, player_y):  # 플레이어 위치를 받는 매개변수 추가
        self.shoot_timer += 1
        return self.shoot_timer,self.shoot_interval,self.x,self.y,self.width,self.height
    def resetTimer(self):
        self.shoot_timer = 0

class EnemyBullet:
    def __init__(self, x, y, angle, screen_height):  # 각도 변수 추가
        self.x = x
        self.y = y
        self.width = 24
        self.height = 24
        self.color = (255, 0, 0)
        self.speed = 6
        self.angle = angle
        self.screen_height = screen_height

    def move(self):
        # 각도와 속도를 사용하여 총알 이동
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def is_offscreen(self):
        return self.y > self.screen_height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)