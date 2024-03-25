from math import sqrt

import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
x = 250
y = 250
color = (0, 0, 0)
speed = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if sqrt((250 - x) ** 2 + (250 - y) ** 2) > 150:
        color = (255, 0, 0)
        speed = 5
    else:
        color = (0, 0, 0)
        speed = 3
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        x = 250
        y = 250
    elif x == 450 or x == 50 or y == 450 or y == 50:
        pygame.draw.line(win,(0,0,0), (x-35,y-35),(x+35,y-35))
        pygame.draw.line(win, (0, 0, 0), (x + 35, y + 35), (x - 35, y + 35))
        x = x
        y = y

    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    elif keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    else:
        if x < 250:
            x += speed
        elif x > 250:
            x -= speed
        elif y < 250:
            y += speed
        elif y > 250:
            y -= speed

    win.fill((255, 255, 255))
    pygame.draw.circle(win, color, (x, y), 50)
    pygame.display.update()

    pygame.time.delay(10)
