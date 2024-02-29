import pygame
import random
from random import randint
from pygame.draw import *
pygame.init()

random.seed(8968)
FPS = 30
screen = pygame.display.set_mode((600, 800))
screen_ellipse = pygame.Surface((600, 800), pygame.SRCALPHA, 32)
screen_tree = pygame.Surface((600, 800), pygame.SRCALPHA, 32)
screen_unicorn = pygame.Surface((600, 800), pygame.SRCALPHA, 32)
screen_unicorn_2 = pygame.Surface((600, 800), pygame.SRCALPHA, 32)

pink = (233, 175, 175)
light_pink = (233, 198, 175)
light_blue = (175, 233, 221)
cream = (255, 238, 170)
light_green = (229, 255, 128)
colors = pink, light_blue, light_pink, light_green, cream

# Sky
rect(screen, (0, 255, 255), (0, 0, 600, 400))

# Sun
color_1 = 0
color_2 = 255
color_3 = 255
for i in range(255):
    color_1 += 1
    if color_2 > 222:
        color_2 = 255 - i // 8
    if color_3 > 87:
        color_3 = 255 - 5*i // 6
    circle(screen, (color_1, color_2, color_3), (423, 172), (255 - i) * 3 // 4)

# Grass
rect(screen, (0, 255, 0), (0, 400, 600, 400))

def draw_tree(screen_x, screen_y, x, y):

    '''
    Function draws tree
    :param screen_x: tree width
    :param screen_y: tree height
    :param x, y: coordinates of the upper left corner
    '''

    # Tree
    rect(screen_tree, (230, 230, 230), (110, 470, 30, 100))
    ellipse(screen_tree, (0, 128, 0), (45, 130, 160, 200))
    ellipse(screen_tree, (0, 255, 0), (44, 128, 164, 204), 5)
    ellipse(screen_tree, (0, 128, 0), (0, 270, 250, 140))
    ellipse(screen_tree, (0, 255, 0), (-1, 268, 253, 143), 5)
    ellipse(screen_tree, (0, 128, 0), (45, 370, 155, 115))
    ellipse(screen_tree, (0, 255, 0), (45, 369, 160, 118), 5)
    # White ellipses
    ellipse(screen_tree, (255, 204, 170), (15, 325, 45, 41))
    ellipse(screen_tree, (0, 255, 0), (15, 325, 45, 41), 5)
    ellipse(screen_tree, (255, 204, 170), (130, 150, 45, 40))
    ellipse(screen_tree, (0, 255, 0), (130, 150, 45, 40), 5)
    ellipse(screen_tree, (255, 204, 170), (190, 327, 47, 41))
    ellipse(screen_tree, (0, 255, 0), (190, 327, 47, 41), 5)
    ellipse(screen_tree, (255, 204, 170), (145, 435, 42, 42))
    ellipse(screen_tree, (0, 255, 0), (145, 435, 42, 42), 5)

    # Drawing tree
    screen.blit(pygame.transform.scale(screen_tree, (screen_x, screen_y)), (x, y))
    
# Unicorn
def unicorn():
    '''
    Function draws unicorn on a separate screen
    '''

    # Tail
    for i in range(25):
        ellipse(screen_unicorn, colors[randint(0, 4)], (
        randint(288 - i * 4, 290 - i * 2), randint(580 + i * 5, 605 + i * 5), randint(30, 45 + 3 * i // 2),
        randint(12, 27)))
    # Body
    ellipse(screen_unicorn, (255, 255, 255), (440, 470, 80, 60))
    ellipse(screen_unicorn, (255, 255, 255), (470, 490, 80, 40))
    ellipse(screen_unicorn, (255, 255, 255), (290, 565, 225, 110))
    rect(screen_unicorn, (255, 255, 255), (445, 500, 60, 120))
    # Legs
    rect(screen_unicorn, (255, 255, 255), (305, 635, 18, 110))
    rect(screen_unicorn, (255, 255, 255), (347, 635, 22, 100))
    rect(screen_unicorn, (255, 255, 255), (430, 635, 20, 120))
    rect(screen_unicorn, (255, 255, 255), (480, 635, 16, 95))
    # Eye
    ellipse(screen_unicorn, (229, 128, 255), (475, 485, 23, 20))
    ellipse(screen_unicorn, (34, 28, 36), (485, 490, 9, 9))
    ellipse(screen_ellipse, (255, 255, 255), (200, 320, 12, 7))
    # Horn
    polygon(screen_unicorn, (233, 175, 175), ([(485, 390), (485, 475), (465, 473), (485, 390)]))
    # Mane
    for i in range(14):
        ellipse(screen_unicorn, colors[randint(0, 4)], (
        randint(438 - i * 7, 440 - i * 2), randint(460 + i * 8, 474 + i * 7), randint(30, 45 + 3 * i // 2),
        randint(15, 30)))

    # Speck
    screen_ellipse_2 = pygame.transform.rotate(screen_ellipse, 135)
    screen_unicorn.blit(pygame.transform.scale(screen_ellipse_2, screen_unicorn.get_rect().size), (177, -8))

def draw_unicorn(screen_x, screen_y, x, y):
    '''
    Function draws unicorn
    :param screen_x: unicorn width
    :param screen_y: unicorn height
    :param x, y: coordinates of the upper left corner
    '''

    # Drawing unicorn
    screen.blit(pygame.transform.scale(screen_unicorn, (screen_x, screen_y)), (x, y))

def draw_mirrored_unicorn(screen_x, screen_y, x, y):
    '''
    Function draws mirrored unicorn
    :param screen_x: unicorn width
    :param screen_y: unicorn height
    :param x, y: coordinates of the upper left corner
    '''

    unicorn()

    # Mirrored unicorn
    screen_unicorn_2 = pygame.transform.flip(screen_unicorn, True, False)
    screen.blit(pygame.transform.scale(screen_unicorn_2, (screen_x, screen_y)), (x, y))

# Drawing 5 trees
draw_tree(700, 900, 50, -140)
draw_tree(450, 800, -50, 50)
draw_tree(450, 400, 130, 270)
draw_tree(400, 500, 50, 320)
draw_tree(400, 500, -30, 430)

# Drawing 4 unicorns
draw_mirrored_unicorn(350, 500, 400, 170)
draw_unicorn(250, 320, 230, 170)
draw_mirrored_unicorn(120, 150, 500, 280)
draw_unicorn(500, 680, -30, 130)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
