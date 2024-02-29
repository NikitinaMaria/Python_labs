import turtle
turtle.shape('turtle')

for x in range (12):
    turtle.right(360/12)
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)

turtle.exitonclick()