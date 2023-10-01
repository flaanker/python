import turtle as f1
import numpy as np
f1.shape('turtle')
f1.speed(10)
rad = 10
x = 1
n = 3
f1.up()
f1.goto(rad, 0)
f1.down()
def polygonych(x):
    for x in range(1, n+1):
        f1.left((180 - 360 / n) / 2)
        f1.left(360 / n)
        f1.forward(2 * rad * np.sin(np.pi/n))
        f1.right((180 - 360 / n) / 2)
for n in range(3, 12):
    polygonych(x)
    n += 1
    rad += 10
    f1.up()
    f1.goto(rad, 0)
    f1.down()
