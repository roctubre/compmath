# Comparing custom and numpy functions which save and load arrays

import matplotlib.pyplot as plt
import numpy as np
import timeit


def loadMatrix(src="matrix.dat"):
    A = []
    with open(src, 'r') as file:
        lines = file.readlines()
        for line in lines:
            B = []
            for x in line.split(' '):
                B.append(float(x))
            A.append(B)

    return np.array(A)


def saveMatrix(A):
    with open('matrix.dat', 'w') as file:
        lines = []
        for i in range(A.shape[0]):
            lines.append(' '.join([str(A[i][j]) for j in range(A.shape[1])]))
        file.writelines('\n'.join(lines))


def main():
    ### Compare file structure
    A = np.array([[1.03,2,3], [4,5.5,6]])

    # custom functions
    saveMatrix(A)
    print(loadMatrix())

    # numpy
    np.savetxt('np_matrix.dat', A)
    B = np.loadtxt('np_matrix.dat')
    print(B)

    ## RESULT file structure
    #  Both cases save the values in a readable format, each line containing one row of the array.
    #  saveMatrix() function uses less space, because it only saves significant digits while the numpy
    #  function saves 18 decimal digits for each value.
    

    ### Compare performance
    n = 1000
    np.random.seed(123)
    A = np.random.rand(n, n)

    # custom functions
    start = timeit.default_timer()
    saveMatrix(A)
    print("Custom SAVE: {} s".format(timeit.default_timer() - start))

    start = timeit.default_timer()
    B = loadMatrix()
    print("Custom LOAD: {} s".format(timeit.default_timer() - start))

    # numpy
    start = timeit.default_timer()
    np.savetxt('np_matrix.dat', A)
    print("Numpy SAVE: {} s".format(timeit.default_timer() - start))

    start = timeit.default_timer()
    B = np.loadtxt('np_matrix.dat')
    print("Numpy LOAD: {} s".format(timeit.default_timer() - start))

    ## RESULT performance
    #  Custom SAVE: 11.1976502 s
    #  Custom LOAD: 0.9726055999999996 s
    #  Numpy SAVE: 1.4901908000000006 s
    #  Numpy LOAD: 1.4007845000000003 s
    #
    #  The custom save() function gets significantly worse when n gets larger. 
    #  This is most likely caused by the usage of two for loops, which gives the function
    #  a complexity of O(n^2).


if __name__ == "__main__":
    main()