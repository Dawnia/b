import pygame
from random import randint
from pygame.draw import *

pygame.init()

# Функции рисования людей должны возвращать некоторые данные о своём положении,
# которые на самом деле не используются. Вернее, используется только у мужика,
# а у остальных в местах, где нужно их контачить, все константы положения в хардкоде

sizeX = 1100
sizeY = 600
FPS = 15

screen = pygame.display.set_mode((sizeX, sizeY))

numcloud = 5
list_of_circles = [[0, 0, 0], [0, 0, 0]]

# main circles
len_x = 16
len_y = 10
list_of_circles[0][0] = 7
list_of_circles[0][1] = 5
list_of_circles[0][2] = 5
list_of_circles[1][0] = 12
list_of_circles[1][1] = 7
list_of_circles[1][2] = 2
radius = min(len_x, len_y) // 2

i = 2
while not radius == 0:
    list_of_circles.append([0, 0, 0])
    x = randint(0, len_x)
    y = randint(0, len_y)
    r = radius
    list_of_circles[i][0], list_of_circles[i][1], list_of_circles[i][2] = x, y, r
    radius = int(radius / 1.3)
    i += 1


def cloud(x, y, k):
    """
    draws a cloud of the circles from the list of circles
    :param x: x-coord of the upper left point of the rect which the cloud in
    :param y: y-coord of...
    :param k: characteristic linear size of the cloud
    :return: none
    """
    for i in range(len(list_of_circles)):
        c_x = list_of_circles[i][0] * k
        c_y = list_of_circles[i][1] * k
        r = list_of_circles[i][2] * k
        circle(screen, (255, 255, 255), (x + c_x, y + c_y), r)


