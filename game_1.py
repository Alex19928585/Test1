import pygame
from settings import *
import time
from Block_file import Block

pygame.font.init()
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# region Переменные и размер сети
grid = [pygame.Rect(x * 60, y * 60, 60, 60) for x in range(10) for y in range(20)]
lst_block = []
lst_full_line = []
valid_right = 0
valid_left = 0
result = []
valid = False
# endregion

running = True
while running:
    clock.tick(FPS)
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Отрисока сетки
    [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]

    # region Создание блока, live присваивается к объекту true(если у последнего оюъекта live == false)
    if len(lst_block) == 0:
        if valid == False:
            lst_block.append(Block('gold', 270, 50))
            lst_block[-1].live = True
    elif lst_block[-1].live == False:
        lst_block.append(Block('gold', 270, 50))
        lst_block[-1].live = True

    # отрисока блоков и если хоть один блок live == true --> двигать
    for i in lst_block:
        all_sprites.add(i)
        # print(i.live)
    for i in lst_block:
        if i.live == True:
            i.move()
    # endregion

    # region Проверка на столкновение блоков
    # Проверка соприкосновений активного блока с неактивными и при столкновении live последнего блока == false
    for k in lst_block:
        if k != lst_block[-1]:
            x = lst_block[-1].rect.center[0]
            if lst_block[-1].rect.center[1] + 60 == k.rect.center[1] and lst_block[-1].rect.center[0] == k.rect.center[0]:
                lst_block[-1].live = False

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
    # endregion

    # region Клавиатура
    pressed_keys = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()

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
    # endregion

    # region Ускорение
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
    # endregion

    # region Удаление ряда

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
    # endregion

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
