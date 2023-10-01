n=int(input())
import turtle as f1
f1.shape('turtle')
f1.speed(10)
for i in range (n):
    for j in range (180):
     turtle.forward(2)
     turtle.left(2)
    turtle.right(180)
    for j in range (180):
      turtle.forward(2)
      turtle.left(2)
    turtle.right(360/n)