list_of_clouds = []
for i in range(numcloud):
    list_of_clouds.append([0, 0, 0, 0])
    k = randint(2, 7)
    x = randint(0, sizeX - k * len_x)
    y = randint(0, sizeY // 2 - k * len_y)
    speed = randint(k // 2, k)
    list_of_clouds[i][0], list_of_clouds[i][1], list_of_clouds[i][2], list_of_clouds[i][3] = x, y, k, speed


def draw_sfemale(x, y, r):
    """
    рисует симметричную женщину
    :param x: координата х центра головы женщины
    :param y: координата у центра головы женщины
    :param r: характерный размер женщины
    :return: полную ширину женщины (в единицах r)
    """
    line(screen, (0, 0, 0), (x - r // 2, y + 2 * r), (x - 4 * r, y + 6 * r), 2)
    line(screen, (0, 0, 0), (x + r // 2, y + 2 * r), (x + 4 * r, y + 6 * r), 2)
    lines(screen, (0, 0, 0), False, [(x - r, y + r * 8),
                                     (x - r, y + r * 11),
                                     (x - 2 * r, y + r * 11)], 2)
    lines(screen, (0, 0, 0), False, [(x + r, y + r * 8),
                                     (x + r, y + r * 11),
                                     (x + 2 * r, y + r * 11)], 2)
    polygon(screen, (200, 0, 200), [(x, y),
                                    (x - r * 3, y + r * 8),
                                    (x + r * 3, y + r * 8)])
    circle(screen, (255, 200, 200), (x, y), 2 * r)

    return 8


def draw_afemale(x, y, r, orientation):
    """
    рисует женщину с асимметричным расположением рук
    :param x: координата х центра головы женщины
    :param y: координата у центра головы женщины
    :param r: характерный размер женщины
    :param orientation: показывает, сгибает ли женщина
                        правую руку ('right') или левую ('left')
    :return: возвращает ширину женщины, а также
            положение по игреку её левой и правой рук (в единицах r)
    """
    if orientation == 'left':
        lines(screen, (0, 0, 0), False, [(x, y + 2 * r),
                                         (x + 3 * r, y + 4 * r),
                                         (x + 4 * r, y + 2 * r)], 2)
        line(screen, (0, 0, 0), (x - r // 2, y + 2 * r), (x - 4 * r, y + 6 * r), 2)
    else:
        lines(screen, (0, 0, 0), False, [(x, y + 2 * r),
                                         (x - 3 * r, y + 4 * r),
                                         (x - 4 * r, y + 2 * r)], 2)
        line(screen, (0, 0, 0), (x + r // 2, y + 2 * r), (x + 4 * r, y + 6 * r), 2)

    lines(screen, (0, 0, 0), False, [(x - r, y + r * 8),
                                     (x - r, y + r * 11),
                                     (x - 2 * r, y + r * 11)], 2)
    lines(screen, (0, 0, 0), False, [(x + r, y + r * 8),
                                     (x + r, y + r * 11),
                                     (x + 2 * r, y + r * 11)], 2)
    polygon(screen, (200, 0, 200), [(x, y),
                                    (x - r * 3, y + r * 8),
                                    (x + r * 3, y + r * 8)])
    circle(screen, (255, 200, 200), (x, y), 2 * r)

    return 8, 6, 2


def draw_male(x, y, r, orientation):
    """
    рисуется асимметричный мужик
    :param x: х головы мужика
    :param y: у головы мужика
    :param r: характерный линейный размер мужика
    :param orientation: правую ли ('right') или левую ('left') ногу он выставляет
    :return: возвращает ширину мужика, а также
            положение по игреку его рук (в единицах r)
    """
    if orientation == 'left':
        lines(screen, (0, 0, 0), False, [(x - r, y + 10 * r),
                                         (x - 3 * r, y + 18 * r),
                                         (x - 5 * r, y + 18 * r)], 2)
        lines(screen, (0, 0, 0), False, [(x + r, y + 10 * r),
                                         (x + 2 * r, y + 18 * r),
                                         (x + 4 * r, y + 18 * r)], 2)
    else:
        lines(screen, (0, 0, 0), False, [(x + r, y + 10 * r),
                                         (x + 3 * r, y + 18 * r),
                                         (x + 5 * r, y + 18 * r)], 2)
        lines(screen, (0, 0, 0), False, [(x - r, y + 10 * r),
                                         (x - 2 * r, y + 18 * r),
                                         (x - 4 * r, y + 18 * r)], 2)

    line(screen, (0, 0, 0), (x - r, y + 3 * r), (x - 6 * r, y + 9 * r), 2)
    line(screen, (0, 0, 0), (x + r, y + 3 * r), (x + 6 * r, y + 9 * r), 2)
    ellipse(screen, (150, 120, 150), [(x - 2 * r, y + r), (4 * r, 10 * r)])
    circle(screen, (255, 200, 200), (x, y), 2 * r)

    return 12, 9


def draw_family(x, y, r, n):
    """
    рисует семью (дед, бабка, дочери, Иван да Марья)
    :param x: координата х центр головы левого отца семейства
    :param y: координата у центр головы левого отца семейства
    :param r: характерный линейный размер семьи
    :param n: полуширина семьи (в единицах членов семьи)
    """
    x0, y0 = draw_male(x, y, r, 'left')
    x_11, y_11 = x - x0 * r // 2, y + y0 * r
    x_21, y_21 = x_11 - r, y_11 - 8 * r
    line(screen, (0, 0, 0), (x_11, y_11), (x_21, y_21))
    polygon(screen, (255, 0, 0), [(x_21, y_21),
                                  (x_21 - 5 * r // 2, y_21 - 7 * r // 2),
                                  (x_21 + 2 * r, y_21 - 7 * r // 2)])
    circle(screen, (255, 0, 0), (x_21 - 3 * r // 2, y_21 - 8 * r // 2), 3 * r // 2)
    circle(screen, (255, 0, 0), (x_21 + r, y_21 - 8 * r // 2), 3 * r // 2)

    if n >= 2:
        x_fem, y_fem = x + (x0 - 2) * r, y + y0 * r

        if n >= 3:
            for i in range(n - 2):
                draw_sfemale(x_fem + i * 8 * r, y + 3 * r, r)

        draw_afemale(x_fem + 8 * (n - 2) * r, y + 3 * r, r, 'left')
        draw_afemale(x_fem + 8 * (n - 1) * r, y + 3 * r, r, 'right')
        x_fem, y_fem = x_fem + 8 * n * r, y + 3 * r

        for i in range(n - 2):
            draw_sfemale(x_fem + i * 8 * r, y_fem, r)

        end = x + (16 * (n - 1) + x0) * r
        draw_male(end, y, r, 'right')

        x_12 = (x + end) // 2
        y_12 = y + 6 * r
        x_22 = x_12 - 3 * r // 2
        y_22 = y_12 - 10 * r
        line(screen, (0, 0, 0), (x_12, y_12), (x_22, y_22))
        circle(screen, (255, 255, 255), (x_22, y_22 - 4 * r), 3 * r // 2)
        polygon(screen, (140, 100, 100), [(x_22, y_22),
                                          (x_22 - 2 * r, y_22 - 3 * r),
                                          (x_22 + 2 * r, y_22 - 3 * r)])
        circle(screen, (235, 255, 120), (x_22 - 3 * r // 2, y_22 - 7 * r // 2), r)
        circle(screen, (120, 255, 235), (x_22 + 3 * r // 2, y_22 - 7 * r // 2), r)

        x_13 = end + x0 * r // 2
        y_13 = y + y0 * r
        x_23 = x_13 + 3 * r
        y_23 = y_13 - 10 * r
        line(screen, (0, 0, 0), (x_13, y_13), (x_23, y_23))
        circle(screen, (255, 255, 255), (x_23, y_23 - 4 * r), 3 * r // 2)
        polygon(screen, (140, 100, 100), [(x_23, y_23),
                                          (x_23 - 2 * r, y_23 - 3 * r),
                                          (x_23 + 2 * r, y_23 - 3 * r)])
        circle(screen, (235, 255, 120), (x_23 - 3 * r // 2, y_23 - 7 * r // 2), r)
        circle(screen, (120, 255, 235), (x_23 + 3 * r // 2, y_23 - 7 * r // 2), r)

    else:  # Это если просят нарисовать двух мужиков
        draw_male(x + x0 * r, y, r, 'right')

        x_12 = x + x0 * r // 2
        y_12 = y + y0 * r
        x_22 = x_12 - 3 * r // 2
        y_22 = y_12 - 10 * r
        line(screen, (0, 0, 0), (x_12, y_12), (x_22, y_22))
        circle(screen, (255, 255, 255), (x_22, y_22 - 4 * r), 3 * r // 2)
        polygon(screen, (140, 100, 100), [(x_22, y_22),
                                          (x_22 - 2 * r, y_22 - 3 * r),
                                          (x_22 + 2 * r, y_22 - 3 * r)])
        circle(screen, (235, 255, 120), (x_22 - 3 * r // 2, y_22 - 7 * r // 2), r)
        circle(screen, (120, 255, 235), (x_22 + 3 * r // 2, y_22 - 7 * r // 2), r)

        x_13 = x + 3 * x0 * r // 2
        y_13 = y + y0 * r
        x_23 = x_13 + 3 * r
        y_23 = y_13 - 10 * r
        line(screen, (0, 0, 0), (x_13, y_13), (x_23, y_23))
        circle(screen, (255, 255, 255), (x_23, y_23 - 4 * r), 3 * r // 2)
        polygon(screen, (140, 100, 100), [(x_23, y_23),
                                          (x_23 - 2 * r, y_23 - 3 * r),
                                          (x_23 + 2 * r, y_23 - 3 * r)])
        circle(screen, (235, 255, 120), (x_23 - 3 * r // 2, y_23 - 7 * r // 2), r)
        circle(screen, (120, 255, 235), (x_23 + 3 * r // 2, y_23 - 7 * r // 2), r)


frame_counter = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    screen = pygame.display.set_mode((sizeX, sizeY))
    screen.fill((200, 200, 255))
    for i in range(numcloud):
        x = list_of_clouds[i][0]
        y = list_of_clouds[i][1]
        k = list_of_clouds[i][2]
        if x >= sizeX:
            x = 0 - len_x * k

        cloud(x, y, k)
        list_of_clouds[i][0] = x + list_of_clouds[i][3]

    rect(screen, (15, 255, 20), (0, sizeY // 2, sizeX, sizeY // 2))
    draw_family(300, 250, 12, 3)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
