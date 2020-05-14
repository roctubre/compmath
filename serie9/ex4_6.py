import numpy as np
np.set_printoptions(precision=2)

def trim_sort(v):
    """
    Removes elements with the highest/lowest absolute value from a vector.
    Also sorts ascendindly with respect to the absolute value.
    In case of equality, sorts with respect to the imaginery part.
    """
    v = np.delete(v, [np.argmin(np.abs(v)), np.argmax(np.abs(v))])
    v = sorted(v, key=lambda x: (abs(x), x.imag))
    return v


def main():
    v = np.array([4+4j,-3+5j,-5-1j, -3+4j, 1+4j, 3+3j, 3+4j, 1+1j])
    print("Input Values: ", v)
    print("Absolute Values:", abs(v))
    print("Output:", trim_sort(v))


if __name__ == "__main__":
    main()

