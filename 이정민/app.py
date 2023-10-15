import pygame
import sys
import random
import math
from Bullet import Bullet
from Character import Character,Boss
from Laser import Laser

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

def spawn():
    std = random.randint(0, 10000)
    if std < 5:
        # 네임드 스폰
        pass
    if std < 50:
        # 잡몹 스폰
        return 1
    return 0

def random_shoot():
    std = random.randint(0, 10000)
    if std < 5:
        # 네임드 스폰
        pass
    if std < 50:
        # 잡몹 스폰
        return 1
    return 0

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 600
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("탄막게임")

enemys = []
bullets = []
lasers = []

player = Character(screen_width//2, screen_height - 30, 0, 0, 20)
player_bullets = []
player_health = 500

boss = None
boss_pattern_timer_1 = 0
boss_pattern_interval_1 = 20
boss_pattern_timer_2 = 0
boss_pattern_interval_2 = 600
boss_health = 5 

frame_tick = 0

enemy_catch = 0

pygame.font.init()
font = pygame.font.Font(None, 36)

rotate_angle = 0

# 메인 루프
running = True

while running:
    screen.fill(white)
    frame_tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                print("player_shoot")
                player_bullets.append(Bullet(player.posX, player.posY, 0, -20, 5))
                
    keys = pygame.key.get_pressed()
    player.move(keys)
    
    ## random spawn
    if spawn() == 1:
        enemys.append(Character(random.randint(0, screen_width), 0, 0, 1, 20))
    
    ## patterned spawn
    # if frame_tick == 10:
    #     enemys.append(Character(random.randint(0, screen_width), 0, 0, 1, 10))
    # if frame_tick == 30:
    #     enemys.append(Character(random.randint(0, screen_width), 0, 0, 1, 10))
    # if frame_tick == 60:
    #     enemys.append(Character(random.randint(0, screen_width), 0, 0, 1, 10))
    
    for enemy in enemys:
        enemy.update()
        pygame.draw.circle(screen, (0,255,0), (enemy.posX, enemy.posY), enemy.rad)
        if random_shoot() == 1:
            # 유도탄 발사
            bullets.append(Bullet(enemy.posX, enemy.posY, (player.posX - enemy.posX) // 100, (player.posY - enemy.posY) // 100, 5))
            print("bullet spawned")
            
            for enemy in enemys:
                if enemy.is_colliding_with_player(player):
                    player_health -= 1
                    enemys.remove(enemy)

                    if player_health <= 0:
                        running = False

    for bullet in bullets:
        bullet.update()
        pygame.draw.circle(screen, (0,0,0), (bullet.posX, bullet.posY), bullet.rad)
        
        if bullet.is_colliding_with_player(player):#플레이어가 적 총알에 맞았을 때
            bullets.remove(bullet)
            player_health -= 1
            
            if player_health <= 0:
                running = False

    for bullet in player_bullets:
        bullet.update()
        pygame.draw.circle(screen, (0,0,255), (bullet.posX, bullet.posY), bullet.rad)
        
        for enemy in enemys:
            if bullet.is_colliding_with_enemy(enemy):#적이 플레이어 총알에 맞았을 때
                player_bullets.remove(bullet)
                enemys.remove(enemy)
                enemy_catch += 1

        if boss is not None and bullet.is_colliding_with_boss(boss):
            player_bullets.remove(bullet)
            boss_health -= 1

            if boss_health <= 0:
                boss = None

    if enemy_catch >= 2:
        if boss is None:
            boss = Boss(screen_width // 2, 100, 3, 0.1, 40, screen_width)
            enemy_catch = 0

    if boss is not None:
        boss.update()
        pygame.draw.circle(screen, (0, 0, 0), (boss.posX, boss.posY), boss.rad)
        rotate_angle += 6
        # 패턴 로직
        if boss_pattern_timer_1 <= 0:
        # 보스 패턴 실행
            bullet_speed = 3  # 총알 속도
            for angle_degrees in range(rotate_angle, rotate_angle + 360, 12):
                angle = math.radians(angle_degrees)  # 각도를 라디안으로 변환
                bullet = Bullet(boss.posX, boss.posY, bullet_speed * math.cos(angle), bullet_speed * math.sin(angle), 5)
                bullets.append(bullet)

            boss_pattern_timer_1 = boss_pattern_interval_1
        else:
            boss_pattern_timer_1 -= 1
            enemys = []

        # 패턴 2 실행 부분 (보스 체력이 일정 수준 아래로 떨어졌을 때)
        if boss_pattern_timer_2 <= 0:
            laser_speed = 5  # 레이저 속도
            laser_width = 10  # 레이저 너비
            laser_height = 100  # 레이저 높이
            for i in range(6):  # 6방향으로 레이저 발사 (60도 간격)
                angle_degrees = i * 60  # 각 레이저의 방향 (60도 간격)
                angle_radians = math.radians(angle_degrees)
                laser_xspeed = laser_speed * math.cos(angle_radians)
                laser_yspeed = laser_speed * math.sin(angle_radians)
                laser = Laser(boss.posX // 2 - laser_width // 2, boss.posY , laser_width, laser_height, laser_xspeed, laser_yspeed, lifespan=100)
                lasers.append(laser)

            boss_pattern_timer_2 = boss_pattern_interval_2
        else:
            boss_pattern_timer_2 -= 1

    for laser in lasers:
        laser.update()
        pygame.draw()

    bullets_to_remove = []
    for bullet in bullets:
        if (bullet.posX < 0 or bullet.posX > screen_width or
            bullet.posY < 0 or bullet.posY > screen_height):
            bullets_to_remove.append(bullet)

    for bullet in bullets_to_remove:
        bullets.remove(bullet)

    player.update()
    pygame.draw.circle(screen, (255,0,0), (player.posX, player.posY), player.rad)
    
    health_text = font.render("Health: " + str(player_health), True, (255, 0, 0))
    screen.blit(health_text, (10, screen_height - 40))
    
    pygame.display.update()
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
sys.exit()