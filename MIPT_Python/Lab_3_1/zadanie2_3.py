import turtle
import numpy as np
turtle.shape('turtle')

def ris(pug1, px, pug2, x1, ug1, x2, ug2, x3, ug3, x4, ug4, x5, ug5, x6, kug1, kx1, kug2, kx2):
    turtle.right(pug1)
    turtle.forward(px)
    turtle.right(pug2)
    turtle.pendown()
    turtle.forward(x1)
    turtle.right(ug1)
    turtle.forward(x2)
    turtle.right(ug2)
    turtle.forward(x3)
    turtle.right(ug3)
    turtle.forward(x4)
    turtle.right(ug4)
    turtle.forward(x5)
    turtle.right(ug5)
    turtle.forward(x6)
    turtle.penup()
    turtle.right(kug1)
    turtle.forward(kx1)
    turtle.right(kug2)
    turtle.forward(kx2)

inp = open('input.txt', 'r')
ris_c = []
for i in range(10):
    per = inp.readline()
    per_list = per.split(' ')
    a = []
    for j in per_list:
        a.append(eval(j))
    ris_c.append(tuple(a))

ris_c = tuple(ris_c)
ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8, ris9 = ris_c

turtle.speed(50)
turtle.penup()
turtle.goto(-200,0)

ris(*ris0)
ris(*ris1)
ris(*ris2)
ris(*ris3)
ris(*ris4)
ris(*ris5)
ris(*ris6)
ris(*ris7)
ris(*ris8)
ris(*ris9)

turtle.goto(-200,70)

ris(*ris1)
ris(*ris4)
ris(*ris1)
ris(*ris7)
ris(*ris0)
ris(*ris0)

inp.close()

turtle.exitonclick()