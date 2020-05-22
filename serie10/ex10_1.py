import matplotlib.pyplot as plt
import numpy as np


def main():
    # create figure
    fig = plt.figure()

    # b) add two axes
    ax1 = fig.add_axes([0.11, 0.11, 0.35, 0.8])
    ax2 = fig.add_axes([0.6, 0.11, 0.35, 0.8])
     
    # c) plot, set labels and titles 
    ax1.set_title("first plot")
    ax2.set_title("second plot")
    x = np.linspace(0,2)
    ax1.set_xlabel("x")
    ax1.set_ylabel("$y=x^2$")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y=x")
    ax1.plot(x, x**2, color="r", label='$x^2$')
    ax2.plot(x, x, color="b", label='x')
    ax1.legend()
    ax2.legend()

    plt .show()

    # d) What do plt.gca and plt.gcf do?
    """
    plt.gca ... get current axes
    - Returns a handle to the current active axis

    plt.gcf ... get current figure
    - returns a handle to the current figure
    - If no current figure exists, a new one is created using figure()
    """


if __name__ == "__main__":
    main()