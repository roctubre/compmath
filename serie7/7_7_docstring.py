import inspect
from ex7_2_classes_quaternions import Quaternion
from ex7_3_classes_vectors import Vector, VectorPlus

if __name__ == "__main__":
    # Quaternion
    print("Quaternion:\n", Quaternion.__doc__)
    print("Quaternion.__init__:\n", Quaternion.__init__.__doc__)
    print("Quaternion.__add__:\n", Quaternion.__add__.__doc__)
    print("Quaternion.norm:\n", Quaternion.__add__.__doc__)

    # Vector
    print("Vector:\n", Vector.__doc__)
    print("Vector.add:\n", Vector.add.__doc__)
    print("Vector.scalar:\n", Vector.scalar.__doc__)

    # VectorPlus
    print("VectorPlus:\n", VectorPlus.__doc__)
    print("VectorPlus.vector_prod:\n", VectorPlus.vector_prod.__doc__)
    print("VectorPlus.tensor:\n", VectorPlus.tensor.__doc__)