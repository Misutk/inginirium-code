import random

import pygame

pygame.init()
FPS = 25
W, H = 500, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Starry sky!")
stars = []


class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255,) * 3

    def draw(self, root):
        if self.color[0] >= 0:
            pygame.draw.circle(root, self.color, (self.x, self.y), 5)
            self.color = (self.color[0] - 1,) * 3


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        stars.append(Star(x, y))
    pygame.draw.circle(win, (75,) * 3, (random.randint(0, W), random.randint(0, H)), 1)
    for s in stars:
        s.draw(win)
    if len(stars) > 0:
        if stars[0].color[0] == 0:
            stars.pop(0)

    pygame.display.update()
    clock.tick(FPS)
