import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots()

    # Starting points
    X, Y = np.meshgrid(np.linspace(-1,1,20, endpoint=True), 
                       np.linspace(-2,1,30, endpoint=True))

    # Directions
    u = Y.copy()
    v = X.copy()
    u[X > 0] = 1 - u[X > 0]
    v[X > 0] = 1 + v[X > 0]
    u[X < 0] = -1 + u[X < 0]
    v[X < 0] = -1 - v[X < 0]

    # Set up plot
    ax.quiver(X[X > 0], Y[X > 0], u[X > 0], v[X > 0], color="r", label='x > 0')
    ax.quiver(X[X < 0], Y[X < 0], u[X < 0], v[X < 0], color="b", label='x < 0')
    ax.axis([-1.2,1.2,-2.2,1.2])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title("Vectorfield")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()