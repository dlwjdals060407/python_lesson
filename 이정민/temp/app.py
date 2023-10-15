import pygame
import sys

pygame.init()

width = 600
height = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("탄막게임")

frame_tick = 0
pygame.font.init()
font = pygame.font.Font(None, 36)

flickering_cnt = 15
interval = 60

running = True

while running:
    screen.fill((255, 255, 255))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if frame_tick % 10 in [0, 1, 2] and flickering_cnt > 0:
        pygame.draw.circle(screen, (120,120,120), (width//2, height//2), 60)
        flickering_cnt -= 1

    if flickering_cnt <= 0 and interval > 0:
        pygame.draw.circle(screen, (120,120,120), (width//2, height//2), (interval + 10))
        pygame.draw.circle(screen, (180,180,180), (width//2, height//2), (interval + 10) * 2 // 3)
        pygame.draw.circle(screen, (220,220,220), (width//2, height//2), (interval + 10) // 3)
        pygame.draw.rect(screen, (120, 120, 120), (width//2-interval//2, height//2, interval, height))
        interval -= 1

    
    frame_tick += 1
    pygame.display.update()
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
sys.exit()