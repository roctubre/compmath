import math

# (1) ... formula seen on exercise sheet

class faculty:
    def fac(n, ptr = False):
        """ Return n! """
        fac = math.factorial(n)
        if ptr:
            print(fac)
        return fac

    def fac_stir(n, ptr = False):
        """ Using Stirling formula to approximate n! """
        fac = (2*math.pi*n)**0.5 * (n/math.e)**n
        if ptr:
            print(fac)
        return fac

    def fac_gam(n, ptr = False):
        """ Using (1) to approximate n! """
        z = n + 1
        fac = ((2*math.pi)/z)**0.5 * \
              ((1/math.e)*(z + 1/(12*z - 1/(10*z))))**z
        if ptr:
            print(fac)
        return fac

    def fac_stir_err(n, ptr = False):
        """ Return the relative error of the stirling formula """
        err = abs(faculty.fac(n) - faculty.fac_stir(n)) / faculty.fac(n)
        if ptr:
            print(err)
        return err

    def fac_gam_err(n, ptr = False):
        """ Return the relative error of the (1) approximation """
        err = abs(faculty.fac(n) - faculty.fac_gam(n)) / faculty.fac(n)
        if ptr:
            print(err)
        return err


if __name__ == "__main__":
    n = 10

    # Test class methods
    print("Exact n!:", faculty.fac(n))
    print("Using Stirling:", faculty.fac_stir(n))
    print("Using (1):", faculty.fac_gam(n))
    print("Stirling Error:", faculty.fac_stir_err(n))
    print("(1) Error:", faculty.fac_gam_err(n))

    # Test print flags
    print("===== Print flag outputs =====")
    faculty.fac(n, True)
    faculty.fac_stir(n, True)
    faculty.fac_gam(n, True)
    faculty.fac_stir_err(n, True)
    faculty.fac_gam_err(n, True)