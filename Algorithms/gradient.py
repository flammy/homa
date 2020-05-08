import numpy as np
import matplotlib.pyplot as plt


# determines the gradient for a given array
# by partial derivative (difference quotient)
def grad(x: np.array, function, h: np.double = np.double(10E-8)) -> np.array:
    gradient = np.empty([2, ], dtype=np.double)
    result = function(x)

    for i in range(len(x)):
        x[i] += h
        gradient[i] = (function(x) - result) / h
        x[i] -= h
    return gradient


# determines the local maximum by following the gradient,
# probing nearby spots and tuning the step size based on the probe
def max(x: np.array, function, lmbda: np.double = np.double(1.0), iteration: int = 25, delay: np.double = np.double(0.0)) -> np.array:

    plt.ion()
    plt.show()

    fig = plt.figure("Maximizing by Gradient")
    ax = fig.add_subplot(111, projection='3d')
    ax.grid()

    for i in range(0, iteration):

        if np.linalg.norm(grad(x, function)) < 10E-5:
            return x

        grd = lmbda * grad(x, function)
        x_new = np.add(x, grd)

        result_old = function(x)
        result_new = function(x_new)

        ax.scatter(x[0], x[1], result_old)

        # probing one step ahead
        if result_new > result_old:
            # probing two steps ahead
            lmbda *= 2
            grd_test = lmbda * grad(x, function)
            x_test = np.add(x, grd_test)
            result_test = function(x_test)
            if result_test > result_new:
                # going two steps if result is better
                x_new = x_test
                result_new = result_test
                ax.plot(np.array([x[0], x_new[0]]), np.array([x[1], x_new[1]]), np.array([result_old, result_new]))
            else:
                # going one step ahead
                lmbda /= 2
                ax.plot(np.array([x[0], x_new[0]]), np.array([x[1], x_new[1]]), np.array([result_old, result_new]))
        else:
            # current position is better
            while result_new <= result_old:
                # trying nearby positions
                lmbda /= 2
                grd = lmbda * grad(x, function)
                x_new = np.add(x, grd)
                result_new = function(x_new)
            ax.plot(np.array([x[0], x_new[0]]), np.array([x[1], x_new[1]]), np.array([result_old, result_new]))

        if delay != 0.0:
            plt.pause(delay)

        x = x_new

    ax.scatter(x[0], x[1], function(x))
    return x
