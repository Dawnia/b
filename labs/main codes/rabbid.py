import pygame
from math import pi
from pygame.draw import *
pygame.init()

sizeX = 400
sizeY = 400
FPS = 30

screen = pygame.display.set_mode((sizeX, sizeY))
screen.fill((255, 255, 255))

def eye(x, y):
    """
    draws an eye watching right
    :param x: x-coord of the rect which the eye in
    :param y: y-coord of the rect which the eye in
    :return: none
    """
    ellipse(screen, (255, 255, 255), [(x, y), (12, 16)])
    circle(screen, (0, 0, 0), (x + 8, y + 8), 4)


def nose(x, y):
    """
    draws a nose
    :param x: x-coord of nose' center
    :param y: y-coord of nose' center
    :return: none
    """
    polygon(screen, (200, 150, 150), [(x - 7, y + 15), (x + 7, y + 15), (x, y + 25)])


def hear(x, y, orientation):
    """
    draws a right of left hear
    :param x: x-coord of the rect which the hear in
    :param y: y-coord of the rect which the hear in
    :param orientation: defines if it is a left ('l') or right ('r') hear
    :return: none
    """
    if orientation == 'l':
        ellipse(screen, (100, 20, 20), [(x, y), (20, 85)])
        ellipse(screen, (200, 150, 150), [(x + 7, y + 10), (10, 70)])

    if orientation == 'r':
        ellipse(screen, (100, 20, 20), [(x, y), (20, 85)])
        ellipse(screen, (200, 150, 150), [(x + 3, y + 10), (10, 70)])


def head(x, y):
    '''
    draws a head of a rabbit in the specified coordinates of center
    :param x: x-coordinate of the center
    :param y: y-coordinate of the center
    :return: none
    '''
    arc(screen, (100, 20, 20), [(x - 25, y - 50), (50, 100)], pi, 2*pi, 25)
    arc(screen, (100, 20, 20), [(x - 25, y - 20), (50, 40)], 0, pi, 20)
    rect(screen, (100, 20, 20), [(x - 10, y), (20, 30)])

    eye(x - 15, y - 5)
    eye(x + 5, y - 5)
    nose(x, y)
    hear(x - 22, y - 95, 'l')
    hear(x + 2, y - 95, 'r')


def hand(x, y, orientation):
    """
    draws a hand
    :param x: x-coordinate of the shoulder
    :param y: y-coordinate of the shoulder
    :param orientation: if this hand is right ('r') or left ('l')
    :return: none
    """
    if orientation == 'l':
        lines(screen, (0, 0, 0), False, [(x, y), (x - 60, y + 35), (x - 15, y + 75)], 5)
        line(screen, (0, 0, 0), (x - 15, y + 75), (x - 30, y + 85), 3)
        line(screen, (0, 0, 0), (x - 15, y + 75), (x - 20, y + 90), 3)
        line(screen, (0, 0, 0), (x - 15, y + 75), (x - 25, y + 88), 3)

    if orientation == 'r':
        lines(screen, (0, 0, 0), False, [(x, y), (x + 60, y + 35), (x + 15, y + 75)], 5)
        line(screen, (0, 0, 0), (x + 15, y + 75), (x + 30, y + 85), 3)
        line(screen, (0, 0, 0), (x + 15, y + 75), (x + 20, y + 90), 3)
        line(screen, (0, 0, 0), (x + 15, y + 75), (x + 25, y + 88), 3)


def leg(x, y):
    """
    draws a leg
    :param x: x-coordinate of the rect which the leg in
    :param y: y-coordinate of the rect which the leg in
    :return: none
    """
    ellipse(screen, (200, 140, 140), [(x, y), (60, 45)])


def main_body(x, y):
    '''
    draws a body
    :param x: x-coord of a center of a body
    :param y: y-coord of a center of a body
    :return: none
    '''
    ellipse(screen, (150, 100, 100), [(x - 50, y - 90), (100, 180)])
    polygon(screen, (200, 200, 200), [(x - 5, y - 50), (x + 5, y - 50), (x, y + 10)])

    hand(x - 30, y - 65, 'l')
    hand(x + 30, y - 65, 'r')

    leg(x - 65, y + 70)
    leg(x + 5, y + 70)


main_body(200, 230)
head(200, 110)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
