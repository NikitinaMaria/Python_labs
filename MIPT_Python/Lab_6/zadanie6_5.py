from typing import List, Any, Union, Tuple

import pygame
from pygame.draw import *
from random import randint
import numpy as np
import random

pygame.init()

screen_size_x = 1200
screen_size_y = 800

FPS = 50
screen = pygame.display.set_mode((screen_size_x, screen_size_y))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

count_of_balls = 10
balls_parameters = []


def new_ball():
    """
    The function sets parameters of a new random ball
    """
    ball_x = randint(100, screen_size_x - 100)
    ball_y = randint(100, screen_size_y - 100)
    ball_r = randint(20, 70)
    speed_x = randint(-10, 10)
    speed_y = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    ball_parameters = [ball_x, ball_y, ball_r, speed_x, speed_y, color]
    return ball_parameters


def draw_new_ball(ball_x, ball_y, ball_r, speed_x, speed_y, color):
    """
    The function draws a new random ball
    """
    circle(screen, color, (ball_x, ball_y), ball_r)


def balls_move(ball_x, ball_y, ball_r, speed_x, speed_y, color):
    """
    The function makes the ball move
    """
    circle(screen, BLACK, (ball_x, ball_y), ball_r)
    ball_x += speed_x
    ball_y += speed_y
    if ball_x <= 0:
        ball_x = 0
        speed_x = - speed_x
    if ball_y <= 0:
        ball_y = 0
        speed_y = - speed_y
    if ball_x >= screen_size_x:
        ball_x = screen_size_x
        speed_x = - speed_x
    if ball_y >= screen_size_y:
        ball_y = screen_size_y
        speed_y = - speed_y
    circle(screen, color, (ball_x, ball_y), ball_r)
    ball_parameters = [ball_x, ball_y, ball_r, speed_x, speed_y, color]
    return ball_parameters


def delete_ball(ball_x, ball_y, ball_r, speed_x, speed_y, color):
    """
    The function deletes the ball
    """
    ball_parameters = [ball_x, ball_y, ball_r, speed_x, speed_y, color]
    if ball_parameters in balls_parameters:
        circle(screen, BLACK, (ball_x, ball_y), ball_r)
        balls_parameters.remove(ball_parameters)
    return balls_parameters


def draw_points(points):
    """
    The function counts points
    """
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Points = ' + str(points), True, GREEN, RED)
    textRect = text.get_rect()
    textRect.center = (screen_size_x * 12 // 13, 50)
    screen.blit(text, textRect)


def click(ball_x, ball_y, ball_r, speed_x, speed_y, color, k, points):
    """
    The function checks if we are in a ball
    :param ball_x: ball coordinate x
    :param ball_y: ball coordinate y
    :param ball_r: ball radius
    """

    # Coordinates of the mouse
    mouse_x, mouse_y = event.pos

    # Distance from mouse to ball center
    distance_ball = np.sqrt((ball_x - mouse_x) * (ball_x - mouse_x) + (ball_y - mouse_y) * (ball_y - mouse_y))

    # Check if we are in a ball and count points
    if distance_ball <= ball_r:
        points += 1
        draw_points(points)
        parameters_for_delete[k] = [ball_x, ball_y, ball_r, speed_x, speed_y, color]

    return parameters_for_delete, points

# Adding the first balls
for i in range(count_of_balls):
    parameters_of_one_ball = new_ball()
    balls_parameters.append(parameters_of_one_ball)
    draw_new_ball(*parameters_of_one_ball)

parameters_for_delete = [[0] * 6] * count_of_balls
points = 0

# Writing the starting points
draw_points(points)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for k in range(count_of_balls):
                # We check whether we hit the ball
                parameters_for_delete, points = click(*balls_parameters[k], k, points)
                
    # Remove the balls that hit and add new ones
    for i in range(count_of_balls):
        balls_parameters = delete_ball(*parameters_for_delete[i])
        if len(balls_parameters) < count_of_balls:
            parameters_of_one_ball = new_ball()
            balls_parameters.append(parameters_of_one_ball)
            draw_new_ball(*parameters_of_one_ball)
    
    # Moving the balls
    for i in range(count_of_balls):
        balls_parameters[i] = balls_move(*balls_parameters[i])
    
    # Updating points
    draw_points(points)
    pygame.display.update()

pygame.quit()
