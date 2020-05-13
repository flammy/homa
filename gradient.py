import Algorithms.gradient as grad
import numpy as np
import matplotlib.pyplot as plt


# test function for  maximizing
def fun(x: np.array) -> np.float:
    bla = np.sin(x[0] * x[1]) + np.sin(x[0]) + np.cos(x[1])
    return bla


# start maximizing from start-point
start = np.array([0.2, -2.1])
grd = grad.max(start, fun)

# disable interactive mode and show result
plt.ioff()
plt.show()
