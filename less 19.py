import random

import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))


class Circle:
    is_jump = False
    jump_counter = 30

    def __init__(self, color, radius, wight, x, y):
        self.rad = radius
        self.color = color
        self.wight = wight
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def move_by_keys(self):
        if self.is_jump:
            if self.jump_counter >= -30:
                self.y -= self.jump_counter
                self.jump_counter -= 1

            else:
                self.jump_counter = 30
                self.is_jump = False
                self.color = (
                    random.randrange(0, 256),
                    random.randrange(0, 256),
                    random.randrange(0, 256)
                )

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 5
        elif keys[pygame.K_s]:
            self.y += 5
        if keys[pygame.K_a]:
            self.x -= 5
        elif keys[pygame.K_d]:
            self.x += 5
        if keys[pygame.K_SPACE]:
            self.is_jump = True


circle = Circle((225, 0, 225), 25, 5, 260, 250)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    circle.move_by_keys()
    win.fill((255, 255, 255))
    circle.draw(win)
    pygame.display.update()
    pygame.time.delay(10)
