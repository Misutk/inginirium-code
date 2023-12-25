import pygame
pygame.init()
pygame.display.set_mode((600,400))


pygame.init()

w, h = input().split()
w = int(w)
h = int(h)
win = pygame.display.set_mode((w, h))
color = (0, 0, 0)
win.fill(color)
pygame.display.update()
pygame.draw.line(win, (255, 255, 255), (0, 0), (w, h), 5)
pygame.draw.line(win,(255,255,255), (w,0),(0,h), 5)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
