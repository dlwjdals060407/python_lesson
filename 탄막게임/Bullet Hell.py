import pygame
import sys
import random

from Enemy import Enemy

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("탄막게임")

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

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

# enemy_width = 25
# enemy_height = 25
# enemy_x = random.randint(0, screen_width - enemy_width)
# enemy_y = 0
# enemy_speed = 2
# 메인 루프
running = True
enemyList = [Enemy(50, 0, screen),]

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

    """ if bullet.colliderect(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)):
        bullets.remove(bullet) """
        
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_width, bullet_height))
        for enemy in enemyList:
            if enemy.check_coliide(bullet):
                bullets.remove(bullet)
                Enemy.x = random.randint(0, screen_width - enemy.width)
                Enemy.y = 0

    # 화면 업데이트
    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    # pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))

    #for enemy in enemyList:
    Enemy.update()
    Enemy.draw()

                

    pygame.display.flip()
    # 초당 프레임 설정
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
sys.exit()


