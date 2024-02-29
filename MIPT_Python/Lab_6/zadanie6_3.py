import pygame
from pygame.draw import *
from random import randint
import numpy as np

pygame.init()

FPS = 20
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
    global ball_x, ball_y, ball_r, color, speed_x, speed_y
    ball_x = randint(100, 1100)
    ball_y = randint(100, 700)
    ball_r = randint(30, 100)
    speed_x = randint(-20, 20)
    speed_y = randint(-20, 20)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (ball_x, ball_y), ball_r)


def ball_move():
    """
    The function function makes the ball move
    """

    global ball_x, ball_y, ball_r, speed_x, speed_y, color
    ball_x += speed_x
    if ball_x <= 0:
        ball_x = 0
        speed_x = - speed_x
    ball_y += speed_y
    if ball_y <= 0:
        ball_y = 0
        speed_y = - speed_y
    if ball_x >= 1200:
        ball_x = 1200
        speed_x = - speed_x
    ball_y += speed_y
    if ball_y >= 800:
        ball_y = 800
        speed_y = - speed_y
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
    distance = np.sqrt((ball_x - mouse_x) * (ball_x - mouse_x) + (ball_y - mouse_y) * (ball_y - mouse_y))

    # Check if we are in a ball and count points
    global points
    if distance <= ball_r:
        print('True')
        points += 1
    else:
        print('False')
    print(points)


# Ball lifetime
round_time = 49


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    round_time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(ball_x, ball_y, ball_r)
    pygame.display.update()
    screen.fill(BLACK)
    if round_time == 50:
        round_time = 0
        new_ball()
    else:
        ball_move()




pygame.quit()
