import pygame
import sys
import random
import math 

from modules.Enemy import Enemy
from modules.Bullet import Bullet
from modules.Player import Player

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

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
enemyList = [Enemy(50, 0, screen, screen_height)]
player = Player(300, 700, screen_width, screen_height)
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
        enemyList.append(Enemy(x, 0, screen, screen_height))

    for enemy in enemyList:
        enemy.update(player.x, player.y)

    enemy_bullet_timer += 1

    if enemy_bullet_timer >= 50: #총알 발사 타이머
        for enemy in enemyList:
            if enemy.active:
                enemy.update(player.x, player.y)
        enemy_bullet_timer = 0

    bullets = [bullet for bullet in bullets if not bullet.is_offscreen()]

    for enemy in enemyList: # 적이 플레이어의 총알에 닿았을 때
        for bullet in bullets:
            if enemy.check_collision(bullet):
                enemyList.remove(enemy)
                bullets.remove(bullet)

    for enemy in enemyList: # 적과 플레이어가 닿았을 때
        if enemy.active:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
            if enemy.check_collision(player_rect):
                player.health -= 1
                enemyList.remove(enemy)
                if player.health == 0:
                    running = False

    for enemy in enemyList: # 플레이어가 적 총알에 닿았을 때
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

