import numpy as np


def getmax(v):
    """
    Returns the max element of a vector. 
    Also replaces all elements |x|>=max_x by sign(x)max_x.
    """
    max = np.max(v)
    v[v < -max] = -max
    return max


def main():
    v = np.array([-5, -3, 0, 2, 3])
    print(v)
    print("Max:", getmax(v))
    print(v)


if __name__ == "__main__":
    main()

