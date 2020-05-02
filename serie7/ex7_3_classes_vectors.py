class Vector:
    """
    Implements Vectors operations using lists:

    Following methods are implemented:

    add(Vector, Vector)
    scalar(float, Vector)
    """
    def add(z1, z2):
        """
        Adds two vectors of the same dimension and returns a new object.
        Vectors are added element-wise.

        Keyword arguments:
        z1 ... first vector (list with numeric elements)
        z2 ... second vector (list with numeric elements)
        """
        if type(z1) is not list or type(z2) is not list:
            raise TypeError("Not a vector")
        elif len(z1) != len(z2):
           raise ValueError("Dimensions do not match")
        return [a + b for a, b in zip(z1, z2)]

    def scalar(a, z1):
        """
        Scalar-Vector multiplication. Returns a new object.

        Keyword arguments:
        a  ... the scalar (a number - float or int)
        z1 ... vector (list with numeric elements)
        """
        if type(a) not in [int, float]:
            raise TypeError("Scalar is not numerical")
        elif type(z1) is not list:
            raise TypeError("Not a vector")
        return [a*z for z in z1]


class VectorPlus(Vector):
    """
    Extends the Vector class.

    Following methods are added:

    vector_prod(vector, vector)
    tensor(vector, vector)
    """
    def vector_prod(z1, z2):
        """
        Calculates the vector product (cross product) of two 3-dimensional vectors.
        Returns a new object.

        Keyword arguments:
        z1 ... first vector with 3 elements (list with numeric elements)
        z2 ... second vector with 3 elements (list with numeric elements)
        """
        if type(z1) is not list or type(z2) is not list:
            raise TypeError("Not a vector")
        elif len(z1) != 3 or len(z2) != 3:
            raise ValueError("Only three-dimensional vectors allowed")
        return [z1[1]*z2[2] - z1[2]*z2[1],
                z1[2]*z2[0] - z1[0]*z2[2],
                z1[0]*z2[1] - z1[1]*z2[0]]

    def tensor(z1, z2):
        """
        Calculates the tensor product of two vectors.
        Note: Forming the tensor product z1 x z2 is like forming 
        the Cartesion product of two sets

        Keyword arguments:
        z1 ... first vector (list with numeric elements)
        z2 ... second vector (list with numeric elements)
        """
        if type(z1) is not list or type(z2) is not list:
            raise TypeError("Not a vector")
        newvector = []
        for x in z1:
            for y in z2:
                newvector.append(x*y)
        return newvector


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [5, 5, 6]
    c = [4, 5]

    # Test Addition
    print(Vector.add(a, b))
    print(VectorPlus.add(a, b))

    # Test Scalar Multiplication
    print(Vector.scalar(3, a))
    print(VectorPlus.scalar(3, b))

    # Test Vector product
    print(VectorPlus.vector_prod(a, b))

    # Test Tensor product
    print(VectorPlus.tensor(a, c))
