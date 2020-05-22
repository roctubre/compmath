import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure()

    # add big axes
    ax1 = fig.add_axes([0.09, 0.1, 0.8, 0.8])
    x = np.linspace(0,100)
    ax1.set_xlabel("x")
    ax1.set_ylabel("$x^2$")
    ax1.plot(x, 2*x, color="r", label='$x^2$')
    ax1.legend()

    # add smaller axes
    ax2 = fig.add_axes([0.163, 0.49, 0.2, 0.2])
    x = np.linspace(20,22)
    ax2.set_xlabel("x")
    ax2.set_ylabel("$x^2$")
    ax2.set_title("zoom")
    ax2.set_ylim(30,50)
    ax2.plot(x, 2*x, color="r", label='$x^2$')

    plt .show()

if __name__ == "__main__":
    main()