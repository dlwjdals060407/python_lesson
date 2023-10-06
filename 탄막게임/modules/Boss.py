import pygame
import random
import math
from modules.Enemy import EnemyBullet

class Boss:
    def __init__(self, x, y, screen, screen_height):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 200
        self.speed = 3
        self.screen = screen
        self.active = True
        self.shoot_timer = 0
        self.shoot_interval = 10
        self.screen_height = screen_height
        self.move_direction_x = random.choice([-1, 1])
        self.move_direction_y = random.choice([-1, 1])
        self.color = (0, 0, 0)
        self.health = 50
        self.bullets = []

        self.patterns = []  # 여러 개의 패턴을 저장할 리스트

        # 패턴 객체들을 생성하고 패턴 리스트에 추가
        self.pattern1 = BossPattern1(self)
        self.patterns.append(self.pattern1)

        self.pattern2 = BossPattern2(self)
        self.patterns.append(self.pattern2)

        # 현재 활성화된 패턴의 인덱스
        self.active_pattern_index = -1

    def move(self):
        if self.active:
            self.x += self.speed * self.move_direction_x
            self.y += self.speed * self.move_direction_y

            if self.x <= 0 or self.x >= 400:
                self.move_direction_x *= -1
            if self.y <= 50 or self.y >= 150:
                self.move_direction_y *= -1

    def shoot(self, player_x, player_y):
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            player_dx = player_x - self.x
            player_dy = player_y - self.y
            angle = math.atan2(player_dy, player_dx)

            bullet_x = self.x + self.width // 2 - 1
            bullet_y = self.y + self.height
            self.bullets.append(EnemyBullet(bullet_x, bullet_y, angle, self.screen_height))

            self.shoot_timer = 0

    def update(self, player_x, player_y):
        self.move()
        self.shoot(player_x, player_y)
        self.update_bullets()

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.is_offscreen():
                self.bullets.remove(bullet)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def check_collision(self, bullet):
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        boss_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(boss_rect)

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw(self.screen)

    def activate_pattern(self, pattern_index):
        # 패턴을 활성화하고 현재 활성화된 패턴 인덱스 설정
        if 0 <= pattern_index < len(self.patterns):
            self.active_pattern_index = pattern_index
            self.patterns[pattern_index].activate()

    def deactivate_pattern(self):
        # 현재 활성화된 패턴을 비활성화하고 인덱스 초기화
        if 0 <= self.active_pattern_index < len(self.patterns):
            self.patterns[self.active_pattern_index].deactivate()
            self.active_pattern_index = -1

    def update(self, player_x, player_y):
        self.move()
        self.shoot(player_x, player_y)
        self.update_bullets()

        if 0 <= self.active_pattern_index < len(self.patterns):
            # 현재 활성화된 패턴이 있다면 실행
            self.patterns[self.active_pattern_index].update(player_x, player_y)

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw(self.screen)

class BossPattern1:
    def __init__(self, boss):
        self.boss = boss
        self.pattern_active = False
        self.pattern_timer = 0
        self.pattern_interval = 5
        self.bullet_angle = 0

    def activate(self):
        self.pattern_active = True
        self.pattern_timer = 0
        self.bullet_angle = 0

    def deactivate(self):
        self.pattern_active = False

    def update(self, player_x, player_y):
        self.pattern_timer += 1

        if self.pattern_active and self.pattern_timer >= self.pattern_interval:
            self.execute_pattern(player_x, player_y)
            self.pattern_timer = 0

    def execute_pattern(self, player_x, player_y):
        self.boss.bullets = []  # 패턴 시작 시 총알 리스트 초기화
        num_bullets = 12  # 패턴에서 발사할 총알 수
        bullet_speed = 5

        # 플레이어의 위치와 보스의 위치를 사용하여 발사 각도 계산
        angle_radians = math.atan2(player_y - self.boss.y, player_x - self.boss.x)

        for _ in range(num_bullets):
            bullet_x = self.boss.x + self.boss.width // 2 - 1
            bullet_y = self.boss.y + self.boss.height
            bullet = EnemyBullet(bullet_x, bullet_y, angle_radians, self.boss.screen_height)
            bullet.speed = bullet_speed
            self.boss.bullets.append(bullet)
    
    def move(self):
        # 패턴 1의 움직임을 원형 모양으로 구현
        if self.pattern_active:
            radius = 100  # 원의 반지름
            angular_speed = 0.03  # 원을 따라 움직이는 속도 (조절 가능)

            self.boss.x = self.boss.player_x + radius * math.cos(angular_speed * self.pattern_timer)
            self.boss.y = self.boss.player_y + radius * math.sin(angular_speed * self.pattern_timer)

    def draw(self):
        for bullet in self.boss.bullets:
            bullet.move()
            bullet.draw(self.boss.screen)


