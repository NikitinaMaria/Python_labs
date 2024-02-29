import turtle
from random import *
from turtle import *
turtle.shape('turtle')

b = Turtle()
b.speed(10)
b.shape('turtle')
b.pencolor('blue')

c = Turtle()
c.speed(10)
c.shape('turtle')
c.pencolor('green')

d = Turtle()
d.speed(10)
d.shape('turtle')
d.pencolor('yellow')

a = Turtle()
a.speed(10)
a.shape('turtle')
turtle.pencolor('red')
turtle.speed(10)
for i in range(1000):
    turtle.right(randint(-360,360))
    turtle.forward(randint(1,50))
    a.right(randint(-360,360))
    a.forward(randint(1,50))
    b.right(randint(-360,360))
    b.forward(randint(1,50))
    c.right(randint(-360,360))
    c.forward(randint(1,50))
    d.right(randint(-360,360))
    d.forward(randint(1,50))

turtle.exitonclick()