import numpy as np
import turtle as f1
f1.shape('turtle')
for i in range (3,12):
    for t in range (i):
       f1.left(180-((180*(i-2)/i)))
       f1.fd(i*20)
    r=(i*2)/(2*np.sin((np.pi)/i))
    f1.penup()
    f1.fd(r*0.8)
    f1.right(180-((180*(i-2)/i)))
    f1.fd(r*0.8)
    f1.left(180-((180*(i-2)/i)))
    f1.pendown()
