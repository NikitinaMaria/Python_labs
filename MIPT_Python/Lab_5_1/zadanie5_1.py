import pygame
from pygame.draw import *
from math import pi

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

grass_green = (55, 200, 113)
sky_blue = (95, 188, 211)
white = (255, 255, 255)
black = (0, 0, 0)
fence_color = (200, 171, 55)
dog_color = (108, 103, 83)
dark = (40, 39, 31)
house_color = (200, 171, 55)
roof_color = (212, 170, 0)


def draw_grass():
    """
    Function drawing grass
    """

    rect(screen, grass_green, (0, 250, 600, 600))


def draw_sky():
    """
    Function drawing sky
    """

    rect(screen, sky_blue, (0, 0, 600, 300))


def fence(x1=0, y1=100, x2=400, y2=350):

    """
    Function draws fence
    :param x1, y1: coordinates of the upper left corner
    :param x2, y2: coordinates of the bottom right corner
    """

    number_of_fence_boards = 20

    # Bottom fence line
    line(screen, black, (x1, y2), (x2, y2))

    # Fence background
    rect(screen, fence_color, (x1, y1, x2 - x1, y2 - y1))

    # Lines on the fence
    board_thickness = (x2 - x1) // number_of_fence_boards
    x = x1 + board_thickness
    for i in range(number_of_fence_boards - 1):
        line(screen, black, (x, y1), (x, y2))
        x += board_thickness


def body(n, x, y):

    """
    Function draws dog body
    :param n: the size of the dog (if it is negative, then dog is mirrored)
    :param x, y: coordinates of the dog (edge of muzzle)
    """

    # Chest
    ellipse(screen, dog_color,
            (round(x + 75 * n - 55 * abs(n)), round(y + 25 * abs(n)), round(110 * abs(n)), round(60 * abs(n))))

    # Back
    ellipse(screen, dog_color,
            (round(x + 115 * n - 35 * abs(n)), round(y + 18 * abs(n)), round(70 * abs(n)), round(40 * abs(n))))

    # Leg_1
    ellipse(screen, dog_color,
            (round(x + 65 * n - 15 * abs(n)), round(y + 45 * abs(n)), round(30 * abs(n)), round(70 * abs(n))))

    # leg_2
    ellipse(screen, dog_color,
            (round(x + 25 * n - 15 * abs(n)), round(y + 35 * abs(n)), round(30 * abs(n)), round(70 * abs(n))))

    # Foot_1
    ellipse(screen, dog_color,
            (round(x + 55 * n - 15 * abs(n)), round(y + 110 * abs(n)), round(30 * abs(n)), round(15 * abs(n))))

    # Foot_2
    ellipse(screen, dog_color,
            (round(x + 15 * n - 15 * abs(n)), round(y + 100 * abs(n)), round(30 * abs(n)), round(15 * abs(n))))

    # Thigh_1
    circle(screen, dog_color, (round(x + int(100 * n)), round(y + int(35 * abs(n)))), round(int(20 * abs(n))))

    # Thigh_2
    circle(screen, dog_color, (round((x + int(145 * n))), round(y + int(60 * abs(n)))),
           round(int(20 * abs(n))))

    # Leg_3
    ellipse(screen, dog_color,
            (round(x + 118 * n - 8 * abs(n)), round(y + 45 * abs(n)), round(16 * abs(n)), round(50 * abs(n))))

    # Leg_4
    ellipse(screen, dog_color,
            (round(x + 158 * n - 8 * abs(n)), round(y + 70 * abs(n)), round(16 * abs(n)), round(40 * abs(n))))

    # Foot_3
    ellipse(screen, dog_color,
            (round(x + 110 * n - 10 * abs(n)), round(y + 90 * abs(n)), round(20 * abs(n)), round(10 * abs(n))))

    # Foot_4
    ellipse(screen, dog_color,
            (round(x + 150 * n - 10 * abs(n)), round(y + 105 * abs(n)), round(20 * abs(n)), round(10 * abs(n))))


