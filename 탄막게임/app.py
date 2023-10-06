import pygame
import sys
import random
import math
from modules.Enemy import Enemy, EnemyBullet
from modules.Bullet import Bullet
from modules.Player import Player
from modules.Boss import Boss

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 600
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("탄막게임")

player_bullet = []
enemies = []
enemy_bullet = []
boss = None
boss_active = False
boss_health = 20
boss_spawn_timer = 0
boss_spawn_interval = 50  # 보스 등장 간격 설정

# 메인 루프
running = True
player = Player(300, 700, screen_width, screen_height)
enemy_bullet_timer = 0
enemies_catch = 0
boss_pattern_active = False  # 보스 패턴 활성화 여부를 나타내는 변수
current_boss_pattern = 0  # 현재 활성화된 보스 패턴 인덱스

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_bullet.append(Bullet(player.x + player.width // 2 - 1, player.y))

    keys = pygame.key.get_pressed()
    player.move(keys)

    if not boss_active:
        if random.randint(1, 10 ) == 9:
            x = random.randint(0, screen_width - 50)
            enemies.append(Enemy(x, 0, screen, screen_height))

    if enemies_catch >= 1 and not boss_active:
        boss_spawn_timer += 1
        if boss_spawn_timer >= boss_spawn_interval:
            x = random.randint(0, screen_width - 200)
            boss = Boss(x, 0, screen, screen_height)
            boss_active = True
            boss_spawn_timer = 0
            boss_pattern_active = True  # 보스 패턴 활성화
            current_boss_pattern = 0
            boss.activate_pattern(0)
            
    for enemy in enemies:
        shoot_timer, shoot_interval, x, y, width, height = enemy.update(player.x, player.y)
        if shoot_timer >= shoot_interval:
            player_dx = player.x - x
            player_dy = player.y - y

            # 발사 각도 계산 (라디안 단위)
            angle = math.atan2(player_dy, player_dx)

            # 총알 생성 및 발사
            bullet_x = x + width // 2 - 1
            bullet_y = y + height
            enemy_bullet.append(EnemyBullet(bullet_x, bullet_y, angle, screen_height))

    enemy_bullet_timer += 1

    if enemy_bullet_timer >= 10:  # 총알 발사 타이머
        for enemy in enemies:
            if enemy.active:
                shoot_timer, shoot_interval, x, y, width, height = enemy.update(player.x, player.y)
                if shoot_timer >= shoot_interval:
                    player_dx = player.x - x
                    player_dy = player.y - y

                    # 발사 각도 계산 (라디안 단위)
                    angle = math.atan2(player_dy, player_dx)

                    # 총알 생성 및 발사
                    bullet_x = x + width // 2 - 1
                    bullet_y = y + height
                    enemy_bullet.append(EnemyBullet(bullet_x, bullet_y, angle, screen_height))
                enemy.resetTimer()
        enemy_bullet_timer = 0

    player_bullet = [bullet for bullet in player_bullet if not bullet.is_offscreen()]

    for enemy in enemies:  # 적이 플레이어의 총알에 닿았을 때
        for bullet in player_bullet:
            if enemy.check_collision(bullet):
                enemies.remove(enemy)
                player_bullet.remove(bullet)
                enemies_catch += 1

    if boss_active:
        for bullet in player_bullet:
            if boss.check_collision(bullet):
                player_bullet.remove(bullet)
                boss_health -= 1
                if boss_health <= 0:
                    boss_active = False
                    boss_health = 20
                    boss_pattern_active = False  # 보스 패턴 비활성화
                    current_boss_pattern = 0  # 첫 번째 패턴을 활성화

    for enemy in enemies:  # 적과 플레이어가 닿았을 때
        if enemy.active:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
            if enemy.check_collision(player_rect):
                player.health -= 1
                enemies.remove(enemy)
                if player.health == 0:
                    running = False

    enemy_bullet = [bullet for bullet in enemy_bullet if not bullet.is_offscreen()]

    for enemy in enemy_bullet:  # 플레이어가 적 총알에 닿았을 때
        for bullet in enemy_bullet:
            if player.check_collision(bullet):
                enemy_bullet.remove(bullet)
                player.health -= 1  # 플레이어 체력 감소
                if player.health == 0:
                    running = False

    screen.fill(white)

    for bullet in player_bullet:
        bullet.move()
        bullet.draw(screen)

    for enemy in enemies:
        enemy.move()
        enemy.draw()

    if boss_active:
        boss.move()
        boss.draw()
        boss.update(player.x, player.y)

        if boss_pattern_active:
            boss.patterns[current_boss_pattern].update(player.x, player.y)
            boss.patterns[current_boss_pattern].draw()  # 현재 활성화된 패턴을 그림

    for bullet in enemy_bullet:
        bullet.move()
        bullet.draw(screen)

    font = pygame.font.Font(None, 30)
    health_text = font.render(f'Health: {player.health}', True, red)
    screen.blit(health_text, (10, 700))

    player.draw(screen)
    pygame.display.update()
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
sys.exit()