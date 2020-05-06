import numpy as np


def diagonals(n, display = True):
    """
    Creates a matrix with ones on the diagonal and anti-diagonal, while all
    other entries are zero.
    """

    # First create an id-matrix (diagonal) and its flipped version (anti-diagonal)
    matrix = np.identity(n)
    trans = np.flip(matrix, axis = 1)

    # Fuse them together by masking
    mask = (matrix == 0)
    matrix[mask] = trans[mask]

    if display:
        print(matrix)

    return matrix


if __name__ == "__main__":
    diagonals(5)