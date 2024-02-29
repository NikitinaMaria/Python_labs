import pygame
import random
from random import randint
from pygame.draw import *
pygame.init()

random.seed(8968)
FPS = 30
screen = pygame.display.set_mode((600, 800))
screen_ellipse = pygame.Surface((600, 800), pygame.SRCALPHA, 32)

pink = (233, 175, 175)
light_pink = (233, 198, 175)
light_blue = (175, 233, 221)
cream = (255, 238, 170)
light_green = (229, 255, 128)
colors = pink, light_blue, light_pink, light_green, cream

# Background of screen
rect(screen, (0, 255, 255), (0, 0, 600, 400))
rect(screen, (0, 255, 0), (0, 400, 600, 400))

# Sun
circle(screen, (255, 221, 85), (570, 70), 100)

# Tree
rect(screen, (230, 230, 230), (80, 470, 30, 100))
ellipse(screen, (0, 128, 0), (15, 370, 160, 120))
ellipse(screen, (0, 128, 0), (-30, 270, 250, 140))
ellipse(screen, (0, 128, 0), (15, 130, 160, 200))
ellipse(screen, (255, 204, 170), (-15, 325, 45, 41))
ellipse(screen, (255, 204, 170), (100, 150, 45, 40))
ellipse(screen, (255, 204, 170), (160, 327, 47, 41))
ellipse(screen, (255, 204, 170), (115, 435, 42, 42))

# Unicorn
# Tail
for i in range(25):
    ellipse(screen, colors[randint(0, 4)], (
    randint(288 - i * 4, 290 - i * 2), randint(580 + i * 5, 605 + i * 5), randint(30, 45 + 3 * i // 2),
    randint(12, 27)))
# Body
ellipse(screen, (255, 255, 255), (440, 470, 80, 60))
ellipse(screen, (255, 255, 255), (470, 490, 80, 40))
ellipse(screen, (255, 255, 255), (290, 565, 225, 110))
rect(screen, (255, 255, 255), (445, 500, 60, 120))
# Legs
rect(screen, (255, 255, 255), (305, 635, 18, 110))
rect(screen, (255, 255, 255), (347, 635, 22, 100))
rect(screen, (255, 255, 255), (430, 635, 20, 120))
rect(screen, (255, 255, 255), (480, 635, 16, 95))
# Eye
ellipse(screen, (229, 128, 255), (475, 485, 23, 20))
ellipse(screen, (34, 28, 36), (485, 490, 9, 9))
ellipse(screen_ellipse, (255, 255, 255), (200, 320, 12, 7))
# Horn
polygon(screen, (233, 175, 175), ([(485, 390), (485, 475), (465, 473), (485, 390)]))
# Mane
for i in range(14):
    ellipse(screen, colors[randint(0, 4)], (
    randint(438 - i * 7, 440 - i * 2), randint(460 + i * 8, 474 + i * 7), randint(30, 45 + 3 * i // 2),
    randint(15, 30)))

screen_ellipse_2 = pygame.transform.rotate(screen_ellipse, 135)
screen.blit(pygame.transform.scale(screen_ellipse_2, screen.get_rect().size), (177, -8))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
