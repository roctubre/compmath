import matplotlib.pyplot as plt
import numpy as np


def main():
    fig2, ax2 = plt.subplots(2, 2, sharex=True)
    x = np.linspace(-2, 2, 100)
    y1 = np.sin(4*x)
    y2 = np.cos(x)*np.sin(x)
    y3 = x**4
    y4 = np.cos(x) + np.sin(x)

    # first subplot
    ax2[0,0].plot(x,y1,"red",label="$sin(4x)$")
    ax2[0,0].set_xlabel("x")
    ax2[0,0].set_ylabel("y")
    ax2[0,0].legend()
    ax2[0,0].set_xticks([0, -2,2])
    ax2[0,0].set_yticks([0, -1,1])

    # second subplot
    ax2[0,1].plot(x,y2,"green",label="$cos(x)sin(x)$")
    ax2[0,1].set_xlabel("x")
    ax2[0,1].legend()
    ax2[0,1].set_yticks([0, -0.5, 0.5])

    # third subplot
    ax2[1,0].plot(x,y3,"blue",label="$x^4$")
    ax2[1,0].set_xlabel("x")
    ax2[1,0].set_ylabel("y")
    ax2[1,0].legend()
    ax2[1,0].set_yticks([0, 10])

    # fourth subplot
    ax2[1,1].plot(x,y4,"black",label="$cos(x)+sin(x)$")
    ax2[1,1].set_xlabel("x")
    ax2[1,1].legend()

    plt.show()


if __name__ == "__main__":
    main()