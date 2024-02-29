import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Background of screen
rect(screen, (220, 220, 220), (0, 0, 400, 400))

# Drawing head
circle(screen, (225, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 1)

# Drawing eyes
# Left eye
circle(screen, (225, 0, 0), (130, 170), 30)
circle(screen, (0, 0, 0), (130, 170), 30, 1)
circle(screen, (0, 0, 0), (130, 170), 10)
# Right eye
circle(screen, (225, 0, 0), (270, 170), 20)
circle(screen, (0, 0, 0), (270, 170), 20, 1)
circle(screen, (0, 0, 0), (270, 170), 10)

# Drawing brows
polygon(screen, (0, 0, 0), [(50, 90), (55, 80), (175, 150), (170, 160), (50, 90)])
polygon(screen, (0, 0, 0), [(230, 153), (345, 110), (348, 120), (233, 163), (230, 153)])

# Drawing mouth
rect(screen, (0, 0, 0), (130, 275, 140, 25))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True