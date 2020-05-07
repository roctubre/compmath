import numpy as np
from timeit import default_timer as timer


def matrix_prod(A, B, display = False):
    """
    Computes the matrix product of two matrices using array slicing and vector operations.
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError("Dimensions not compatible.")

    # Not allowed!?
    #matrix = A.dot(B)

    # Dotproduct of each A.row*B.clm
    matrix = np.array([[np.sum(A[i,:]*B[:,j]) for j in range(B.shape[1])] 
                       for i in range(A.shape[0])])

    if display:
        print(matrix)

    return matrix


def matrix_prod2(A, B, display = False):
    """
    Computes the matrix product of two matrices using python loops.
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError("Dimensions not compatible.")

    matrix = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for l in range(A.shape[1]):
                matrix[i,j] += A[i,l]*B[l,j]

    if display:
        print(matrix)

    return matrix


def main():
    # Test functions
    A = np.array([[1,2], [3,4]])
    B = np.array([[1,2,3], [4,5,6]])
    print(A.dot(B))
    matrix_prod(A, B, True)
    matrix_prod2(A, B, True)
    

    #---------------------------------------------------------
    print("### Test performance ###")
    # Generate large random matrices
    np.random.seed(0)
    A = np.random.randint(low=0, high=100, size=(100,500))
    B = np.random.randint(low=0, high=100, size=(500,200))

    # Method #0: numpy.dot()
    tic = timer()
    A.dot(B)
    toc = timer()
    print("Reference - np.dot(): ", toc - tic, "s")

    # Method #1: using slicing
    tic = timer()
    matrix_prod(A, B)
    toc = timer()
    print("Method #1 - Slicing: ", toc - tic, "s")

    # Method #2: using loops
    tic = timer()
    matrix_prod2(A, B)
    toc = timer()
    print("Method #2 - Looping: ", toc - tic, "s")

    """ Result (on my machine)
    Reference - np.dot():       0.0094825 s
    Method #1 - Slicing:        0.1890397 s
    Method #2 - Looping:       11.7723318 s

    Interpretation:
    Slicing > looping through elements. In-built function are best.
    """

if __name__ == "__main__":
    main()