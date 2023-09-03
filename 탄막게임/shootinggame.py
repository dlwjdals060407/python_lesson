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

    def check_collision(self, bullet):
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(enemy_rect)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, red, (self.x, self.y, self.width, self.height))

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 스페이스바를 누를 때 총알 객체를 생성하고 리스트에 추가
                bullets.append(Bullet(player.x + player.width // 2 - 1, player.y))

    keys = pygame.key.get_pressed()
    player.move(keys)

    if random.randint(1, 100) == 90:
        x = random.randint(0, screen_width - 50)
        enemyList.append(Enemy(x, 0, screen))

    # 총알 이동 및 화면을 벗어나면 제거
    bullets = [bullet for bullet in bullets if not bullet.is_offscreen()]

    for enemy in enemyList:
        for bullet in bullets:
            if enemy.check_collision(bullet):
                enemyList.remove(enemy)
                bullets.remove(bullet)

    for enemy in enemyList:
        if enemy.active:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
            if enemy.check_collision(player_rect):
                player.health -= 1
                enemyList.remove(enemy)
                if player.health == 0:
                    running = False

    # 화면 업데이트
    screen.fill(white)

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen) 

    for enemy in enemyList:
        enemy.move()
        enemy.draw()

    font = pygame.font.Font(None, 30)
    health_text = font.render(f'Helth: {player.health}', True, red)
    screen.blit(health_text, (10, 700) )

    player.draw(screen)
    pygame.display.update()
    # 초당 프레임 설정
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
sys.exit()