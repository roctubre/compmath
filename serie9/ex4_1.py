import numpy as np


def block_diagonal_matrices(n):
    """
    Generates the block diagonal matrices mentionen in Problem 4.1 using
    the Kronecker product, a composite array made of blocks of the second 
    array scaled by the first.
    """
    A1 = np.kron(np.eye(n,dtype=int), np.ones((2, 2)))
    A2 = np.kron(np.eye(n,dtype=int), np.ones((3, 2)))
    return A1, A2



def main():
    A1, A2 = block_diagonal_matrices(3)
    print(A1)
    print(A2)


if __name__ == "__main__":
    main()

