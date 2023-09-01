import pygame 
import random
import sys

pygame.init()

width = 800
heigh = 600

white = (255,255,255)
player_cr = (0, 0, 255)

player_size = 50
player_speed = 5
player_x = (width - heigh)/2
player_y = (width - heigh) - 10

screen = pygame.display.set_mode((width, heigh))

pygame.display.set_caption("탄막게임")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_left]:
        player_x -= player_x
    if keys[pygame.K_RIGHT]:
        player_x += player_x
    if keys[pygame.K_DOWN]:
        player_y -= 

    screen.fill(white)
    pygame.display.update()

pygame.quit()
sys.exit()