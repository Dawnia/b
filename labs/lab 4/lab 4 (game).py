import pygame
from pygame.draw import *
from random import randint
from math import sqrt
pygame.init()

shrift = pygame.font.SysFont('serif', 30)
scorelist = 'C:\\Users\\Данила\\Documents\\праки\\results of the game.txt'

FPS = 30
sizeX = 800
sizeY = 500
numball = 10
numfem = 2
vmax = 10
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
    list_of_balls[i][2] = randint(10, 50)                                           #radius
    list_of_balls[i][0] = randint(list_of_balls[i][2], sizeX - list_of_balls[i][2]) #x-coord
    list_of_balls[i][1] = randint(list_of_balls[i][2], sizeY - list_of_balls[i][2]) #y-coord
    list_of_balls[i][3] = randint(0, 5)                                             #color
    list_of_balls[i][4] = randint(-1 * vmax, vmax)                                  #v_x
    vx = list_of_balls[i][4]
    vy_max = int(sqrt(vmax ** 2 - vx ** 2))
    list_of_balls[i][5] = randint(-1 * vy_max, vy_max)                              #v_y


for i in range(numball):
    ballmaster(i)

pygame.display.update()
clock = pygame.time.Clock()
score = 0
time_0 = pygame.time.get_ticks()
pause_time = time_0
time = 0
start_of_pause = 0
end_of_pause = 0
time1 = 0
finished = False
pause = 1

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

        if y - 2 * r <= 0 or y + 11 * r >= sizeY:
            vy *= -1
            if y - 2 * r <= 0:
                y += r // 2
            else:
                y -= r // 2

        femlist[i][0] = x
        femlist[i][1] = y
        femlist[i][3] = vx
        femlist[i][4] = vy
        femlist[i][0] += vx * pause
        femlist[i][1] += vy * pause
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
        list_of_balls[i][0] += list_of_balls[i][4] * pause
        list_of_balls[i][1] += list_of_balls[i][5] * pause
        circle(screen, COLORS[color], (x, y), r)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('aga')
                if pause == 0:
                    print('aga')
                    pause = 1
                    end_of_pause = pygame.time.get_ticks()
                    pause_time += end_of_pause - start_of_pause
                else:
                    print('aga')
                    start_of_pause = pygame.time.get_ticks()
                    pause = 0
                    time1 = time

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            check = 0
            for i in range(numball):
                x0 = list_of_balls[i][0]
                y0 = list_of_balls[i][1]
                r = list_of_balls[i][2]
                vx = list_of_balls[i][4]
                vy = list_of_balls[i][5]
                v = sqrt(vx**2 + vy**2)
                if (x - x0)**2 + (y - y0)**2 < r**2:
                    ballmaster(i)
                    score += int((100 - r) / 10 * v)
                    check += 1

            for i in range(numfem):
                x0 = femlist[i][0]
                y0 = femlist[i][1]
                r = femlist[i][2]
                vx = femlist[i][3]
                vy = femlist[i][4]
                v = sqrt(vx ** 2 + vy ** 2)
                head = (x - x0)**2 + (y - y0)**2 < 9 * r**2
                v1 = (x - x0) * 8 - (y - y0) * 3 < 0
                v2 = y < y0 + 8 * r
                v3 = (x - x0) * 8 + (y - y0) * 3 > 0
                body = v1 and v2 and v3
                if head or body:
                    femmaster(i)
                    score += int((120 - r) / 10 * v)
                    check += 1

            if check > 0:
                print(':з')
                score *= sqrt(check)
                score = int(score)
            else:
                print(':<')
                score -= 15

    time_m = pygame.time.get_ticks() - pause_time
    time = time_m // 1000
    if score < 0:
        score = 0
    text1 = shrift.render("score: " + str(score), 1, (0, 0, 0))
    if pause == 0:
        text2 = shrift.render("time: " + str(time1), 1, (0, 0, 0))
    else:
        text2 = shrift.render("time: " + str(time), 1, (0, 0, 0))

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))
    pygame.display.update()

strings_count = 1
input = open(scorelist, 'r')
for i in input:
    strings_count += 1

input = open(scorelist, 'a')
input.write(str(strings_count) + ". Score: " + str(score) + ", time: " + str(time) + '\n')
pygame.quit()