import turtle
turtle.shape('turtle')

turtle.left(90)
r = 25
for i in range(10):
    turtle.circle(r, 360)
    turtle.circle(-r, 360)
    r += 7

turtle.exitonclick()