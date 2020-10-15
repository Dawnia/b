import pygame
from pygame.draw import *
from random import randint
from math import sqrt
pygame.init()

shrift = pygame.font.SysFont('serif', 30)

FPS = 24
sizeX = 800
sizeY = 500
numball = 10
numfem = 2
vmax = 5
screen = pygame.display.set_mode((sizeX, sizeY))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def draw_sfemale(x, y, r):
    """
    рисует симметричную женщину
    :param x: координата х центра головы женщины
    :param y: координата у центра головы женщины
    :param r: характерный размер женщины
    :return: none
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


femlist = [[0,0,0,0,0]]
for i in range(1, numfem):
    femlist.append([0,0,0,0,0])

def femmaster(i):
    femlist[i][2] = randint(4, 10)
    r = femlist[i][2]
    femlist[i][0] = randint(0, sizeX)
    femlist[i][1] = randint(0, sizeY - r * 11)
    femlist[i][3] = randint(-1 * vmax, vmax)
    vx = femlist[i][3]
    vy_max = int(sqrt(vmax**2 - vx**2))
    femlist[i][4] = randint(-1 * vy_max, vy_max)


for i in range(numfem):
    femmaster(i)

list_of_balls = [[0,0,0,0,0,0]]
for i in range(1, numball):
    list_of_balls.append([0,0,0,0,0,0])

def ballmaster(i):
    list_of_balls[i][2] = randint(10, 50)
    list_of_balls[i][0] = randint(list_of_balls[i][2], sizeX - list_of_balls[i][2])
    list_of_balls[i][1] = randint(list_of_balls[i][2], sizeY - list_of_balls[i][2])
    list_of_balls[i][3] = randint(0, 5)
    list_of_balls[i][4] = randint(-1 * vmax, vmax)
    vx = list_of_balls[i][4]
    vy_max = int(sqrt(vmax ** 2 - vx ** 2))
    list_of_balls[i][5] = randint(-1 * vy_max, vy_max)


for i in range(numball):
    ballmaster(i)

pygame.display.update()
clock = pygame.time.Clock()
score = 0
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    for i in range(numfem):
        x = femlist[i][0]
        y = femlist[i][1]
        r = femlist[i][2]
        vx = femlist[i][3]
        vy = femlist[i][4]
        if x - 4*r <= 0 or x + 4*r >= sizeX:
            vx *= -1
            if x - 4*r <= 0:
                x += r // 2
            else:
                x -= r // 2

        if y - 2*r <= 0 or y + 11*r >= sizeY:
            vy *= -1
            if y - 2*r <= 0:
                y += r // 2
            else:
                y -= r // 2

        femlist[i][0] = x
        femlist[i][1] = y
        femlist[i][3] = vx
        femlist[i][4] = vy
        femlist[i][0] += vx
        femlist[i][1] += vy
        draw_sfemale(x, y, r)

    for i in range(numball):
        x = list_of_balls[i][0]
        y = list_of_balls[i][1]
        r = list_of_balls[i][2]
        color = list_of_balls[i][3]
        vx = list_of_balls[i][4]
        vy = list_of_balls[i][5]
        if x - r <= 0 or x + r >= sizeX:
            vx *= -1
            if x - r <= 0:
                x += vx // 2
            else:
                x -= vx // 2
        if y - r <= 0 or y + r >= sizeY:
            vy *= -1
            if y - r <= 0:
                y += vy // 2
            else:
                y -= vy // 2

        list_of_balls[i][4] = vx
        list_of_balls[i][5] = vy
        list_of_balls[i][0] += list_of_balls[i][4]
        list_of_balls[i][1] += list_of_balls[i][5]
        circle(screen, COLORS[color], (x, y), r)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            check = False
            for i in range(numball):
                x0 = list_of_balls[i][0]
                y0 = list_of_balls[i][1]
                r = list_of_balls[i][2]
                if (x - x0)**2 + (y - y0)**2 < r**2:
                    ballmaster(i)
                    score += int((100 - r) // 10)
                    check = True

            for i in range(numfem):
                x0 = femlist[i][0]
                y0 = femlist[i][1]
                r = femlist[i][2]
                if (x - x0)**2 + (y - y0)**2 < 9 * r**2:
                    femmaster(i)
                    score += int((100 - r) // 10)
                    check = True

            if check:
                print(':з')
            else:
                print(':<')

    text = shrift.render("score:" + str(score), 1, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.update()

pygame.quit()