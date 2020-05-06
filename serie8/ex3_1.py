import numpy as np
from timeit import default_timer as timer


def block(A, B, display = False):
    """
    Generates a block diagonal matrix of the form [[A,0], [0,B]] using 
    vector/matrix functions and indexing.
    """

    # Create matrix according to sizes of A and B
    C = np.zeros((A.shape[0] + B.shape[0], A.shape[1] + B.shape[1]))

    # Put matrix A into upper left using slicing
    C[:A.shape[0], :A.shape[1]] = A

    # Put matrix B into the middle using slicing
    C[A.shape[0]:, A.shape[1]:] = B

    if display:
        print(C)

    return C


def block_loops(A, B, display = False):
    """
    Generates a block diagonal matrix of the form [[A,0], [0,B]] using loops.
    """

    # Create matrix according to sizes of A and B
    C = np.zeros((A.shape[0] + B.shape[0], A.shape[1] + B.shape[1]))

    # Put matrix A into upper left using loops
    for clm in range(A.shape[1]):
        for row in range(A.shape[0]):
            C[row, clm] = A[row, clm]

    # Put matrix B into the middle using loops
    for clm in range(B.shape[1]):
        for row in range(B.shape[0]):
            C[A.shape[0]+row, A.shape[1]+clm] = B[row,clm]

    if display:
        print(C)

    return C


def main():
    # Small Test: generate block matrices
    print("### Test block generation ###")
    A = np.array([[1,2], [3,4]])
    B = np.array([[1,2,3], [4,5,6]])
    print("Are equal?", np.array_equal(block(A, B, True), block_loops(A, B, True)))


    #---------------------------------------------------------
    print("### Test performance ###")
    # Generate large random matrices
    A = np.random.randint(low=0, high=100, size=(1000,2000))
    B = np.random.randint(low=0, high=100, size=(4400,3300))

    # Method 1: using slicing
    tic = timer()
    block(A, B)
    toc = timer()
    print("Method #1: ", toc - tic, "s")

    # Method 2: using loops
    tic = timer()
    block_loops(A, B)
    toc = timer()
    print("Method #2: ", toc - tic, "s")

    """ Result (on my machine)
    Method #1:   0.1364385 s
    Method #2:  13.6611307 s

    Interpretation:
    It gets more apparent that the larger the matrices are the more effcient slicing is 
    compared to just using loops.
    """


if __name__ == "__main__":
    main()

