import turtle
import numpy as np
turtle.shape('turtle')

def zvezda(n):
    turtle.speed(10)
    r = 10 * n #Радиус описанного правильного многоугольника
    if n % 2 != 0: #Для нечётных
        deg = 180 / n
        a = r * np.sin((180 - deg) * np.pi / 180) / np.sin(deg / 2 * np.pi / 180) #Длина стороны звезды
        turtle.left(deg / 2)
        turtle.penup()
        turtle.forward(r)
        turtle.left(180 - deg / 2)
        turtle.pendown()
        for i in range(n):
            turtle.forward(a)
            turtle.left(180 - deg)
    elif n % 4 == 0: #Для чётных, делящихся на 4
        deg = 360 / n
        a = r * np.sin((180 - deg) * np.pi / 180) / np.sin(deg / 2 * np.pi / 180) #Длина стороны звезды
        turtle.left(deg / 2)
        turtle.penup()
        turtle.forward(r)
        turtle.left(180 - deg / 2)
        turtle.pendown()
        for i in range(n):
            turtle.forward(a)
            turtle.left(180 - deg)
    else: #Для чётных, не делящихся на 4
        deg = 360 / n
        a = r * np.sin((180 - deg) * np.pi / 180) / np.sin(deg / 2 * np.pi / 180) #Длина стороны звезды
        turtle.left(deg / 2)
        turtle.penup()
        turtle.forward(r)
        turtle.left(180 - deg / 2)
        turtle.pendown()
        t = n // 2
        for i in range(t):
            turtle.forward(a)
            turtle.left(180 - deg)
        turtle.left(deg / 2)
        turtle.penup()
        turtle.forward(r)
        turtle.right(180 - deg)
        turtle.forward(r)
        turtle.left(180 - deg / 2)
        turtle.pendown()
        t = n // 2
        for i in range(t):
            turtle.forward(a)
            turtle.left(180 - deg)

zvezda(26)

turtle.exitonclick()