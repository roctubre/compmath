import numpy as np


def tensor1(A, B, display=False):
    """
    Calculates the product of two matrices using the first method (see HW Problem 3.6).

    Using numpy's einsum() function it calculates the product with the given axis. 
    """
    mat = np.einsum('irl,lrj->ij', A, B)
    if display:
        print(mat)
    return mat


def tensor2(A, B, display=False):
    """
    Calculates the product of two matrices using the second method (see HW Problem 3.6).

    Applying the product on the second axis of method 1 will give us our 1-D Array.
    """
    mat = np.product(tensor1(A, B), axis=1)
    if display:
        print(mat)
    return mat


def main():
    # Test functions
    A = np.array([[[1,2], [3,4]], [[1,2], [3,4]]])
    B = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
    tensor1(A, B, True)
    tensor2(A, B, True)


if __name__ == "__main__":
    main()