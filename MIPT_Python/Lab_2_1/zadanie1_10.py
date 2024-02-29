import turtle
turtle.shape('turtle')

for i in range (3):
    turtle.circle(50, 360)
    turtle.circle(-50, 360)
    turtle.left(60)

turtle.exitonclick()
