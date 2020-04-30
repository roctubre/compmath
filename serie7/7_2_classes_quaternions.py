# Using definition from https://de.wikipedia.org/wiki/Quaternion

class Quaternion:
    def __init__(self, x0, x1, x2, x3):
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def __add__(self, o):
        """ Overloading + operator
            Addition between two Quaternions
        """
        if type(o) is not Quaternion:
            raise TypeError("Second Value is not a Quanterion")
        return Quaternion(self.x0 + o.x0, self.x1 + o.x1, 
                          self.x2 + o.x2, self.x3 + o.x3)

    def __mul__(self, o):
        """ Overloading * operator
            Multiplication between two Quaternions
        """
        if type(o) is not Quaternion:
            raise TypeError("Second Value is not a Quanterion")
        return Quaternion(self.x0*o.x0 - self.x1*o.x1 - self.x2*o.x2 - self.x3*o.x3,
                          self.x0*o.x1 + self.x1*o.x0 + self.x2*o.x3 - self.x3*o.x2,
                          self.x0*o.x2 - self.x1*o.x3 + self.x2*o.x0 + self.x3*o.x1,
                          self.x0*o.x3 + self.x1*o.x2 - self.x2*o.x1 + self.x3*o.x0)

    def norm(self):
        """ Returns the norm of the Quaternion """
        return self.x0**2 + self.x1**2 + self.x2**2 + self.x3**2

    def __str__(self):
        """ Overload string output """
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
