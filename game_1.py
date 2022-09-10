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

screen = pygame.display.set_mode((WIDTH-320, HEIGHT))


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(pygame.Color('gold'))
        self.rect = self.image.get_rect()
        self.image1 = pygame.Surface((30, 30))
        self.image1.fill(pygame.Color('gold'))
        self.rect1 = self.image1.get_rect()

        self.speed = 8
        self.kx = -1
        self.ky = 1
        self.valid = False
        self.rect.center = (300, 300)
        self.rect1.center = (400, 400)

    def update(self):
        # self.rect.y += self.speed * self.kx
        pass


lst_figure = figure()
lst_figure_full = []

# Создание фигуры



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
