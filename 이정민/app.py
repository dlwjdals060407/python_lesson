import pygame
import sys
import random
import math
from Bullet import Bullet
from Character import Character,Boss

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

def spawn():
    std = random.randint(0, 5000)
    if std < 5:
        # 네임드 스폰
        pass
    if std < 500:
        # 잡몹 스폰
        return 1
    return 0

def random_shoot():
    std = random.randint(0, 5000)
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

player = Character(screen_width//2, screen_height - 30, 0, 0, 20)
player_bullets = []
player_health = 50

boss = None
boss_pattern_timer_1 = 0
boss_pattern_interval_1 = 20
boss_pattern_timer_2 = 0
boss_pattern_interval_2 = 30
boss_pattern_timer_3 = 0
boss_pattern_interval_3 = 150
boss_pattern3_main_bullet = []
boss_pattern3_bullet = []
boss_pattern3_attack_timer = 0
boss_pattern_timer_4 = 0
boss_pattern_interval_4 = 20
boss_health = 5 
time_tick = 0

frame_tick = 0

enemy_catch = 0

flikering_cnt = 15

enemy_spawn = True

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
    
    if enemy_spawn == True:
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
            if bullet.rad == 20:
                boss_pattern3_main_bullet.remove(bullet)
            player_health -= 1
            
            if player_health <= 0:
                running = False

    for bullet in player_bullets:
        bullet.update()
        pygame.draw.circle(screen, (0,0,255), (bullet.posX, bullet.posY), bullet.rad)
        
        if enemy_spawn == True:
            for enemy in enemys:
                if bullet.is_colliding_with_enemy(enemy):#적이 플레이어 총알에 맞았을 때
                    if bullet in player_bullets:
                        player_bullets.remove(bullet)
                    else:
                        pass
                    if enemy in enemys:
                        enemys.remove(enemy)
                        enemy_catch += 1
                    else:
                        pass

        if boss is not None and bullet.is_colliding_with_boss(boss):
            player_bullets.remove(bullet)
            boss_health -= 1

            if boss_health <= 0:
                boss = None
                enemy_spawn = True

    if enemy_catch >= 2:
        if boss is None:
            boss = Boss(screen_width // 2, 100, 3, 0, 40, screen_width)
            enemy_catch = 0
            enemy_spawn = False

    if boss is not None:
        boss.update()
        pygame.draw.circle(screen, (0, 0, 0), (boss.posX, boss.posY), boss.rad)
        rotate_angle += 6
        # 패턴 로직
        if boss_health >= 4 :
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
        if boss_health ==3:
            if boss_pattern_timer_2 <= 0:
                num_bullets = 8  # 생성할 총알 수 조절
                for _ in range(num_bullets):
                    # 무작위 방향 생성 (화면 테두리에서 시작)
                    side = random.choice(["top", "bottom", "left", "right"])
                    if side == "top":
                        posX = random.uniform(0, screen_width)
                        posY = 0
                    elif side == "bottom":
                        posX = random.uniform(0, screen_width)
                        posY = screen_height
                    elif side == "left":
                        posX = 0
                        posY = random.uniform(0, screen_height)
                    else:
                        posX = screen_width
                        posY = random.uniform(0, screen_height)

                    # 방향 벡터 계산
                    direction = math.atan2(player.posY - posY, player.posX - posX)
                    bullet_speed = 3  # 총알 속도

                    # 총알 생성
                    bullet = Bullet(posX, posY, bullet_speed * math.cos(direction), bullet_speed * math.sin(direction), 6)
                    bullets.append(bullet)
    
            if boss_pattern_timer_2 <= 0:            
                boss_pattern_timer_2 = boss_pattern_interval_2
            else:
                boss_pattern_timer_2 -= 1

        #패턴 3
        if boss_health == 2:
            print(boss_pattern3_attack_timer)
            if boss_pattern_timer_3 <= 0:
                angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
                print("큰거나옴")
                boss_pattern3_attack_timer =0
                for angle in angles:
                    radian_angle = math.radians(angle)
                    bullet_x = boss.posX + 70 * math.cos(radian_angle)
                    bullet_y = boss.posY + 70 * math.sin(radian_angle)
                    bullet = Bullet(bullet_x, bullet_y, (bullet_speed * math.cos(radian_angle))*3, (bullet_speed * math.sin(radian_angle))*3, 20)
                    bullets.append(bullet)
                    boss_pattern3_main_bullet.append(bullet)
                # if bullet.is_colliding_with_player(player):
                #     boss_pattern3_main_bullet.remove(bullet)
                #     player_health -= 1

                boss_pattern_timer_3 = boss_pattern_interval_3
            else:
                boss_pattern_timer_3 -= 1
                boss_pattern3_attack_timer += 1
            if boss_pattern3_attack_timer == 30:
                for main_bullet in boss_pattern3_main_bullet:
                    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
                        bullet_direction = math.radians(angle)
                        new_bullet = Bullet(main_bullet.posX, main_bullet.posY,bullet_speed * math.cos(bullet_direction), bullet_speed * math.sin(bullet_direction),5)
                        bullets.append(new_bullet)

        #패턴 4
        if boss_health == 1:
            if boss_pattern_timer_4 <= 0:
                time_tick = 0

                boss_pattern_timer_4 = boss_pattern_interval_4
                        
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