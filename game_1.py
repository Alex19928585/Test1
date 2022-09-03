import pygame
from settings import *
from figure import figure
import time
import random

pygame.font.init()
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode((WIDTH-400, HEIGHT))


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 20))
        self.image.fill(pygame.Color('gold'))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)
        self.speed = 8
        self.kx = -1
        self.ky = 1
        self.valid = False

    def update(self):
        # self.rect.y += self.speed * self.kx
        pass


lst_figure = figure()

for i in range(len(lst_figure)):
    print(lst_figure[i])

b1 = Block()
all_sprites.add(b1)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Клавиатура
    pressed_keys = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass



    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
