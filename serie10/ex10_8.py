""" Reference
https://stackoverflow.com/questions/8487893/generate-all-the-points-on-the-circumference-of-a-circle
https://stackoverflow.com/questions/33510979/generator-of-evenly-spaced-points-in-a-circle-in-python
"""

import matplotlib.pyplot as plt
import math


def circle_points(r, n, ellipse=False):
    """
    Returns evenly spaced points on the circumfuerence of a circle given the radii
    and number of points
    """
    if ellipse == False:
        return [[math.cos(2 * math.pi / n * x) * r for x in range(0, n + 1)],
                [math.sin(2 * math.pi / n * x) * r for x in range(0, n + 1)]]
    else:
        return [[math.cos(2 * math.pi / n * x) * r for x in range(0, n + 1)],
                [math.sin(2 * math.pi / n * x) * r/2 for x in range(0, n + 1)]]


def main():
    # init variables
    num_rays = 19
    num_circles = 20
    R = [r / 20 for r in range(num_circles)]
    fig, ax = plt.subplots(1, 2, figsize=(10, 3))

    # first subplot
    circles1 = [circle_points(R[i], num_rays) for i in range(num_circles)]
    for circle in circles1:
        ax[0].scatter(circle[0], circle[1], s=5)  # s defines size of dots
        ax[0].set_xticks([-1, -0.5, 0, 0.5, 1]) # scale x axes
        ax[0].set_yticks([-1, -0.5, 0, 0.5, 1]) # scale y axes
        ax[0].legend(['circle'], loc='upper right')

    # second subplot
    circles2 = [circle_points(R[i], num_rays, True) for i in range(num_circles)]
    for circle in circles2:
        ax[1].scatter(circle[0], circle[1], s=5)  # s defines size of dots
        ax[1].set_xticks([-1, -0.5, 0, 0.5, 1]) # scale x axes
        ax[1].set_yticks([-1, -0.5, 0, 0.5, 1]) # scale y axes
        ax[1].legend(['ellipsis'], loc='upper right')

    plt.show()


if __name__ == "__main__":
    main()