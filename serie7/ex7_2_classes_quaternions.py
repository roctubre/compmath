# Using definition from https://de.wikipedia.org/wiki/Quaternion

class Quaternion:
    """
    This class implements the quaternions with simply methods
    """
    def __init__(self, x0=0.0, x1=0.0, x2=0.0, x3=0.0):
        """
        Initializes a quaternion.

        Keyword arguments:
        x0 ... real part
        x1 ... i-imaginary part
        x2 ... j-imaginary part
        x3 ... k-imaginary part
        """
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def __add__(self, o):
        """
        Overloads the + operator.
        Adds two quaternions element wise and returns a new oject.
        
        Example:
        q1 = Quaternion(1, 0, 0, 0)
        q2 = Quaternion(0, 1, 1, 1)
        print(q1 + q1)

        Example Output:
        [1, 1, 1, 1]
        """
        if type(o) is not Quaternion:
            raise TypeError("Second Value is not a Quaternion")
        return Quaternion(self.x0 + o.x0, self.x1 + o.x1, 
                          self.x2 + o.x2, self.x3 + o.x3)

    def __mul__(self, o):
        """
        Overloads the * operator.
        Multiplies two Quaternions and returns a new oject.
        """
        if type(o) is not Quaternion:
            raise TypeError("Second Value is not a Quaternion")
        return Quaternion(self.x0*o.x0 - self.x1*o.x1 - self.x2*o.x2 - self.x3*o.x3,
                          self.x0*o.x1 + self.x1*o.x0 + self.x2*o.x3 - self.x3*o.x2,
                          self.x0*o.x2 - self.x1*o.x3 + self.x2*o.x0 + self.x3*o.x1,
                          self.x0*o.x3 + self.x1*o.x2 - self.x2*o.x1 + self.x3*o.x0)

    def norm(self):
        """Returns the norm of the Quaternion."""
        return self.x0**2 + self.x1**2 + self.x2**2 + self.x3**2

    def __str__(self):
        """Overloads string output"""
        return "[" + ", ".join([str(self.x0), str(self.x1), str(self.x2), str(self.x3)]) + "]"
        


if __name__ == "__main__":
    a = Quaternion(1, 2, 3, 4)
    b = Quaternion(5, 5, 6, 6)

    # Test Addition
    print(a + b)

    # Test Mulitplication: Quaternions are not commutative
    print(a * b)
    print(b * a)

    # Test Norm
    print(a.norm())
    print(b.norm())
