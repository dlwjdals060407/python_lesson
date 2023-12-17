import pygame
import sys
import random
import math

# 파이게임 초기화
pygame.init()

# 화면 설정
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("간단한 파이게임 예제")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 ,0)

light_start = (width // 20, random.randint(0, height //2))
angle = math.radians(random.uniform(270, 360))
line_length = 100

n1 = 1.0
n2 = 1.5

speed_glass = n1 / n2

light_end_air = (light_start[0] + int(line_length * math.cos(angle)),
             light_start[1] - int(line_length * math.sin(angle)))

light_end_glass = (light_start[0] + int(line_length * math.cos(angle)),
                   light_start[1] - int(line_length * math.sin(angle)) - 50)

font = pygame.font.Font(None, 36)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    x = pygame.draw.line(screen, white, (0, height // 2), (width, height // 2), 2)
    y = pygame.draw.line(screen, white, (width // 20, 0), (width // 20, height), 2)

    pygame.draw.circle(screen, red, light_start, 5)    

    intersection_point = (width // 20, height // 2) #원점으로 지정
    pygame.draw.circle(screen, red, intersection_point, 5)

    text = font.render("O", True, white)
    screen.blit(text, (intersection_point[0] + 5, intersection_point[1] - 25))

    pygame.draw.line(screen, red, light_start, light_end_air, 2)

    # 직선 그리기 (유리)
    pygame.draw.line(screen, red, light_end_air, light_end_glass, 2)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정 (30프레임)
    pygame.time.Clock().tick(60)
