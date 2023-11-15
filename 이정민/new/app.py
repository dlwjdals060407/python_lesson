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


frameCnt = 0

player = Character(screen_width//2, screen_height-50, 20)

LEFT = False
RIGHT = False
UP = False
DONW = False

enemys = []
enemyBullets = []

running = True
while running:
    frameCnt += 1
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if frameCnt == 10:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 3, 20, attr=0))
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 3, 20, attr=0))
    if frameCnt == 40:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 5, 20, attr=0))
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 5, 20, attr=0))
    if frameCnt == 60:
        for e in enemys:
            enemyBullets.append(Bullet(e.x, e.y, 0, 6, 4))
    if frameCnt == 70:
        enemys.append(Enemy(0, 50, 8, 2, 20, attr=1))
    if frameCnt == 80:
        enemys.append(Enemy(0, 50, 8, 2, 20, attr=1))
    if frameCnt == 90:
        enemys.append(Enemy(0, 50, 8, 2, 20, attr=1))
    if frameCnt == 100:
        for e in enemys:
            enemyBullets.append(Bullet(e.x, e.y, (player.x-e.x)/100, (player.y-e.y)/100, 4))
    if frameCnt == 300:
        enemys.append(Enemy(screen_width//2 - 50, 0, 0, 2, 20, attr=0))
    if frameCnt == 320:
        enemys.append(Enemy(screen_width//2 + 50, 0, 0, 2, 20, attr=0))
    if frameCnt == 350:
        for e in enemys:
            enemyBullets = e.pattern1(enemyBullets)
    if frameCnt == 400:
        enemys.append(Enemy(screen_width//2, 0, 0, 2, 20, attr=0))
    if frameCnt == 420:
        for e in enemys:
            enemyBullets = e.pattern2(enemyBullets)
    if frameCnt == 500:
        enemys.append(Enemy(screen_width, 50, -8, 2, 20, attr = 1))
    if frameCnt == 510:
        enemys.append(Enemy(screen_width, 50, -8, 2, 20, attr = 1))
    if frameCnt == 520:
        enemys.append(Enemy(screen_width, 50, -8, 2, 20, attr = 1))
    if frameCnt == 525:
        for e in enemys:
            if e.attr == 1:
                for angles in range(0, 360, 20):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle)*3, math.sin(angle)*3, 4))
    if frameCnt == 540:
        for e in enemys:
            if e.attr == 1:
                for angles in range(0, 360, 20):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle)*3, math.sin(angle)*3, 4))
    if frameCnt == 555:
        for e in enemys:
            if e.attr == 1:
                for angles in range(0, 360, 20):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle)*3, math.sin(angle)*3, 4))
    if frameCnt == 560:
        enemys.append(Enemy(screen_width//2, 0, 0, 2, 20, attr=0))
    if frameCnt == 570:
        for e in enemys:
            if e.attr == 0:
                enemyBullets = e.pattern3(enemyBullets)                
    
    # enemy update
    for e in enemys:
        e.update()
    
    # draw enemy
    for e in enemys:
        pygame.draw.circle(screen, (0,0,0), (e.x, e.y), e.rad)
    
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
        enemyBullets = b.update(enemyBullets, player)
    
    # draw enemy bullet
    for b in enemyBullets:
        pygame.draw.circle(screen, (0, 0, 0), (b.x, b.y), b.rad)
    
    # delete enemy bullet
    for b in enemyBullets:
        if b.x < 0 or b.x > screen_width:
            enemyBullets.remove(b)
            continue
        if b.y < 0 or b.y > screen_height:
            enemyBullets.remove(b)
            continue
    
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