n=int(input())
import turtle
turtle.shape('turtle')
for i in range (n):
    turtle.forward(60)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(60)
    turtle.right(360/n)
