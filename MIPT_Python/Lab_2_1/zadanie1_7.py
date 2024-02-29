import turtle
import numpy as np
turtle.shape('turtle')

k = 0.5
fi_rad = 0.1
fi_deg = fi_rad * (180 / np.pi)
for i in range (1000):
    ro = k * fi_rad
    turtle.forward(ro)
    turtle.left(fi_deg)
    fi_rad += 0.1

turtle.exitonclick()