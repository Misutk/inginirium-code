import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
dir_d = 1
dir_e = 1
dir_c = 1
dir_r = 1
y_c = 90
x_x = 1
e_e = 90
d_d = 90
u = 600
dir_u = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUT:I
            exit()

    x_x = x_x + 1 * dir_r
    d_d = d_d + 1 * dir_d
    e_e = e_e + 1 * dir_e
    y_c += 1 * dir_c
    u += dir_u
    if y_c > 550:
        dir_c = -1
    elif y_c < 50:
        dir_c = 1
    if x_x > 550:
        dir_r = -1
    elif x_x < 50:
        dir_r = 1
    if e_e < 0:
        dir_e = 1
    elif e_e > 550:
        dir_e = -1
    if d_d < 0:
        dir_d = 1
    elif d_d > 550:
        dir_d = -1
    if u < 0:
        dir_u = 1
    elif u > 550:
        dir_u = -1
    win.fill((0, 255, 255))
    pygame.draw.circle(win, (0, 0, 0), (100, y_c), 50)
    pygame.draw.rect(win, (255, 255, 255), (x_x, 100, 40, 50))
    pygame.draw.circle(win, (255, 255, 0), (d_d, u), 50)
    pygame.draw.circle(win, (255, 255, 255), (e_e, e_e), 50)
    pygame.display.update()

    pygame.time.delay(3)
