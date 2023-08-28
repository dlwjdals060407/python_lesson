import pygame
import sys
import random

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

class Enemy:
    def __init__(self, x, y, screen):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.speed = 3
        self.screen = screen
        self.active = True

    def move(self):
        if self.active:
            self.y += self.speed
            if self.y > self.screen.get_height():
                self.active = False

    def check_coliide(self, bullet):
        bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(enemy_rect)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, red, (self.x, self.y, self.width, self.height))

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("탄막게임")

# 플레이어 초기 위치 및 속도
player_width = 25
player_height = 25
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 5

# 총알 초기 설정
bullet_width = 2
bullet_height = 12
bullet_color = (255, 0, 0)
bullet_speed = 10
bullets = []

# 메인 루프
running = True
enemyList = [Enemy(50, 0, screen)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    # 플레이어 움직임 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 플레이어가 화면을 벗어나지 않도록 제한
    player_x = max(0, min(player_x, screen_width - player_width))
    player_y = max(0, min(player_y, screen_height - player_height))

    # 총알 이동 및 화면을 벗어나면 제거
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
    
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_width, bullet_height))
        for enemy in enemyList:
            if enemy.check_coliide(bullet):
                bullets.remove(bullet)
                enemy.x = random.randint(0, screen_width - enemy.width)
                enemy.y = 0

    # 화면 업데이트
    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

    for enemy in enemyList:
        enemy.move()
        enemy.draw()

    pygame.display.flip()
    # 초당 프레임 설정
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
sys.exit()


