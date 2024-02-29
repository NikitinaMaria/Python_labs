import turtle
turtle.shape('turtle')
def glaz():
    turtle.pendown()
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(-15)
    turtle.end_fill()
    turtle.penup()

turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()

turtle.goto(-40,150)
glaz()

turtle.goto(40,150)
glaz()

turtle.goto(0,100)
turtle.pendown()
turtle.pencolor('black')
turtle.width(10)
turtle.right(90)
turtle.forward(25)
turtle.penup()

turtle.goto(-50,70)
turtle.pendown()
turtle.pencolor('red')
turtle.circle(50, 180)

turtle.exitonclick()