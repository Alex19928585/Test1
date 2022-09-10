import pygame
from settings import *
import time
import random

pygame.font.init()
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Block(pygame.sprite.Sprite):
    def __init__(self, col, rect_x, rect_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(pygame.Color(col))
        self.rect = self.image.get_rect()

        self.speed = 8
        self.kx = -1
        self.ky = 1
        self.valid = False
        self.rect.center = (rect_x, rect_y)

    def move(self):
        self.rect.y -= self.speed * self.kx


# Создание фигуры
b1 = Block('gold', 300, 50)
all_sprites.add(b1)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    Block.move(b1)


    # Клавиатура
    pressed_keys = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
