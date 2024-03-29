import pygame
import sys
from Character import Character
from Enemy import Enemy
from Bullet import Bullet
import random
import math
import time

# Pygame 초기화
pygame.init()

# 창 크기 설정
screen_width = 600
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

background_image = pygame.image.load("asset/background.png")
background_rect = background_image.get_rect()
background_y = -background_rect.height + screen_height

# enemy_image = pygame.image.load("asset/jotgilgo.png")
# enemy_image = pygame.transform.scale(enemy_image, (40, 40))

player_image = pygame.image.load("asset/player.png")  
player_image = pygame.transform.scale(player_image, (40, 40))

bullet_image = pygame.image.load("asset/bullet.png")
bullet_image = pygame.transform.scale(bullet_image, (40, 40))

enemy_image = pygame.image.load("asset/enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (40, 40))
rotate_angle = 0

Time = time.time()

frameCnt = 0
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 30)

player = Character(screen_width//2, screen_height-50, 20)
player_health = 5

LEFT = False
RIGHT = False
UP = False
DONW = False

enemys = []
enemyBullets = []
playerBullets = []

name = []

Collision = True
running = True
game_over = False
game_clear = False
while running and not game_over:
    frameCnt += 1
    print(frameCnt)
    screen.fill((255, 255, 255))
    screen.blit(background_image, (-300, background_y))
    background_y += 3
    if background_y > 0:
        background_y = -background_rect.height + screen_height
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # print(frameCnt)
    
    if frameCnt == 10:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 3, 20, 45, attr=0))
    if frameCnt == 20:
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
            enemyBullets.append(Bullet(e.x, e.y, (player.x-e.x)/100, (player.y-e.y)/100, 2))
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
        enemys.append(Enemy(100, 0, 0, 2, 20, 35, attr=6))
        enemys.append(Enemy(500, 0, 0, 2, 20, 35, attr=6))
    if frameCnt >= 820 and frameCnt % 82 == 0:
        for e in enemys:
            if e.attr == 6:
                enemyBullets = e.pattern4(enemyBullets)
    if frameCnt >= 870 and frameCnt % 87 == 0:
        for e in enemys:
            if e.attr == 6:
                enemyBullets = e.pattern5(enemyBullets)
    if frameCnt == 1300:#1300
        enemys.append(Enemy(screen_width//2, 0, 0, 1, 75, 1, attr=7))#보스
    if 1500 <= frameCnt <= 2500 and frameCnt % 40 == 0: #1500 - 2300
        for e in enemys:
            if e.attr == 7:
                enemyBullets = e.boss_pattern_1(enemyBullets)
    if frameCnt == 2300: #2200
        enemys.append(Enemy(e.x, e.y, 0, 1, 35, 500, attr=9))
        enemys.append(Enemy(e.x , e.y, 0, 1, 35, 500, attr=10))
    if 2420 <= frameCnt <= 2850 and frameCnt % 40 == 0: #2420 - 2850
        rotate_angle += 6
        for e in enemys:
            if e.attr == 9 or e.attr == 10:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 2, math.sin(angle) * 5, 5))
    if frameCnt > 2850 and frameCnt % 40 ==0: # 2850
        for e in enemys:
            if e.attr == 9 or e.attr == 10:
                rotate_angle += 3
                for angles in range(rotate_angle, rotate_angle+360, 10):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 2, math.sin(angle) * 5, 5))
    if 2900 <= frameCnt <= 3600 and frameCnt % 15 == 0: #3050 - 3600
        rotate_angle +=9
        for e in enemys:
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * -3, math.sin(angle) * 3, 10))
    if frameCnt == 3700: #3700
        enemys.append(Enemy(e.x, e.y, 1, 1, 20, 100, attr=11))
        enemys.append(Enemy(e.x, e.y, 1, 1, 20, 100, attr=12))
    if 3750 <= frameCnt <= 4500 and frameCnt % 20 == 0:
        for e in enemys:
            if e.attr == 11 or e.attr == 12:
                rotate_angle += 3
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle) * 5, 5))
    if 4600<= frameCnt <= 5300 and frameCnt % 40 == 0:
        if e.attr == 11:
            if e in enemys:
                enemys.remove(e)
        if e.attr == 12:
            if e in enemys:
                enemys.remove(e)    
        for e in enemys:
            rotate_angle +=3
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle) * 5, 10))
    if 4620<= frameCnt <= 5320 and frameCnt % 20 == 0:
        for e in enemys:
            rotate_angle +=3
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle)+ 5, 10))
    if frameCnt == 5500:
        game_clear = True

    # enemy update
    for e in enemys:
        # screen.blit(enemy_image, (e.x- 20, e.y- 20))
        enemyBullets = e.update(enemyBullets)
        if e.is_colliding_with_player(player):
            player_health -= 1
            if player_health <= 0:
                running = False  
    
    # draw enemy
    for e in enemys:
        pygame.draw.circle(screen, (255,204,51), (e.x, e.y), e.rad)
        # pygame.draw.rect(screen, (255, 0, 0), (e.x - e.rad, e.y - e.rad - 10, e.health, 5))
        health_text = font2.render(f'{e.health}', True, (255, 0, 0))
        screen.blit(health_text, ((e.x - e.rad)+5, e.y - e.rad - 20))
        # transparent_surface = pygame.Surface((e.rad * 2, e.rad * 2), pygame.SRCALPHA)
        # pygame.draw.circle(transparent_surface, (0, 0, 0, 255), (e.rad, e.rad), e.rad)
        # screen.blit(enemy_image, (e.x-20, e.y-20))
        
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
            player_health -= 1
            if player_health <= 0:
                game_over = True
                running = False
        enemyBullets = b.update(enemyBullets, player)
    
    # draw enemy bullet
    for b in enemyBullets:
        # screen.blit(bullet_image, (b.x - b.rad, b.y - b.rad))
        pygame.draw.circle(screen, (255, 51, 0), (b.x, b.y), b.rad)
    
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
                player_health -= 1
                if player_health <= 0 :
                    running = False
                    game_over = True 

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
        pygame.draw.circle(screen, (102, 255, 255), (bullet.x, bullet.y), bullet.rad)

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
    player.move(keys, screen_width, screen_height)
    
    # draw player
    transparent_surface = pygame.Surface((player.rad * 2, player.rad * 2), pygame.SRCALPHA)
    pygame.draw.circle(transparent_surface, (0, 0, 0, 255), (player.rad, player.rad), player.rad)
    screen.blit(player_image, (player.x-20, player.y-20))

    health_text = font.render(f'Health: {player_health}', True, (255, 0, 0))
    screen.blit(health_text, (10, screen_height - 60))
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 초당 60프레임으로 제한

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False  # Exit the game over screen
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = False  # Exit the game over screen
            elif event.key == pygame.K_RETURN:
                # Restart the game
                player_health = 5
                enemys = []
                playerBullets = []
                enemyBullets = []
                player.x = screen_width // 2
                player.y = screen_height - 50
                game_over = False  # Exit the game over screen
                running = True  # Start the game
                frameCnt = 0

    screen.fill((255, 255, 255))
    game_over_text = font.render("Game Over", True, (0, 0, 0))
    screen.blit(game_over_text, (screen_width // 2 - 50, screen_height // 2 - 20))
    press_enter_text = font.render("Press ENTER to restart", True, (0, 0, 0))
    screen.blit(press_enter_text, (screen_width // 2 - 120, screen_height // 2 + 20))
    life_text = font.render("life = (1/3) ", True, (0, 0, 0))
    screen.blit(life_text, (screen_width // 2 - 50, screen_height // 2 + 40))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

while running and not game_over:
    frameCnt += 1
    screen.fill((255, 255, 255))
    screen.blit(background_image, (-300, background_y))
    background_y += 3
    if background_y > 0:
        background_y = -background_rect.height + screen_height
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # print(frameCnt)
    
    if frameCnt == 10:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 3, 20, 45, attr=0))
    if frameCnt == 20:
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
            enemyBullets.append(Bullet(e.x, e.y, (player.x-e.x)/100, (player.y-e.y)/100, 2))
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
        enemys.append(Enemy(100, 0, 0, 2, 20, 35, attr=6))
        enemys.append(Enemy(500, 0, 0, 2, 20, 35, attr=6))
    if frameCnt >= 820 and frameCnt % 82 == 0:
        for e in enemys:
            if e.attr == 6:
                enemyBullets = e.pattern4(enemyBullets)
    if frameCnt >= 870 and frameCnt % 87 == 0:
        for e in enemys:
            if e.attr == 6:
                enemyBullets = e.pattern5(enemyBullets)
    if frameCnt == 1300:#1300
        enemys.append(Enemy(screen_width//2, 0, 0, 1, 75, 2500, attr=7))#보스
    if 1500 <= frameCnt <= 2500 and frameCnt % 40 == 0: #1500 - 2300
        for e in enemys:
            if e.attr == 7:
                enemyBullets = e.boss_pattern_1(enemyBullets)
    if frameCnt == 2300: #2200
        enemys.append(Enemy(e.x, e.y, 0, 1, 35, 500, attr=9))
        enemys.append(Enemy(e.x , e.y, 0, 1, 35, 500, attr=10))
    if 2420 <= frameCnt <= 2850 and frameCnt % 40 == 0: #2420 - 2850
        rotate_angle += 6
        for e in enemys:
            if e.attr == 9 or e.attr == 10:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 2, math.sin(angle) * 5, 5))
    if frameCnt > 2850 and frameCnt % 40 ==0: # 2850
        for e in enemys:
            if e.attr == 9 or e.attr == 10:
                rotate_angle += 3
                for angles in range(rotate_angle, rotate_angle+360, 10):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 2, math.sin(angle) * 5, 5))
    if 2900 <= frameCnt <= 3600 and frameCnt % 15 == 0: #3050 - 3600
        rotate_angle +=9
        for e in enemys:
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * -3, math.sin(angle) * 3, 10))
    if frameCnt == 3700: #3700
        enemys.append(Enemy(e.x, e.y, 1, 1, 20, 100, attr=11))
        enemys.append(Enemy(e.x, e.y, 1, 1, 20, 100, attr=12))
    if 3750 <= frameCnt <= 4500 and frameCnt % 20 == 0:
        for e in enemys:
            if e.attr == 11 or e.attr == 12:
                rotate_angle += 3
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle) * 5, 5))
    if 4600<= frameCnt <= 5300 and frameCnt % 40 == 0:
        if e.attr == 11:
            enemys.remove(e)
        if e.attr == 12:
            enemys.remove(e)
        for e in enemys:
            rotate_angle +=3
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle) * 5, 10))
    if 4620<= frameCnt <= 5320 and frameCnt % 20 == 0:
        for e in enemys:
            rotate_angle +=3
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle)+ 5, 10))
    if frameCnt == 6000:
        game_clear = True

    # enemy update
    for e in enemys:
        # screen.blit(enemy_image, (e.x- 20, e.y- 20))
        enemyBullets = e.update(enemyBullets)
        if e.is_colliding_with_player(player):
            player_health -= 1
            if player_health <= 0:
                running = False  
    
    # draw enemy
    for e in enemys:
        pygame.draw.circle(screen, (255,204,51), (e.x, e.y), e.rad)
        # pygame.draw.rect(screen, (255, 0, 0), (e.x - e.rad, e.y - e.rad - 10, e.health, 5))
        health_text = font2.render(f'{e.health}', True, (255, 0, 0))
        screen.blit(health_text, ((e.x - e.rad)+5, e.y - e.rad - 20))
        # transparent_surface = pygame.Surface((e.rad * 2, e.rad * 2), pygame.SRCALPHA)
        # pygame.draw.circle(transparent_surface, (0, 0, 0, 255), (e.rad, e.rad), e.rad)
        # screen.blit(enemy_image, (e.x-20, e.y-20))
        
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
            player_health -= 1
            if player_health <= 0:
                game_over = True
                running = False
        enemyBullets = b.update(enemyBullets, player)
    
    # draw enemy bullet
    for b in enemyBullets:
        # screen.blit(bullet_image, (b.x - b.rad, b.y - b.rad))
        pygame.draw.circle(screen, (255, 51, 0), (b.x, b.y), b.rad)
    
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
                player_health -= 1
                if player_health <= 0 :
                    running = False
                    game_over = True 

    bullets_to_remove = []

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and frameCnt % 3 == 0:  
        playerBullets.append(Bullet(player.x-15, player.y, -0.2, -15, 7))
        playerBullets.append(Bullet(player.x-5, player.y, -0.15, -15, 7))  
        playerBullets.append(Bullet(player.x, player.y, 0, -15, 7))
        playerBullets.append(Bullet(player.x+5, player.y, 0.15, -15, 7))
        playerBullets.append(Bullet(player.x+15, player.y, 0.2, -15, 7))

    for bullet in playerBullets:
        bullet.update(playerBullets, player)

    # draw player bullets
    for bullet in playerBullets:
        pygame.draw.circle(screen, (102, 255, 255), (bullet.x, bullet.y), bullet.rad)

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
    player.move(keys, screen_width, screen_height)
    
    # draw player
    transparent_surface = pygame.Surface((player.rad * 2, player.rad * 2), pygame.SRCALPHA)
    pygame.draw.circle(transparent_surface, (0, 0, 0, 255), (player.rad, player.rad), player.rad)
    screen.blit(player_image, (player.x-20, player.y-20))

    health_text = font.render(f'Health: {player_health}', True, (255, 0, 0))
    screen.blit(health_text, (10, screen_height - 60))
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 초당 60프레임으로 제한

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False  # Exit the game over screen
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = False  # Exit the game over screen
            elif event.key == pygame.K_RETURN:
                # Restart the game
                player_health = 5
                enemys = []
                playerBullets = []
                enemyBullets = []
                player.x = screen_width // 2
                player.y = screen_height - 50
                game_over = False  # Exit the game over screen
                running = True  # Start the game
                frameCnt = 0

    screen.fill((255, 255, 255))
    game_over_text = font.render("Game Over", True, (0, 0, 0))
    screen.blit(game_over_text, (screen_width // 2 - 50, screen_height // 2 - 20))
    press_enter_text = font.render("Press ENTER to restart", True, (0, 0, 0))
    screen.blit(press_enter_text, (screen_width // 2 - 120, screen_height // 2 + 20))
    life_text = font.render("life = (2/3)", True, (0, 0, 0))
    screen.blit(life_text, (screen_width // 2 - 50, screen_height // 2 + 40))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

while running and not game_over:
    frameCnt += 1
    screen.fill((255, 255, 255))
    screen.blit(background_image, (-300, background_y))
    background_y += 3
    if background_y > 0:
        background_y = -background_rect.height + screen_height
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # print(frameCnt)
    
    if frameCnt == 10:
        enemys.append(Enemy(random.randint(0, screen_width), 0, 0, 3, 20, 45, attr=0))
    if frameCnt == 20:
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
            enemyBullets.append(Bullet(e.x, e.y, (player.x-e.x)/100, (player.y-e.y)/100, 2))
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
        enemys.append(Enemy(100, 0, 0, 2, 20, 35, attr=6))
        enemys.append(Enemy(500, 0, 0, 2, 20, 35, attr=6))
    if frameCnt >= 820 and frameCnt % 82 == 0:
        for e in enemys:
            if e.attr == 6:
                enemyBullets = e.pattern4(enemyBullets)
    if frameCnt >= 870 and frameCnt % 87 == 0:
        for e in enemys:
            if e.attr == 6:
                enemyBullets = e.pattern5(enemyBullets)
    if frameCnt == 1300:#1300
        enemys.append(Enemy(screen_width//2, 0, 0, 1, 75, 2500, attr=7))#보스
    if 1500 <= frameCnt <= 2500 and frameCnt % 40 == 0: #1500 - 2300
        for e in enemys:
            if e.attr == 7:
                enemyBullets = e.boss_pattern_1(enemyBullets)
    if frameCnt == 2300: #2200
        enemys.append(Enemy(e.x, e.y, 0, 1, 35, 500, attr=9))
        enemys.append(Enemy(e.x , e.y, 0, 1, 35, 500, attr=10))
    if 2420 <= frameCnt <= 2850 and frameCnt % 40 == 0: #2420 - 2850
        rotate_angle += 6
        for e in enemys:
            if e.attr == 9 or e.attr == 10:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 2, math.sin(angle) * 5, 5))
    if frameCnt > 2850 and frameCnt % 40 ==0: # 2850
        for e in enemys:
            if e.attr == 9 or e.attr == 10:
                rotate_angle += 3
                for angles in range(rotate_angle, rotate_angle+360, 10):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 2, math.sin(angle) * 5, 5))
    if 2900 <= frameCnt <= 3600 and frameCnt % 15 == 0: #3050 - 3600
        rotate_angle +=9
        for e in enemys:
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * -3, math.sin(angle) * 3, 10))
    if frameCnt == 3700: #3700
        enemys.append(Enemy(e.x, e.y, 1, 1, 20, 100, attr=11))
        enemys.append(Enemy(e.x, e.y, 1, 1, 20, 100, attr=12))
    if 3700 <= frameCnt <= 4500 and frameCnt % 20 == 0:
        for e in enemys:
            if e.attr == 11 or e.attr == 12:
                rotate_angle += 3
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle) * 5, 5))
    if 4600<= frameCnt <= 5300 and frameCnt % 40 == 0:
        if e.attr == 11:
            enemys.remove(e)
        if e.attr == 12:
            enemys.remove(e)
        for e in enemys:
            rotate_angle +=3
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle) * 5, 10))
    if 4620<= frameCnt <= 5320 and frameCnt % 20 == 0:
        for e in enemys:
            rotate_angle +=3
            if e.attr == 7:
                for angles in range(rotate_angle, rotate_angle+360, 15):
                    angle = math.radians(angles)
                    enemyBullets.append(Bullet(e.x, e.y, math.cos(angle) * 5, math.sin(angle)+ 5, 10))
    if frameCnt == 6000:
        game_clear = True

    # enemy update
    for e in enemys:
        # screen.blit(enemy_image, (e.x- 20, e.y- 20))
        enemyBullets = e.update(enemyBullets)
        if e.is_colliding_with_player(player):
            player_health -= 1
            if player_health <= 0:
                running = False  
    
    # draw enemy
    for e in enemys:
        pygame.draw.circle(screen, (255,204,51), (e.x, e.y), e.rad)
        # pygame.draw.rect(screen, (255, 0, 0), (e.x - e.rad, e.y - e.rad - 10, e.health, 5))
        health_text = font2.render(f'{e.health}', True, (255, 0, 0))
        screen.blit(health_text, ((e.x - e.rad)+5, e.y - e.rad - 20))
        # transparent_surface = pygame.Surface((e.rad * 2, e.rad * 2), pygame.SRCALPHA)
        # pygame.draw.circle(transparent_surface, (0, 0, 0, 255), (e.rad, e.rad), e.rad)
        # screen.blit(enemy_image, (e.x-20, e.y-20))
        
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
            player_health -= 1
            if player_health <= 0:
                game_over = True
                running = False
        enemyBullets = b.update(enemyBullets, player)
    
    # draw enemy bullet
    for b in enemyBullets:
        # screen.blit(bullet_image, (b.x - b.rad, b.y - b.rad))
        pygame.draw.circle(screen, (255, 51, 0), (b.x, b.y), b.rad)
    
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
                player_health -= 1
                if player_health <= 0 :
                    running = False
                    game_over = True 

    bullets_to_remove = []

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and frameCnt % 3 == 0:  
        playerBullets.append(Bullet(player.x-15, player.y, -0.2, -15, 7))
        playerBullets.append(Bullet(player.x-5, player.y, -0.15, -15, 7))  
        playerBullets.append(Bullet(player.x, player.y, 0, -15, 7))
        playerBullets.append(Bullet(player.x+5, player.y, 0.15, -15, 7))
        playerBullets.append(Bullet(player.x+15, player.y, 0.2, -15, 7))

    for bullet in playerBullets:
        bullet.update(playerBullets, player)

    # draw player bullets
    for bullet in playerBullets:
        pygame.draw.circle(screen, (102, 255, 255), (bullet.x, bullet.y), bullet.rad)

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
    player.move(keys, screen_width, screen_height)
    
    # draw player
    transparent_surface = pygame.Surface((player.rad * 2, player.rad * 2), pygame.SRCALPHA)
    pygame.draw.circle(transparent_surface, (0, 0, 0, 255), (player.rad, player.rad), player.rad)
    screen.blit(player_image, (player.x-20, player.y-20))

    health_text = font.render(f'Health: {player_health}', True, (255, 0, 0))
    screen.blit(health_text, (10, screen_height - 60))
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 초당 60프레임으로 제한

