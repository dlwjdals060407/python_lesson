import pygame
import sys
from Character import Character
from Enemy import Enemy
from Bullet import Bullet
import random
import math

# Pygame 초기화
pygame.init()

# 창 크기 설정
screen_width = 600
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

rotate_angle = 0

frameCnt = 0

player = Character(screen_width//2, screen_height-50, 20)
player_health = 0

LEFT = False
RIGHT = False
UP = False
DONW = False

enemys = []
enemyBullets = []
playerBullets = []

running = True
while running:
    frameCnt += 1
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(frameCnt)
    
    if frameCnt == 10:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 3, 20, 45, attr=0))
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 3, 20, 45, attr=0))
    if frameCnt == 40:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 5, 20, 45, attr=0))
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 5, 20, 45, attr=0))
    if frameCnt == 60:
        for e in enemys:
            enemyBullets.append(Bullet(e.x, e.y, 0, 6, 4))
    if frameCnt == 70:
        enemys.append(Enemy(0, 50, 8, 2, 20, 45, attr=1))
    if frameCnt == 80:
        enemys.append(Enemy(0, 50, 8, 2, 20, 45, attr=1))
    if frameCnt == 90:
        enemys.append(Enemy(0, 50, 8, 2, 20, 45, attr=1))
    if frameCnt == 100:
        for e in enemys:
            enemyBullets.append(Bullet(e.x, e.y, (player.x-e.x)/100, (player.y-e.y)/100, 4))
    if frameCnt == 300:
        enemys.append(Enemy(screen_width//2 - 50, 0, 0, 2, 20, 45, attr=0))
    if frameCnt == 320:
        enemys.append(Enemy(screen_width//2 + 50, 0, 0, 2, 20, 45, attr=0))
    if frameCnt == 350:
        for e in enemys:
            enemyBullets = e.pattern1(enemyBullets)
    if frameCnt == 400:
        enemys.append(Enemy(screen_width//2, 0, 0, 2, 20, 45, attr=0))
    if frameCnt == 420:
        for e in enemys:
            enemyBullets = e.pattern2(enemyBullets)
    if frameCnt == 500:
        enemys.append(Enemy(screen_width, 50, -8, 2, 20, 45, attr = 1))
    if frameCnt == 510:
        enemys.append(Enemy(screen_width, 50, -8, 2, 20, 45, attr = 1))
    if frameCnt == 520:
        enemys.append(Enemy(screen_width, 50, -8, 2, 20, 45, attr = 1))
    if frameCnt == 525:
        for e in enemys:
            if e.attr == 1:
                for angles in range(0, 360, 45):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle)*3, math.sin(angle)*3, 4))
    if frameCnt == 540:
        for e in enemys:
            if e.attr == 1:
                for angles in range(0, 360, 45):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle)*3, math.sin(angle)*3, 4))
    if frameCnt == 555:
        for e in enemys:
            if e.attr == 1:
                for angles in range(0, 360, 45):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle)*3, math.sin(angle)*3, 4))
    if frameCnt == 560:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 2, 20, 45, attr=3))
    if frameCnt >= 600 and frameCnt % 60 == 0:
        for e in enemys:
            if e.attr == 3:
                for angles in range(0, 360, 20):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 3, math.sin(angle) * 3, 4))
    if frameCnt == 620:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 2, 20, 45, attr=4))
    if frameCnt >= 680 and frameCnt % 68 == 0:
        for e in enemys:
            if e.attr == 4:
                for angles in range(0, 360, 20):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 3, math.sin(angle) * 3, 4))
    if frameCnt == 720:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 2, 20, 45, attr=5))
    if frameCnt >= 720 and frameCnt % 72 == 0:
        for e in enemys:
            if e.attr == 5:
                for angles in range(0, 360, 20):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 3, math.sin(angle) * 3, 4))
    if frameCnt == 800:
        enemys.append(Enemy(100, 0, 0, 2, 20, 45, attr=6))
        enemys.append(Enemy(500, 0, 0, 2, 20, 45, attr=6))
    if frameCnt >= 820 and frameCnt % 82 == 0:
        for e in enemys:
            if e.attr == 6:
                enemyBullets = e.pattern4(enemyBullets)
    if frameCnt >= 870 and frameCnt % 87 == 0:
        for e in enemys:
            if e.attr == 6:
                enemyBullets = e.pattern5(enemyBullets)
    if frameCnt == 1300:
        enemys.append(Enemy(screen_width//2, 0, 0, 1, 75, 2000, attr=7))
    if 1500 <= frameCnt <= 2300 and frameCnt % 40 == 0:
        for e in enemys:
            if e.attr == 7:
                enemyBullets = e.boss_pattern_1(enemyBullets)
    if frameCnt == 2250:
        enemys.append(Enemy(e.x, e.y, 0, 1, 35, 500, attr=9))
        enemys.append(Enemy(e.x , e.y, 0, 1, 35, 500, attr=10))
    if 2420 <= frameCnt <= 2850 and frameCnt % 40 == 0:
        rotate_angle += 6
        for e in enemys:
            if e.attr == 9 or e.attr == 10:
                for angles in range(rotate_angle, rotate_angle+360, 30):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 2, math.sin(angle) * 5, 5))
    if frameCnt > 2850 and frameCnt % 40 ==0:
        for e in enemys:
            if e.attr == 9 or e.attr == 10:
                rotate_angle += 3
                for angles in range(rotate_angle, rotate_angle+360, 20):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 2, math.sin(angle) * 5, 5))
    if 3250 <= frameCnt <= 4300 and frameCnt % 15 == 0:
        rotate_angle +=9
        for e in enemys:
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 3, math.sin(angle) * 3, 7))
    if frameCnt == 4700:
        pass

    # enemy update
    for e in enemys:
        e.update()
        if e.is_colliding_with_player(player):
            pass
    
    # draw enemy
    for e in enemys:
        pygame.draw.circle(screen, (0,0,102), (e.x, e.y), e.rad)
    
    # delete enemy
    for e in enemys:
        if e.x < 0 or e.x > screen_width:
            enemys.remove(e)
            continue
        if e.y < 0 or e.y > screen_height:
            enemys.remove(e)
            continue
    
    # enemy bullet update
    for b in enemyBullets:
        if b.is_colliding_with_player(player):
            pass
        enemyBullets = b.update(enemyBullets, player)
    
    # draw enemy bullet
    for b in enemyBullets:
        pygame.draw.circle(screen, (0, 0, 255), (b.x, b.y), b.rad)
    
    # delete enemy bullet
    for b in enemyBullets:
        if b.x < 0 or b.x > screen_width:
            enemyBullets.remove(b)
            continue
        if b.y < 0 or b.y > screen_height:
            enemyBullets.remove(b)
            continue
    
    for b in enemyBullets:
        if b.is_colliding_with_player(player):
            if b in enemyBullets:
                enemyBullets.remove(b)

    bullets_to_remove = []

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and frameCnt % 3 == 0:  
        playerBullets.append(Bullet(player.x-15, player.y, -0.15, -15, 7))  
        playerBullets.append(Bullet(player.x, player.y, 0, -15, 7))
        playerBullets.append(Bullet(player.x+15, player.y, 0.15, -15, 7))

    for bullet in playerBullets:
        bullet.update(playerBullets, player)

    # draw player bullets
    for bullet in playerBullets:
        pygame.draw.circle(screen, (0, 0, 0), (bullet.x, bullet.y), bullet.rad)

    for b in playerBullets:
        for e in enemys:
            if e.is_colliding_with_bullet(b):
                if b in playerBullets:
                    playerBullets.remove(b)
                if e.health <= 0:
                    enemys.remove(e)

    # delete player bullets
    playerBullets = [bullet for bullet in playerBullets if 0 < bullet.y < screen_height]

    # player move
    keys = pygame.key.get_pressed()
    player.move(keys)
    
    # draw player
    pygame.draw.circle(screen, (255, 0, 0), (player.x, player.y), player.rad)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 초당 60프레임으로 제한

# Pygame 종료
pygame.quit()
sys.exit()