import pygame

a, n = [int(i) for i in input().split()]
pygame.init()
win = pygame.display.set_mode((a, a))
win.fill((255, 255, 255))
if a % n != 0:
    print("неверно")
    exit()
h = a // n

for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            pygame.draw.rect(win, (0, 0, 0), (i*h, j*h, h, h))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
