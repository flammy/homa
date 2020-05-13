import numpy as np
import matplotlib.pyplot as plt


def bisection(function, start: np.double, stop: np.double, e: np.double = np.double(10E-8), iteration: int = 25, delay: np.double = np.double(0.0)) -> np.double:

    plt.ion()
    plt.show()

    fig = plt.figure("Find null by bisection")
    ax = fig.add_subplot(111)
    ax.grid()

    for i in range(0, iteration):
        if np.abs(start - stop) <= e:
            return start
        middle = (start + stop) / 2
        f_start = function(start)
        f_stop = function(stop)
        f_middle = function(middle)

        ax.scatter(start, f_start, color='red')
        ax.scatter(stop, f_stop, color='blue')

        if f_start < 0 < f_middle:
            stop = middle
        elif f_middle < 0 < f_stop:
            start = middle
        else:
            raise ValueError('Function does not change signs in interval [{0}:{1}]'.format(start, stop))
    return start