class BossPattern2:
    def __init__(self, boss,angle):
        self.boss = boss
        self.pattern_active = False
        self.pattern_timer = 0
        self.pattern_interval = 5
        self.bullet_angle = 0
        self.angle = angle

    def activate(self):
        self.pattern_active = True
        self.pattern_timer = 0
        self.bullet_angle = 0

    def deactivate(self):
        self.pattern_active = False

    def update(self, player_x, player_y):
        self.pattern_timer += 1

        if self.pattern_active and self.pattern_timer >= self.pattern_interval:
            self.execute_pattern(player_x, player_y)
            self.pattern_timer = 0

    def execute_pattern(self, player_x, player_y):
        self.boss.bullets = []  # 패턴 시작 시 총알 리스트 초기화
        num_bullets = 12  # 패턴에서 발사할 총알 수
        bullet_speed = 5

        for i in range(num_bullets):
            angle_radians = math.radians(self.bullet_angle)
            bullet_x = self.boss.x + self.boss.width // 2 - 1
            bullet_y = self.boss.y + self.boss.height
            bullet = EnemyBullet(bullet_x, bullet_y, angle_radians, self.boss.screen_height)
            bullet.speed = bullet_speed
            self.boss.bullets.append(bullet)
            self.bullet_angle += 30  # 각도를 조절하여 원형 모양으로 총알이 발사되도록 함
    
    def move(self):
        # 각도와 속도를 사용하여 총알 이동
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
    
    def draw(self):
        for bullet in self.boss.bullets:
            bullet.move()
            bullet.draw(self.boss.screen)

    def activate(self):
        self.pattern_active = True
        self.pattern_timer = 0
        self.bullet_angle = 0

    def deactivate(self):
        self.pattern_active = False

    def update(self, player_x, player_y):
        self.pattern_timer += 1

        if self.pattern_active and self.pattern_timer >= self.pattern_interval:
            self.execute_pattern(player_x, player_y)
            self.pattern_timer = 0

    def execute_pattern(self, player_x, player_y):
        self.boss.bullets = []  # 패턴 시작 시 총알 리스트 초기화
        num_bullets = 12  # 패턴에서 발사할 총알 수
        bullet_speed = 5

        for i in range(num_bullets):
            angle_radians = math.radians(self.bullet_angle)
            bullet_x = self.boss.x + self.boss.width // 2 - 1
            bullet_y = self.boss.y + self.boss.height
            bullet = EnemyBullet(bullet_x, bullet_y, angle_radians, self.boss.screen_height)
            bullet.speed = bullet_speed
            self.boss.bullets.append(bullet)
            self.bullet_angle += 30  # 각도를 조절하여 원형 모양으로 총알이 발사되도록 함
    
    def draw(self):
        for bullet in self.boss.bullets:
            bullet.move()
            bullet.draw(self.boss.screen)


class BossPattern2:
    def __init__(self, boss):
        self.boss = boss
        self.pattern_active = False
        self.pattern_timer = 0
        self.pattern_interval = 5
        self.bullet_angle = 0

    def activate(self):
        self.pattern_active = True
        self.pattern_timer = 0
        self.bullet_angle = 0

    def deactivate(self):
        self.pattern_active = False

    def update(self, player_x, player_y):
        self.pattern_timer += 1

        if self.pattern_active and self.pattern_timer >= self.pattern_interval:
            self.execute_pattern(player_x, player_y)
            self.pattern_timer = 0

    def execute_pattern(self, player_x, player_y):
        self.boss.bullets = []  # 패턴 시작 시 총알 리스트 초기화
        num_bullets = 12  # 패턴에서 발사할 총알 수
        bullet_speed = 5

        for i in range(num_bullets):
            angle_radians = math.radians(self.bullet_angle)
            bullet_x = self.boss.x + self.boss.width // 2 - 1
            bullet_y = self.boss.y + self.boss.height
            bullet = EnemyBullet(bullet_x, bullet_y, angle_radians, self.boss.screen_height)
            bullet.speed = bullet_speed
            self.boss.bullets.append(bullet)
            self.bullet_angle += 30  # 각도를 조절하여 원형 모양으로 총알이 발사되도록 함
    
    def move(self):
        # 각도와 속도를 사용하여 총알 이동
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
    
    def draw(self):
        for bullet in self.boss.bullets:
            bullet.move()
            bullet.draw(self.boss.screen)
