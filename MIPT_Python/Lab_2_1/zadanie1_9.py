import turtle
import numpy as np
turtle.shape('turtle')

def mnogougol(n):
    r = (n - 2) * 20 #Радиус описанной окружности
    a = 2 * r * np.sin(2 / (2 * n) * np.pi) #Длина стороны
    n_deg = (n - 2) * 180 #Градусная мера одного угла
    turtle.left(90)
    turtle.left((180 - n_deg / n) / 2) #Стартовый угол
    for i in range (n):
        turtle.forward(a)
        turtle.left(180 - n_deg / n)
    turtle.penup()
    turtle.right((180 - n_deg / n) / 2) #Возвращение к стартовому углу
    turtle.right(90)
    turtle.forward(20) #Переход к следующей фигуре
    turtle.pendown()

for k in range (3, 11):
    mnogougol(k)

turtle.exitonclick()