from numpy import prod
from timeit import default_timer as timer


class Poly:
    def __init__(self, coeff):
        """
        Initializes the coefficients 
        Must be a list object.
        """
        if type(coeff) != list:
            raise TypeError("Coefficients must be a list")
        self.coefficients = coeff

    def poly_eval(self, x):
        """
        Evaluates polynomial at x
        """
        p = 0
        for i in range(len(self.coefficients)):
            p += self.coefficients[i]*x**i
        return p

    def poly_der_coef(self, n):
        """
            returns the n-th derivative of the polynomial
        """
        d = []
        for i in range(n, len(self.coefficients)):
            d.append(self.coefficients[i] * prod([x for x in range((i+1)-n,i+1) if x > 0]))
        return Poly(d)

    def __str__(self):
        return str(self.coefficients)


def main():
    # Test poly_eval
    p = Poly([1,2,3])
    print(p.poly_eval(2));

    # Test poly_der_coef
    q = Poly([2, 3, 4, 5, 6])
    print(q.poly_der_coef(3));
    r = Poly([1, -2, 0, 0, 1, -10])    # 2. deriv: 12x^2 - 200x^3
    print(r.poly_der_coef(2));


if __name__ == "__main__":
    main()