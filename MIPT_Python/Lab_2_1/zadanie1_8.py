import turtle
turtle.shape('turtle')

a = 5
uvel = 5
for i in range (50):
    turtle.forward(a)
    turtle.left(90)
    a += uvel

turtle.exitonclick()