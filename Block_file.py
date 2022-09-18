import pygame
from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, col, rect_x, rect_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((58, 58))
        self.image.fill(pygame.Color(col))
        self.rect = self.image.get_rect()

        self.speed = 5
        self.kx = -1
        self.ky = 1
        self.rect.center = (rect_x, rect_y)
        self.x = 0
        self.y = 0
        self.live = False

    def move(self):
        self.rect.y -= self.speed * self.kx
        # print(self.rect.bottom, self.rect.center[0])
        if self.rect.bottom > HEIGHT:
            self.x = self.rect.center[0]
            self.rect.center = (self.x, 690)
        if self.rect.center[1] == 690:
            self.live = False
            self.speed = 0
        if self.rect.right > WIDTH:
            self.x = self.rect.center[0]
            self.y = self.rect.center[1]
            self.rect.center = (self.x-60, self.y)