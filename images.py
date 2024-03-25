import random
from os import PathLike
from typing import Any, IO

import pygame as pg

pg.init()
size = W, H = 700, 700
FPS = 30
win = pg.display.set_mode(size)


def load_img(name: str | bytes | PathLike[str] | PathLike[bytes] | IO[bytes] | IO[str]):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img


class Ingiinirium(pg.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.image = pg.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) * random.choice((1, -1)),
                                   random.randrange(3) * random.choice((1, -1)))

        new_img = pg.transform.rotate(self.image,random.randrange(3) * random.choice((1, -1)))

        self.rect = new_img.get_rect(center=self.rect.center)
        self.image = new_img


img = load_img('ing.png')
all_sprites = pg.sprite.Group()
for _ in range(9999):
    Ingiinirium(img, all_sprites)

clock = pg.time.Clock()
angle = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    win.fill((255,) * 3)
    all_sprites.update()
    all_sprites.draw(win)

    pg.display.update()

    clock.tick(FPS)
