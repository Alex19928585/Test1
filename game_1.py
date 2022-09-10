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
        self.x = 0

    def move(self):
        self.rect.y -= self.speed * self.kx
        print(self.rect.bottom, self.rect.center[1])
        if self.rect.bottom == 658:
            self.speed = 0
        if self.rect.bottom > HEIGHT:
            self.x = self.rect.center[0]
            self.rect.center = (self.x, 620)


# Создание фигуры
b1 = Block('gold', 300, 50)
all_sprites.add(b1)

running = True
while running:
    clock.tick(FPS)
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    Block.move(b1)


    # Клавиатура
    pressed_keys = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        b1.rect.x += b1.speed
    elif keys[pygame.K_LEFT]:
        b1.rect.x -= b1.speed

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
