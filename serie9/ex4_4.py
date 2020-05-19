import numpy as np
from numpy.linalg import norm
from scipy.linalg import eig

def poweriteration(A, tau=10e-8, x=None):
    """
    Approximates the eigenvalue with the greatest absolute value of a
    symmetric matrix A.
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A is not symmetric.")
    if not x:
        x = np.ones((A.shape[0]))
    lam = x.dot(np.matmul(A, x))

    while True:
        x = np.matmul(A, x)/norm(np.matmul(A, x))
        lam_prev = lam
        lam = x.dot(np.matmul(A, x))

        if abs(lam) <= tau:
            cond = tau
        else:
            cond = tau*abs(lam)

        if norm(np.matmul(A, x) - lam*x) <= tau and abs(lam_prev - lam) <= cond:
            break

    return lam, x



def main():
    # Test 2x2
    print("### Test 2x2")
    A = np.array([[6, -1], [2, 3]])
    print(poweriteration(A)[0])
    print(eig(A)[0].real)

    # Test 3x3
    print("\n### Test 3x3")
    A = np.array([[1, 2, 1], [6, -1, 0], [-1, -2, -1]])
    print(poweriteration(A)[0])
    print(eig(A)[0].real)

if __name__ == "__main__":
    main()

