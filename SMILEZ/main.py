import pygame
from pygame.draw import *

pygame.init()

sizeX = 500
sizeY = 500
r = 50
n = 3
x0 = 100
y0 = 100

FPS = 30

screen = pygame.display.set_mode((sizeX, sizeY))

rect(screen, (255, 255, 255), (0, 0, sizeX, sizeY))

def smile1(x, y):
    k = r // 25

    circle(screen, (250, 200, 0), (x, y), r)
    rect(screen, (50, 50, 50), (x - 3 * k, y, 6 * k, 6 * k))
    circle(screen, (250, 0, 0), (x - 10 * k, y - 5 * k), r // 5)
    circle(screen, (250, 0, 0), (x + 10 * k, y - 5 * k), r // 5)
    circle(screen, (0, 0, 0), (x - 10 * k, y - 5 * k), r // 25)
    circle(screen, (0, 0, 0), (x + 10 * k, y - 5 * k), r // 25)
    rect(screen, (0, 0, 0), (x - 8 * k, y + 9 * k, 16 * k, 3 * k))
    polygon(screen, (0, 0, 0), [(x - 15 * k, y - 13 * k),
                                (x - 1 * k, y - 10 * k),
                                (x - 2 * k, y - 4 * k),
                                (x - 14 * k, y - 12 * k)])
    polygon(screen, (0, 0, 0), [(x + 15 * k, y - 13 * k),
                                (x + 1 * k, y - 10 * k),
                                (x + 2 * k, y - 4 * k),
                                (x + 14 * k, y - 12 * k)])


def smile2(x, y):
    k = r // 25

    circle(screen, (250, 200, 0), (x, y), r * 3 // 2)
    polygon(screen, (0, 0, 0), [(x - 3 * k, y), (x + 3 * k, y), (x, y + 3 * k)])
    circle(screen, (250, 0, 0), (x - 10 * k, y - 5 * k), r // 5)
    circle(screen, (250, 0, 0), (x + 10 * k, y - 5 * k), r // 5)
    circle(screen, (0, 0, 0), (x - 10 * k, y - 5 * k), r // 25)
    circle(screen, (0, 0, 0), (x + 10 * k, y - 5 * k), r // 25)
    rect(screen, (0, 0, 0), (x - 8 * k, y + 9 * k, 16 * k, 3 * k))
    polygon(screen, (0, 0, 0), [(x - 15 * k, y - 13 * k),
                                (x - 1 * k, y - 10 * k),
                                (x - 2 * k, y - 4 * k),
                                (x - 14 * k, y - 12 * k)])
    polygon(screen, (0, 0, 0), [(x + 15 * k, y - 13 * k),
                                (x + 1 * k, y - 10 * k),
                                (x + 2 * k, y - 4 * k),
                                (x + 14 * k, y - 12 * k)])


for i in range(n):
    for j in range(n):
        if (i*n + j) % 2:
            smile2(x0 + r * 3 * j, y0 + r * 3 * i)
        else:
            smile1(x0 + r * 3 * j, y0 + r * 3 * i)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()