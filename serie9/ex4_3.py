import numpy as np


def formed_matrices(n):
    """
    Creates 0,1,2-formed nxn-matrices for a given odd n >= 5.
    """
    if n < 5 or n % 2 == 0:
        raise ValueError("n must be odd and >=5")

    # Init matrices
    A0 = np.zeros((n,n))
    A1 = np.zeros((n,n))
    A2 = np.zeros((n,n))
    mid = int(n/2)

    # zero
    A0[[0,-1],:] = 1
    A0[:,[0,-1]] = 1

    # one
    A1[:,mid] = 1

    # two
    A2[[0,-1, mid],:] = 1
    A2[:mid,-1] = 1
    A2[mid:,0] = 1

    return A0, A1, A2



def main():
    A0, A1, A2 = formed_matrices(5)
    print(A0)
    print(A1)
    print(A2)


if __name__ == "__main__":
    main()

