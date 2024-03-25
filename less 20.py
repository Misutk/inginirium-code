import random

import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))


class Figuri:
    def __init__(self, x, y, color, ):
        self.x = x
        self.y = y
        self.color = color
        self.dir = [random.random(), random.random()]
        self.axis = random.choice(("x", "y"))

    def move(self):

        self.x += self.dir[0] * 3

        self.y -= self.dir[1] * 3
        if self.x > 500 or  self.x < 0:
            self.dir[0] *= -1
        if self.y > 500 or self.y < 0:
            self.dir[1] *= -1

    def draw(self, root):
        pygame.draw.polygon(root, self.color, ((self.x, self.y),))


class Circle(Figuri):
    def __init__(self, x, y, color, rad):
        super().__init__(x, y, color)
        self.rad = rad

    def draw(self, root):
        pygame.draw.circle(root, self.color, (self.x, self.y), self.rad)


class Rect(Figuri):

    def __init__(self, x, y, color, w, h):
        super().__init__(x, y, color)
        self.w = w
        self.h = h

    def draw(self, root):
        pygame.draw.rect(root, self.color, (self.x, self.y, self.w, self.h))


objects = [random.choice((
    Circle(random.randint(0, 500), random.randint(0, 500), random.choices(range(256), k=3), random.randint(15, 50)),
    Rect(random.randint(0, 500), random.randint(0, 500), random.choices(range(256), k=3), random.randint(15, 50),
         random.randint(10, 50))
)) for _ in range(24)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 0))
    for figura in objects:
        figura.move()
        figura.draw(win)

    pygame.display.update()
    pygame.time.delay(10)
