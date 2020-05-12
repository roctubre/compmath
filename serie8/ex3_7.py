import numpy as np
from numpy.linalg import det

def wedge(w_vecs):
    """
    Returns a function to calculate the wedge product.
    Basis w-vectors must be given.
    """
    def prod(v_vecs):
        """
        Evaluates the wedge product given v-vectors.

        It first performs the euclidean scalar product on the basis with each vector in v.
        The resulting array is then used to get the determinant.
        """
        return det(np.array([[np.dot(w_vecs, v) for w_vecs in w_vecs] for v in v_vecs]))

    return prod


def main():
    w_vecs = [[1,2,3],[1,1,1],[1,0,2]]
    v_vecs = [[1,1,2],[1,1,1],[2,1,1]]
    f = wedge(w_vecs)
    print(f(v_vecs))


if __name__ == "__main__":
    main()