import turtle
import numpy as np
turtle.shape('circle')

turtle.speed(50)
turtle.penup()
turtle.width(5)
turtle.goto(-300, -300)
turtle.pendown()
turtle.goto(300, -300)
turtle.goto(300, 300)
turtle.goto(-300, 300)
turtle.goto(-300, -300)
turtle.hideturtle()

from random import randint
import turtle


number_of_turtles = 25


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
coord_x = []
coord_y = []
speed_x = []
speed_y = []
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-300, 300), randint(-300, 300))
    coordx0, coordy0 = unit.position()
    coord_x.append(coordx0)
    coord_y.append(coordy0)
    speed_x.append(randint(-10, 10))
    speed_y.append(randint(-10, 10))


for i in range(200):
    for j in range(number_of_turtles):
        unit = pool[j]
        if coord_x[j] > 300:
            coord_x[j] = 298
            speed_x[j] = - speed_x[j]
        if coord_y[j] > 300:
            coord_y[j] = 298
            speed_y[j] = - speed_y[j]
        if coord_x[j] < -300:
            coord_x[j] = -298
            speed_x[j] = - speed_x[j]
        if coord_y[j] < -300:
            coord_y[j] = -298
            speed_y[j] = - speed_y[j]
        unit.goto(coord_x[j] + speed_x[j], coord_y[j] + speed_y[j])
        coord_x[j] += speed_x[j]
        coord_y[j] += speed_y[j]

turtle.exitonclick()