def ears(n, x, y):

    """
    Function draws dog ears
    :param n: the size of the dog (if it is negative, then dog is mirrored)
    :param x, y: coordinates of the dog (edge of muzzle)
    """
    # bhs - base head size
    bhs = 56

    # Size of the ears
    ear_size_x = bhs / 5
    ear_size_y = bhs / 3

    # Draw ear1
    ellipse(screen, dog_color, (round(x - ear_size_x / 2 * abs(n)), y, round(ear_size_x * abs(n)),
                                round(ear_size_y * abs(n))))
    ellipse(screen, dark, (round(x - ear_size_x / 2 * abs(n)), y, round(ear_size_x * abs(n)),
                           round(ear_size_y * abs(n))), 2)

    # Draw ear2
    ellipse(screen, dog_color, (round(x + bhs * n - ear_size_x / 2 * abs(n)), y, round(ear_size_x * abs(n)),
                                round(ear_size_y * abs(n))))
    ellipse(screen, dark, (round(x + bhs * n - ear_size_x / 2 * abs(n)), y, round(ear_size_x * abs(n)),
                           round(ear_size_y * abs(n))), 2)


def eyes(n, x, y):

    """
    Function draws dog eyes
    :param n: the size of the dog (if it is negative, then dog is mirrored)
    :param x, y: coordinates of the dog (edge of muzzle)
    """

    # bhs - base head size
    bhs = 56

    # Size of the eyes
    eye_size_x = bhs / 4
    eye_size_y = bhs / 8

    # Draw eye1
    ellipse(screen, white, (round(x + (bhs / 8 + eye_size_x / 2) * n - eye_size_x / 2 * abs(n)),
                            round(y + bhs / 4 * abs(n)), round(eye_size_x * abs(n)), round(eye_size_y * abs(n))))
    ellipse(screen, dark, (round(x + (bhs / 8 + eye_size_x / 2) * n - eye_size_x / 2 * abs(n)),
                           round(y + bhs / 4 * abs(n)), round(eye_size_x * abs(n)), round(eye_size_y * abs(n))), 1)
    circle(screen, black, (x + int(bhs / 4 * n), y + int(5 * bhs / 16 * abs(n))), int(bhs / 16 * abs(n)))

    # Draw eye2
    ellipse(screen, white, (round(x + (5 * bhs / 8 + eye_size_x / 2) * n - eye_size_x / 2 * abs(n)),
                            round(y + bhs / 4 * abs(n)), round(eye_size_x * abs(n)), round(eye_size_y * abs(n))))
    ellipse(screen, dark, (round(x + (5 * bhs / 8 + eye_size_x / 2) * n - eye_size_x / 2 * abs(n)),
                           round(y + bhs / 4 * abs(n)), round(eye_size_x * abs(n)), round(eye_size_y * abs(n))), 1)
    circle(screen, black, (x + int(3 * bhs / 4 * n), y + int(5 * bhs / 16 * abs(n))), int(bhs / 16 * abs(n)))


def mouth(n, x, y):

    """
    Function draws dog mouth
    :param n: the size of the dog (if it is negative, then dog is mirrored)
    :param x, y: coordinates of the dog (edge of muzzle)
    """

    # bhs - base head size
    bhs = 56

    # Arc of the mouth
    angle = pi / 16
    end_angle = pi

    # Size of the mouth
    mouth_size = bhs / 3

    arc(screen, black, (round(x + (bhs / 4 + 0.75 * mouth_size) * n - 0.75 * mouth_size * abs(n)),
                        round(y + 3 * bhs / 4 * abs(n)), round(1.5 * mouth_size * abs(n)), round(mouth_size * abs(n))),
        angle, end_angle)

    # Draw teeth
    polygon(screen, white, [(round(x + bhs / 3 * n), round(y + 4 * bhs / 5 * abs(n))),
                            (round(x + bhs / 3 * n), round(y + 7 * bhs / 10 * abs(n))),
                            (round(x + 7 * bhs / 18 * n), round(y + 15 * bhs / 20 * abs(n)))])
    polygon(screen, white, [(round(x + (bhs - bhs / 3) * n), round(y + 4 * bhs / 5 * abs(n))),
                            (round(x + (bhs - bhs / 3) * n), round(y + 7 * bhs / 10 * abs(n))),
                            (round(x + (bhs - 7 * bhs / 18) * n), round(y + 15 * bhs / 20 * abs(n)))])


