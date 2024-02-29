import pygame
from pygame.draw import *
from random import randint
import numpy as np
import random

pygame.init()

screen_size_x = 1200
screen_size_y = 800

FPS = 50

# The main screen
screen = pygame.display.set_mode((screen_size_x, screen_size_y))

# Font for creating some writings in the game
font = pygame.font.Font('freesansbold.ttf', 50)

# Needs for quit button, which will appear after the game
quit_button = pygame.font.Font('freesansbold.ttf', 50)

# Needs for save button, which will appear after the game
save_button = pygame.font.Font('freesansbold.ttf', 50)

restart_button = pygame.font.Font('freesansbold.ttf', 32)

# Open file with results
winners_file = open('Winners.txt', 'a')

# Colors and list of the colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Balls
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
        balls_parameters.remove(ball_parameters)
    return balls_parameters


def click(ball_x, ball_y, ball_r, speed_x, speed_y, color, k, points):
    """
    The function checks if we are in a ball
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


# Unicorns
count_of_unicorns = 3
unicorns_parameters = []

random.seed(8968)
screen_unicorn = pygame.Surface((600, 800), pygame.SRCALPHA, 32)
screen_unicorn_2 = pygame.Surface((600, 800), pygame.SRCALPHA, 32)
screen_ellipse = pygame.Surface((600, 800), pygame.SRCALPHA, 32)


def unicorn():
    '''
    Function draws unicorn on a separate screen
    '''

    pink = (233, 175, 175)
    light_pink = (233, 198, 175)
    light_blue = (175, 233, 221)
    cream = (255, 238, 170)
    light_green = (229, 255, 128)
    colors_of_unicorn = pink, light_blue, light_pink, light_green, cream
    white = (255, 255, 255)

    # Tail
    for i in range(25):
        ellipse(screen_unicorn, colors_of_unicorn[randint(0, 4)], (
            randint(288 - i * 4, 290 - i * 2), randint(580 + i * 5, 605 + i * 5), randint(30, 45 + 3 * i // 2),
            randint(12, 27)))
    # Body
    ellipse(screen_unicorn, white, (440, 470, 80, 60))
    ellipse(screen_unicorn, white, (470, 490, 80, 40))
    ellipse(screen_unicorn, white, (290, 565, 225, 110))
    rect(screen_unicorn, white, (445, 500, 60, 120))
    # Legs
    rect(screen_unicorn, white, (305, 635, 18, 110))
    rect(screen_unicorn, white, (347, 635, 22, 100))
    rect(screen_unicorn, white, (430, 635, 20, 120))
    rect(screen_unicorn, white, (480, 635, 16, 95))
    # Eye
    ellipse(screen_unicorn, (229, 128, 255), (475, 485, 23, 20))
    ellipse(screen_unicorn, (34, 28, 36), (485, 490, 9, 9))
    ellipse(screen_ellipse, white, (200, 320, 12, 7))
    # Horn
    polygon(screen_unicorn, (233, 175, 175), ([(485, 390), (485, 475), (465, 473), (485, 390)]))
    # Mane
    for i in range(14):
        ellipse(screen_unicorn, colors_of_unicorn[randint(0, 4)], (
            randint(438 - i * 7, 440 - i * 2), randint(460 + i * 8, 474 + i * 7), randint(30, 45 + 3 * i // 2),
            randint(15, 30)))

    # Speck
    screen_ellipse_2 = pygame.transform.rotate(screen_ellipse, 135)
    screen_unicorn.blit(pygame.transform.scale(screen_ellipse_2, screen_unicorn.get_rect().size), (177, -8))


unicorn()


def new_unicorn():
    '''
    The function sets parameters of a new random unicorn
    '''
    unicorn_x = randint(-200, screen_size_x - 300)
    unicorn_y = randint(-200, screen_size_y - 300)
    unicorn_size = randint(20, 70)
    speed_unicorn_x = randint(-10, 10)
    speed_unicorn_y = randint(-10, 10)
    unicorn_parameters = [unicorn_x, unicorn_y, unicorn_size, speed_unicorn_x, speed_unicorn_y]
    return unicorn_parameters


def draw_new_unicorn(unicorn_x, unicorn_y, unicorn_size, speed_unicorn_x, speed_unicorn_y):
    """
    The function draws a new random unicorn
    """
    screen.blit(pygame.transform.scale(screen_unicorn, (6 * unicorn_size, 8 * unicorn_size)),
                (unicorn_x, unicorn_y))


def unicorns_move(unicorn_x, unicorn_y, unicorn_size, speed_unicorn_x, speed_unicorn_y):
    """
    The function function makes unicorns move
    """
    unicorn_x += speed_unicorn_x
    unicorn_y += speed_unicorn_y
    if unicorn_x <= 0:
        unicorn_x = 0
        speed_unicorn_x = - speed_unicorn_x
    if unicorn_y <= -200:
        unicorn_y = -200
        speed_unicorn_y = - speed_unicorn_y
    if unicorn_x >= screen_size_x - 200:
        unicorn_x = screen_size_x - 200
        speed_unicorn_x = - speed_unicorn_x
    if unicorn_y >= screen_size_y - 200:
        unicorn_y = screen_size_y - 200
        speed_unicorn_y = - speed_unicorn_y
    unicorn_parameters = [unicorn_x, unicorn_y, unicorn_size, speed_unicorn_x, speed_unicorn_y]
    screen.blit(pygame.transform.scale(screen_unicorn, (6 * unicorn_size, 8 * unicorn_size)),
                (unicorn_x, unicorn_y))
    return unicorn_parameters


def click_unicorn(unicorn_x, unicorn_y, unicorn_size, speed_unicorn_x, speed_unicorn_y, k, points):
    """
    The function checks if we are in a unicorn
    """

    # Coordinates of the mouse
    mouse_x, mouse_y = event.pos

    if (unicorn_x + 2 * unicorn_size < mouse_x) and (unicorn_x + 6 * unicorn_size > mouse_x) and \
            (unicorn_y + (39 * unicorn_size) // 10 < mouse_y) and (unicorn_y + (77 * unicorn_size) // 10 > mouse_y):
        points -= 5
        draw_points(points)
        parameters_for_delete_unicorn[k] = [unicorn_x, unicorn_y, unicorn_size, speed_unicorn_x, speed_unicorn_y]

    return parameters_for_delete_unicorn, points


def delete_unicorn(unicorn_x, unicorn_y, unicorn_size, speed_unicorn_x, speed_unicorn_y):
    """
    The function deletes the unicorn
    """
    unicorn_parameters = [unicorn_x, unicorn_y, unicorn_size, speed_unicorn_x, speed_unicorn_y]
    if unicorn_parameters in unicorns_parameters:
        unicorns_parameters.remove(unicorn_parameters)
    return unicorns_parameters


# Other functions
def draw_points(points):
    """
    The function counts points
    """
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Points = ' + str(points), True, GREEN, RED)
    textRect = text.get_rect()
    textRect.center = (screen_size_x * 12 // 13, 50)
    screen.blit(text, textRect)


def button(font, text, x, y, color):
    """
    The function adds a field with text
    """
    textrun = font.render(text, True, RED, color)
    textRect = textrun.get_rect()
    textRect.center = (x, y)
    screen.blit(textrun, textRect)


def sort():
    """
    The function sorts the rating of players
    """

    # Reading data from the file
    with open('Winners.txt', 'r') as winners_file_read:
        winners = winners_file_read.read().splitlines()
    winners_file_read.close()

    # The numerical values of the points of players
    winners_points = [0] * len(winners)

    # Creating a list of rating lines and player points
    for i in range(len(winners)):
        a, b = winners[i].split()
        winners_points[i] = int(b)
        winners[i] = (winners[i], winners_points[i])

    # Sorting this list
    winners_sorted = sorted(winners, key=lambda winner: winner[1], reverse=True)

    # Write the sorted list to a file
    with open('Winners.txt', 'w') as winners_file_sort:
        for player in winners_sorted:
            player_1, player_2 = player
            winners_file_sort.write(player_1 + '\n')
    winners_file_sort.close()


# Adding the first balls
for i in range(count_of_balls):
    parameters_of_one_ball = new_ball()
    balls_parameters.append(parameters_of_one_ball)
    draw_new_ball(*parameters_of_one_ball)

# Adding the first unicorns
for i in range(count_of_unicorns):
    parameters_of_one_unicorn = new_unicorn()
    unicorns_parameters.append(parameters_of_one_unicorn)
    draw_new_unicorn(*parameters_of_one_unicorn)

# Lists of removal targets
parameters_for_delete = [[0] * 6] * count_of_balls
parameters_for_delete_unicorn = [[0] * 5] * count_of_unicorns

# Player account
points = 0
draw_points(points)

clock = pygame.time.Clock()
finished = False
finished_game = False

pygame.display.update()
player_name = ''

# Game time
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for k in range(count_of_balls):
                parameters_for_delete, points = click(*balls_parameters[k], k, points)
            for k in range(count_of_unicorns):
                parameters_for_delete_unicorn, points = click_unicorn(*unicorns_parameters[k], k, points)

    screen.fill(BLACK)

    # Remove the balls that hit and add new ones
    for i in range(count_of_balls):
        balls_parameters = delete_ball(*parameters_for_delete[i])
        if len(balls_parameters) < count_of_balls:
            parameters_of_one_ball = new_ball()
            balls_parameters.append(parameters_of_one_ball)
            draw_new_ball(*parameters_of_one_ball)

    # Remove the unicorns that hit and add new ones
    for i in range(count_of_unicorns):
        unicorns_parameters = delete_unicorn(*parameters_for_delete_unicorn[i])
        if len(unicorns_parameters) < count_of_unicorns:
            parameters_of_one_unicorn = new_unicorn()
            unicorns_parameters.append(parameters_of_one_unicorn)
            draw_new_unicorn(*parameters_of_one_unicorn)

    # Move unicorns
    for i in range(count_of_unicorns):
        unicorns_parameters[i] = unicorns_move(*unicorns_parameters[i])

    # Move balls
    for i in range(count_of_balls):
        balls_parameters[i] = balls_move(*balls_parameters[i])

    draw_points(points)
    pygame.display.update()

screen.fill(CYAN)
finished = False

# Start of the game
screen.fill(CYAN)
button(font, 'Please, write your nickname,', screen_size_x // 2, screen_size_y // 3, CYAN)
button(font, 'Click Enter when you are ready', screen_size_x // 2, screen_size_y // 3 + 200, CYAN)

# Field to enter the name
rect(screen, BLACK, (screen_size_x // 3, screen_size_y // 2 - 70, screen_size_x // 3, 70))
button(font, '', screen_size_x // 2, screen_size_y // 2 - 35, RED)

# Reading the player name
while not finished:
    for event in pygame.event.get():

        # Exiting the game
        if event.type == pygame.QUIT:
            finished = True
            finished_game = True

        if event.type == pygame.KEYDOWN:
            # If the Enter is pressed
            if event.key == pygame.K_RETURN:
                finished = True

            # If the Backspace is pressed
            elif event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
                rect(screen, BLACK, (screen_size_x // 3, screen_size_y // 2 - 70, screen_size_x // 3, 70))

            else:
                player_name += event.unicode

        button(font, player_name, screen_size_x // 2, screen_size_y // 2 - 35, BLACK)
        pygame.display.update()

screen.fill(CYAN)
if not finished_game:
    finished = False

# Quit button
button(quit_button, 'I want to quit of the game', screen_size_x // 2, 200, GREEN)

# Save result button
button(save_button, 'I want to save my result', screen_size_x // 2, 400, YELLOW)

# Save and quit
while not finished:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # If player exits the game
            if (mouse_x >= screen_size_x // 2 - 400) and (mouse_x <= screen_size_x // 2 + 400) and (mouse_y >= 180) and \
                    (mouse_y <= 220):
                finished = True

            # If saving
            if (mouse_x >= screen_size_x // 2 - 400) and (mouse_x <= screen_size_x // 2 + 400) and (mouse_y >= 380) and \
                    (mouse_y <= 420):
                button(save_button, 'Successfuly saved', screen_size_x // 2, 600, BLACK)
                winners_file.write(player_name + ': ' + str(points) + '\n')

winners_file.close()

sort()

pygame.quit()
