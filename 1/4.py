import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-70, 70, 1)
plt.plot(x, eval(input()))
 with plt.xkcd():
    plt.title(input())
    plt.xlabel(input())
plt.ylabel(input())
plt.grid(True)
plt.show()
