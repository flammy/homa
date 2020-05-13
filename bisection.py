import Algorithms.bisection as bisection
import numpy as np
import matplotlib.pyplot as plt


def fun(x):
    return np.cos(x)


bisection.bisection(fun, np.double(-3.0), np.double(0.0))

# disable interactive mode and show result
plt.ioff()
plt.show()
