import numpy as np


def cgsolve(A, b, tau):
    """
    Given A nd b, it solves the linear system Ax=b using the CF-method.
    The matrix A must be symmetric and postive definite.

    The CG-steps get smaller after every iteration. 
    For an nxn matrix the algorithm performs at most n iterations before terminating.
    """

    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A is not symmetric.")
    for eig in np.linalg.eigvals(A):
        if eig <= 0.:
            raise ValueError("Matrix A is not positive definite")

    x = np.ones(A.shape[0])    # arbitrary initial guess
    r = b - np.matmul(A, x)
    d = r

    while True:
        r_prev = r
        alpha = r.dot(r)/d.dot(np.matmul(A, d))
        x = x + alpha*d
        r = r - alpha*np.matmul(A, d)
        if np.linalg.norm(r) <= tau:
            break
        d = r + (r.dot(r)/r_prev.dot(r_prev))*d

    return x


def main():
    # 2x2 matrx
    A = np.array([[1, 0],[0, 1]])
    b = np.array([23, 34])
    tau = 10e-8

    x = cgsolve(A, b, tau)
    print("### Test 2x2")
    print("x:", x)
    print("Approx.:", np.matmul(A, x))
    print("Actual:", b)

    # 6x6 matrix
    A = np.array([[7, -2, -3, 0, -1, 0],
                  [-2, 8, 0, 0, -1, 0],
                  [-3, 0, 4, -1, 0, 0],
                  [0, 0, -1, 5, 0, -2],
                  [-1, -1, 0, 0, 4, 0],
                  [0, 0, 0, -2, 0, 6]])
    b = np.array([1, 2, 3, 4, 5, 6])
    tau = 10e-8

    x = cgsolve(A, b, tau)
    print("\n### Test 6x6")
    print("x:", x)
    print("Approx.:", np.matmul(A, x))
    print("Actual:", b)


if __name__ == "__main__":
    main()

