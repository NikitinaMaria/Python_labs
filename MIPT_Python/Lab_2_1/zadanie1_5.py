import turtle
turtle.shape('turtle')

for x in range(10, 110, 10):
    for i in range(3):
        turtle.forward(x)
        turtle.left(90)
    turtle.forward(x)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.pendown()
    turtle.left(180)

turtle.exitonclick()