def head(n, x, y):

    """
    Function draws dog head
    :param n: the size of the dog (if it is negative, then dog is mirrored)
    :param x, y: coordinates of the dog (edge of muzzle)
    """

    # bhs - base head size
    bhs = 56

    # Draw head
    rect(screen, dog_color, (round(x + bhs / 2 * n - bhs / 2 * abs(n)), y, round(bhs * abs(n)), round(bhs * abs(n))))
    rect(screen, dark, (round(x + bhs / 2 * n - bhs / 2 * abs(n)), y, round(bhs * abs(n)), round(bhs * abs(n))), 2)

    # Draw ears
    ears(n, x, y)

    # Draw eyes
    eyes(n, x, y)

    # Draw mouth
    mouth(n, x, y)


def dog(n=1.0, x=50, y=400):

    """
    Function draws dog
    :param n: the size of the dog (if it is negative, then dog is mirrored)
    :param x, y: coordinates of the dog (edge of muzzle)
    """

    # Draw body
    body(n, x, y)

    # Draw head
    head(n, x, y)


def dog_house(x=275, y=375):

    """
    Function draws dog house
    :param x, y: coordinates of the dog house (upper left corner)
    """

    # Draw walls and entrance
    polygon(screen, house_color, [(x, y), (x + 75, y + 30), (x + 100, y),
                                  (x + 100, y + 80), (x + 75, y + 110), (x, y + 80)])
    polygon(screen, black, [(x, y), (x + 75, y + 30),
                            (x + 75, y + 110), (x, y + 80)], 1)
    polygon(screen, black, [(x + 75, y + 30), (x + 100, y),
                            (x + 100, y + 80), (x + 75, y + 110)], 1)
    ellipse(screen, black, (x + 17, y + 32, 40, 45))

    # Draw roof
    polygon(screen, roof_color, [(x, y), (x + 75, y + 30), (x + 100, y), (x + 70, y - 70), (x + 40, y - 55)])
    polygon(screen, black, [(x, y), (x + 75, y + 30), (x + 40, y - 55)], 1)
    polygon(screen, black, [(x + 75, y + 30), (x + 100, y), (x + 70, y - 70), (x + 40, y - 55)], 1)

    # Draw chain
    ellipse(screen, black, (x + 10, y + 70, 25, 10), 1)
    ellipse(screen, black, (x + 5, y + 70, 15, 20), 1)
    ellipse(screen, black, (x - 5, y + 80, 20, 15), 1)
    ellipse(screen, black, (x - 15, y + 90, 25, 10), 1)
    ellipse(screen, black, (x - 20, y + 93, 15, 15), 1)
    ellipse(screen, black, (x - 35, y + 101, 25, 10), 1)
    ellipse(screen, black, (x - 45, y + 105, 20, 10), 1)
    ellipse(screen, black, (x - 55, y + 105, 15, 8), 1)


draw_sky()
draw_grass()
fence(75, 25, 700, 300)
fence(-50, 100, 225, 300)
fence(185, 150, 500, 325)
fence(-50, 200, 175, 350)
dog(-0.75, 400, 300)
dog(-0.9, 200, 450)
dog(1, 50, 300)
dog_house()
dog(2, 300, 450)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
