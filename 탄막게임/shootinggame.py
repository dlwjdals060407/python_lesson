import pygame
import sys
import random
import math  # math 모듈 추가

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class EnemyBullet:
    def __init__(self, x, y, angle):  # 각도(angle) 매개변수 추가
        self.x = x
        self.y = y
        self.width = 24
        self.height = 24
        self.color = (255, 0, 0)
        self.speed = 13
        self.angle = angle  # 발사 각도 저장

    def move(self):
        # 각도와 속도를 사용하여 총알 이동
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def is_offscreen(self):
        return self.y > screen_height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Enemy:
    def __init__(self, x, y, screen):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.speed = 3
        self.screen = screen
        self.active = True
        self.bullets = []
        self.shoot_timer = 0
        self.shoot_interval = 50

    def move(self):
        if self.active:
            self.y += self.speed
            if self.y > self.screen.get_height():
                self.active = False

    def check_collision(self, bullet):
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(enemy_rect)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, red, (self.x, self.y, self.width, self.height))

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.move()

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
            if bullet.is_offscreen():
                self.bullets.remove(bullet)

    def update(self, player_x, player_y):  # 플레이어 위치를 받는 매개변수 추가
        self.shoot_timer += 1

        if self.shoot_timer >= self.shoot_interval:
            player_dx = player_x - self.x
            player_dy = player_y - self.y

            # 발사 각도 계산 (라디안 단위)
            angle = math.atan2(player_dy, player_dx)

            # 총알 생성 및 발사
            bullet_x = self.x + self.width // 2 - 1
            bullet_y = self.y + self.height
            self.bullets.append(EnemyBullet(bullet_x, bullet_y, angle))
            self.shoot_timer = 0

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 2
        self.height = 12
        self.color = (0, 255, 0)
        self.speed = 10

    def move(self):
        self.y -= self.speed

    def is_offscreen(self):
        return self.y < 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.speed = 5
        self.health = 3

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.x = max(0, min(self.x, screen_width - self.width))
        self.y = max(0, min(self.y, screen_height - self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
    
    def check_collision(self, bullet):
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        return player_rect.colliderect(bullet_rect)

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("탄막게임")

bullets = []

# 메인 루프
running = True
enemyList = [Enemy(50, 0, screen)]
player = Player(300, 700)
enemy_bullet_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x + player.width // 2 - 1, player.y))

    keys = pygame.key.get_pressed()
    player.move(keys)

    if random.randint(1, 100) == 90:
        x = random.randint(0, screen_width - 50)
        enemyList.append(Enemy(x, 0, screen))

    for enemy in enemyList:
        enemy.update(player.x, player.y)

    enemy_bullet_timer += 1

    if enemy_bullet_timer >= 50:
        for enemy in enemyList:
            if enemy.active:
                enemy.update(player.x, player.y)
        enemy_bullet_timer = 0

    bullets = [bullet for bullet in bullets if not bullet.is_offscreen()]

    for enemy in enemyList:
        for bullet in bullets:
            if enemy.check_collision(bullet):
                enemyList.remove(enemy)
                bullets.remove(bullet)
                player.health -= 1
                if player.health == 0:
                    running = False

    for enemy in enemyList:
        if enemy.active:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
            if enemy.check_collision(player_rect):
                player.health -= 1
                enemyList.remove(enemy)
                if player.health == 0:
                    running = False

    for enemy in enemyList:
        for bullet in enemy.bullets:
            if player.check_collision(bullet):
                enemy.bullets.remove(bullet)
                player.health -= 1  # 플레이어 체력 감소
                if player.health == 0:
                    running = False

    screen.fill(white)

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)

    for enemy in enemyList:
        enemy.move()
        enemy.draw()
        enemy.move_bullets()
        enemy.draw_bullets(screen)

    font = pygame.font.Font(None, 30)
    health_text = font.render(f'Health: {player.health}', True, red)
    screen.blit(health_text, (10, 700))

    player.draw(screen)
    pygame.display.update()
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
sys.exit()

