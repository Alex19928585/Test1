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
        # if self.rect.bottom > 655:
        #     self.rect.center = (200, 200)



grid = [pygame.Rect(x * 60, y * 60, 60, 60) for x in range(10) for y in range(20)]
lst_block = []
lst_full_line = []
valid_right = 0
valid_left = 0
result = []

# def create_object():
#
#     b1 = Block('gold', 270, 50)
#     all_sprites.add(b1)
#     return b1

valid = False

running = True
while running:
    clock.tick(FPS)
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False


    [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]

    # if kol == 0 or b1.live != True:
    #     b1 = create_object()
    #     kol = 1


    if len(lst_block) == 0:
        if valid == False:
            lst_block.append(Block('gold', 270, 50))
            lst_block[-1].live = True

    elif lst_block[-1].live == False:
        lst_block.append(Block('gold', 270, 50))
        lst_block[-1].live = True

    for i in lst_block:
        all_sprites.add(i)
        # print(i.live)
    for i in lst_block:
        if i.live == True:
            i.move()


    for k in lst_block:
        if k != lst_block[-1]:
            x = lst_block[-1].rect.center[0]
            if lst_block[-1].rect.center[1] + 60 == k.rect.center[1] and lst_block[-1].rect.center[0] == k.rect.center[0]:
                lst_block[-1].live = False

    # Клавиатура
    pressed_keys = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()

    # Проверка на блок справа
    for i in lst_block:
        if i != lst_block[-1]:
            if lst_block[-1].rect.center[0] + 60 == i.rect.center[0] and i.rect.center[1] - 60 <= \
                    lst_block[-1].rect.center[1] <= i.rect.center[1] + 60:
                valid_right = True
                break
            else:
                valid_right = False
    # Проверка на блок справа
    for i in lst_block:
        if i != lst_block[-1]:
            if lst_block[-1].rect.center[0] - 60 == i.rect.center[0] and i.rect.center[1] - 60 <= \
                    lst_block[-1].rect.center[1] <= i.rect.center[1] + 60:
                valid_left = True
                break
            else:
                valid_left = False

    if keys[pygame.K_RIGHT] and lst_block[-1].rect.center[0] != 510 and valid_right == False:
        y = lst_block[-1].rect.center[1]
        x = lst_block[-1].rect.center[0]
        lst_block[-1].rect.center = (x+60, y)
        time.sleep(0.1)
    elif keys[pygame.K_LEFT] and lst_block[-1].rect.center[0] != 30 and valid_left == False:
        y = lst_block[-1].rect.center[1]
        x = lst_block[-1].rect.center[0]
        lst_block[-1].rect.center = (x - 60, y)
        time.sleep(0.1)
    elif len(lst_block) == 1 and keys[pygame.K_DOWN]:
        lst_block[-1].speed = 10

    elif keys[pygame.K_DOWN]:

        for i in range(len(lst_block)):
            if i != len(lst_block)-1:
                if lst_block[i].rect.center[0] == lst_block[-1].rect.center[0] and lst_block[i].rect.center[1]-90 < lst_block[-1].rect.center[1]:
                    lst_block[-1].speed = 5
                    break
                else:
                    lst_block[-1].speed = 10
    else:
        lst_block[-1].speed = 5

    # Удаление ряда

    for i in lst_block:
        if i.rect.center[1] == 690:
            lst_full_line.append(i)
    # if len(lst_full_line) == 9:
    #     for i in lst_full_line:
    #         i.image.fill(pygame.Color('white'))
    #     time.sleep(1)
    if len(lst_full_line) == 9:
        for i in lst_full_line:
            i.rect.center = (700, 1000)
            i.kill()
        for i in lst_block:
            if i not in lst_full_line:
                i.rect.center = (i.rect.center[0], i.rect.center[1]+60)
        # Перезаписываем массив с эементами, убирая при этом элементы удаленной линии
        for i in lst_block:
            if i not in lst_full_line:
                result.append(i)
        lst_block = []
        lst_block.extend(result)
        result = []
        lst_full_line = []
    else:
        lst_full_line = []

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
