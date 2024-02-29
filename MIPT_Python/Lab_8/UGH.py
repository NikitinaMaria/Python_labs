from random import randrange as rnd, choice
import pygame
from pygame.draw import *
import math
import time

pygame.init()

screen_size_x = 800
screen_size_y = 600
FPS = 50

# Colors and list of the colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# The main screen
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
screen.fill(WHITE)
font = pygame.font.Font('freesansbold.ttf', 32)


class Ball:
    def __init__(self, angle, power, parent, ball_x=40, ball_y=450):
        """ Constructor of the ball class

        Args:
        x - Starting position of the ball horizontally
        y - Starting position of the ball vertically
        """
        self.parent = parent
        self.ball_x = ball_x
        self.ball_y = ball_y

        # Radius of the ball
        self.ball_r = 13

        # Speed of the ball
        self.speed_x = 0.8 * power * math.cos(angle)
        self.speed_y = - 0.8 * power * math.sin(angle)
        self.color = choice([RED, GREEN, BLUE, MAGENTA])
        self.id = circle(screen, self.color,
                         (self.ball_x, self.ball_y,), self.ball_r)
        self.live = 200

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        gravitation = 1
        self.speed_y -= gravitation
        self.ball_x += self.speed_x
        self.ball_y -= self.speed_y

        # Taking into account the reflection from the walls
        if self.ball_x <= self.ball_r:
            self.ball_x = self.ball_r
            self.speed_x = - self.speed_x * 0.8
        if self.ball_y <= 0:
            self.ball_y = 0
            self.speed_y = - self.speed_y
            self.speed_x = self.speed_x * 0.8
        if self.ball_x >= screen_size_x - self.ball_r:
            self.ball_x = screen_size_x - self.ball_r
            self.speed_x = - self.speed_x * 0.8
        if self.ball_y >= screen_size_y - self.ball_r:
            self.ball_y = screen_size_y - self.ball_r
            self.speed_y = - self.speed_y * 0.9
            self.speed_x = self.speed_x * 0.9

        self.live -= 1
        if self.live == 0:
            self.parent.delete_ball()
        self.id = circle(screen,
                         self.color,
                         (round(self.ball_x), round(self.ball_y)), self.ball_r)

    def check(self, target_x, target_y, target_r):
        distance = math.sqrt((self.ball_x - target_x) * (self.ball_x - target_x) + \
                             (self.ball_y - target_y) * (self.ball_y - target_y))
        if distance <= self.ball_r + target_r:
            return True
        return False


class Gun:
    def __init__(self, parent, gun_power=10, gun_on=0, gun_angle=0):
        """ Constructor of the gun class
        Args:
        gun_power - Power of the gun
        """
        self.parent = parent
        self.gun_power = gun_power
        self.gun_on = gun_on
        self.gun_angle = gun_angle
        self.color = BLACK
        self.id = line(screen, self.color, [20, 420], [50, 450], 7)

    def fire_start(self):
        self.gun_on = 1

    def fire_end(self):
        self.gun_on = 0
        self.parent.shoot(self.gun_angle, self.gun_power)
        self.gun_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        mouse_x, mouse_y = event.pos
        if mouse_x > 20:
            self.gun_angle = math.atan((mouse_y - 450) / (mouse_x - 20))
    def draw(self):
        if self.gun_on:
            self.color = RED
        else:
            self.color = BLACK
        self.id = line(screen, self.color, [20, 450],
                       [20 + max(self.gun_power, 20) * math.cos(self.gun_angle), 450 + max(self.gun_power, 20) * math.sin(self.gun_angle)],7)

    def power_up(self):
        if self.gun_on:
            if self.gun_power < 100:
                self.gun_power += 1
            self.color = RED
        else:
            self.color = BLACK


class Target:
    def __init__(self, parent):
        """
        Constructor of the target class
        """
        self.points = 0
        self.live = 1
        self.color = RED
        self.target_x = 0
        self.target_y = 0
        self.target_r = 0
        self.id = circle(screen, self.color, (self.target_x, self.target_y), self.target_r)
        self.text = font.render(str(self.points), True, BLACK)
        self.screen_id_points = screen.blit(self.text, self.text.get_rect())
        self.parent = parent
        self.hitted = False
        self.count_of_shoots = 0
        self.congrats_time = 100


    def new_target(self):
        """ Инициализация новой цели. """
        self.target_x = rnd(600, 780)
        self.target_y = rnd(300, 550)
        self.target_r = rnd(10, 50)
        self.id = circle(screen, self.color, (self.target_x, self.target_y), self.target_r)

    def draw_target(self):
        if self.hitted:
            self.congrats_time -= 1
            if self.congrats_time < 0:
                self.new_target()
                self.congrats_time = 100
                self.hitted = False
            text = font.render('You hit the target in ' + str(self.count_of_shoots) + ' turns', True, BLACK)
            screen.blit(text, (screen_size_x // 4, screen_size_y // 2))
            self.text = font.render(str(self.points), True, BLACK)
            self.screen_id_points = screen.blit(self.text, self.text.get_rect())

        else:
            self.id = circle(screen, self.color, (self.target_x, self.target_y), self.target_r)
            self.text = font.render(str(self.points), True, BLACK)
            self.screen_id_points = screen.blit(self.text, self.text.get_rect())

    def hit(self, count_of_shoots, points=1):
        """Попадание шарика в цель."""
        self.hitted = True
        self.count_of_shoots = count_of_shoots
        self.points += points
        self.text = font.render(str(self.points), True, BLACK)
        self.screen_id_points = screen.blit(self.text, self.text.get_rect())



class Solyanka:
    def __init__(self):
        self.gun = Gun(self)
        self.balls = []
        self.target = Target(self)
        self.target.new_target()
        self.count_of_shoots = 0

    def draw(self):
        self.gun.draw()
        for ball in self.balls:
            ball.move()
        self.target.draw_target()

    def shoot(self, angle, power):
        self.balls.append(Ball(angle, power, self))
        self.count_of_shoots += 1

    def delete_ball(self):
        del self.balls[0]

    def hitting(self):
        if self.target.hitted == False:
            for ball in self.balls:
                if ball.check(self.target.target_x, self.target.target_y, self.target.target_r):
                    self.target.hit(self.count_of_shoots)
                    self.count_of_shoots = 0


clock = pygame.time.Clock()
finished = False
solyanka = Solyanka()


while not finished:
    clock.tick(FPS)
    pygame.display.update()
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            solyanka.gun.fire_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            solyanka.gun.fire_end()
        elif event.type == pygame.MOUSEMOTION:
            solyanka.gun.targetting(event)
    solyanka.gun.power_up()
    solyanka.hitting()
    solyanka.draw()


pygame.quit()