while game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False  # Exit the game over screen
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = False  # Exit the game over screen
            elif event.key == pygame.K_RETURN:
                # Restart the game
                player_health = 5
                enemys = []
                playerBullets = []
                enemyBullets = []
                player.x = screen_width // 2
                player.y = screen_height - 50
                game_over = False  # Exit the game over screen
                running = True  # Start the game
                frameCnt = 0

    screen.fill((255, 255, 255))
    game_over_text = font.render("Game Over", True, (0, 0, 0))
    screen.blit(game_over_text, (screen_width // 2 - 50, screen_height // 2 - 20))
    press_enter_text = font.render("Press ENTER to restart", True, (0, 0, 0))
    screen.blit(press_enter_text, (screen_width // 2 - 120, screen_height // 2 + 20))
    life_text = font.render("life = (3/3)", True, (0, 0, 0))
    screen.blit(life_text, (screen_width // 2 - 50, screen_height // 2 + 40))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

while game_clear:
    screen.fill((255, 255, 255))
    game_clear_text = font.render("Game Cleared!", True, (0, 0, 0))
    screen.blit(game_clear_text, (screen_width // 2 - 70, screen_height // 2 - 20))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_clear = False
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Reset the game
            game_clear = False
            frameCnt = 0
            player_health = 5
            player.x = screen_width // 2
            player.y = screen_height - 50
            enemys = []
            enemyBullets = []
            playerBullets = []

# Pygame 종료
pygame.quit()
sys.exit()
