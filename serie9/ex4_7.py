""" 1) Prove
U is a regular matrix which has non-zero values on its diagonal. 
Thus having full rank, it can be brought to reduced row echelon form, meaning has a definite solution.

This can be shown through induction:
From the last equation x[-1]* U[n-1,n-1] = b[-1] we receive a definite x[-1].
x[-2]*U[n-2,n-2] + x[-1]* U[n-1,n-1] = b[-2] we receive x[-2].
Analogue for all others until x[-n]
"""

import numpy as np

def solveU(U, b):
    """
    Computes the unique solution x in C^n of Ux=b, given an upper triangular matrix.
    Uses only loops and arithmetics.
    """
    # validate input
    if np.allclose(U,np.triu(U))==False or np.linalg.det == 0:
        raise TypeError("U is not an upper regular triangular matrix")
        
    elif len(U.shape) != 2 or len(b.shape) != 1:
        raise TypeError("unsuitable object")
        
    else:
        un, um = U.shape
        n, = b.shape
        if un != um or un != n:
            raise TypeError(("dimensions do not fullfill requirements"))

    # solve 
    x = np.zeros(n, dtype=complex)
    x[-1] = (b[-1]) / U[n - 1, n - 1]
    for i in range(1, n):
        t = U[(n - (i + 1)):(n - i)] @ x
        x[-(i + 1)] = (b[-(i + 1)] - t) / U[n - (i + 1), n - (i + 1)]

    return x


def main():
    U = np.array([[3 + 7j, 5 + 0j, 9 + 2j, 1 + 0j],
                      [0 + 0j, 0 + 1j, 3 + 0j, 2 + 7j],
                      [0 + 0j, 0 + 0j, -2 + 5j, 1 + 1j],
                      [0 + 0j, 0 + 0j, 0 + 0j, 4 + 1j]])   
    b = np.array([3 - 1j, 0 + 0j, 9 + 2j, 2 + 0j])
    x = solveU(U,b)
    print(x)  

    #Test
    print(np.allclose(U @ x,b))  # compare Ax to b

    r = np.linalg.solve(U, b) # using np.linalg
    print(np.allclose(x, r))  # compare results


if __name__=="__main__":
    main()

        
    