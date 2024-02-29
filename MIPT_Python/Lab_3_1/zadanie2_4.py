import turtle
import numpy as np
turtle.shape('circle')

turtle.speed(50)
turtle.penup()
turtle.goto(-300, -200)
turtle.pendown()
turtle.goto(300, -200)

a_y = -5
v_x = 10
x = 0
y = 0
v_y = 50
dt = 0.1
turtle.penup()
turtle.goto(-300, -200)
turtle.pendown()
while True:
    turtle.goto(-300 + x, -200 + y)
    x += v_x * dt
    y += v_y * dt + a_y * dt ** 2 / 2
    v_y += a_y * dt
    if y < 0:
        v_y = -0.8 * v_y
        v_x = 0.8 * v_x
        y = 0

turtle.exitonclick()