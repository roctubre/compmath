import numpy as np


def chessboard(n, display = True):
    """
    Creates a chessboard-matrix with dimensions n times n

    To account for uneven matrices, first a 2n times 2n matrix is created, then
    only the upper left part of the matrix (n times n) is sliced out
    """
    even_row = np.array([1,0]*n)
    uneven_row = np.array([0,1]*n)
    stacked = np.row_stack((even_row, uneven_row)*n)
    matrix = stacked[:n,:n]

    if display:
        print(matrix)

    return matrix


if __name__ == "__main__":
    chessboard(7)