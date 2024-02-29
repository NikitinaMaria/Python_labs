import pygame
from pygame.draw import *
from random import randint
import numpy as np

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """
    The function draws a new random ball in a random place
    """
    global ball_x, ball_y, ball_r
    ball_x = randint(100, 1100)
    ball_y = randint(100, 700)
    ball_r = randint(30, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (ball_x, ball_y), ball_r)


points = 0


def click(ball_x, ball_y, ball_r):
    """
    The function checks if we are in a ball and counts points
    :param ball_x: ball coordinate x
    :param ball_y: ball coordinate y
    :param ball_r: ball radius
    """

    # Coordinates of the mouse
    mouse_x, mouse_y = event.pos

    # Distance from mouse to ball center
    distance = np.sqrt((ball_x - mouse_x) ** 2 + (ball_y - mouse_y) ** 2)

    # Check if we are in a ball and count points
    global points
    if distance <= ball_r:
        print('True')
        points += 1

    else:
        print('False')
    print(points)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(ball_x, ball_y, ball_r)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
