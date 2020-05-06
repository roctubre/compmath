import numpy as np
from timeit import default_timer as timer

def seminorm_loop(x, p, display = False):
    """
    Calculate for a given complex vector and some 1 <= p < inf the l_p-semi-norm
    using loops and scalar arithmetic
    """
    if p < 1:
        raise ValueError("p must be >= 1")

    # Using scalar arithmetic to calculate each elements absolute value raised to p
    x_abs_p = x.real**2 + x.imag**2 * (1j)
    x_abs_p = ((x_abs_p.real + x_abs_p.imag) ** 0.5) ** p

    # Sum all elements with an uneven index
    sum = 0
    for j in range(1, len(x_abs_p)+1, 2):
        # Since arrays in python are zero-based, substract 1 from j
        j -= 1
        sum += x_abs_p[j]

    # Raise to 1/p to get the l_p-semi-norm
    result = sum**(1/p)

    if display:
        print(result)

    return result


def seminorm(x, p, display = False):
    """
    Calculate for a given complex vector and some 1 <= p < inf the l_p-semi-norm
    using vector functions and arithmetics
    """
    if p < 1:
        raise ValueError("p must be >= 1")

    # Using slicing to get every second element, then calculate the absulte value for each element 
    # raised to p, then take the sum of them which is raised to 1/p
    result = np.sum(np.abs(x[::2])**p)**(1/p)

    if display:
        print(result)

    return result


def main():
    # Test functions
    x = np.array([1+1j, 2+2j, 3+3j])
    seminorm_loop(x, 3, True)
    seminorm(x, 3, True)

    #---------------------------------------------------------
    print("### Test performance ###")
    # Generate random complex vector with dim 10**5
    np.random.seed(0)
    x = np.random.random(10**7) + np.random.random(10**7) * 1j
    p = np.random.randint(1, 1000)
    
    # Method 1: using loops and scalar arithmetic
    tic = timer()
    seminorm_loop(x, p)
    toc = timer()
    print("Method /w loops: ", toc - tic, "s")

    # Method 2: using vector functios and arithmetics
    tic = timer()
    seminorm(x, p)
    toc = timer()
    print("Method /w vec-fns: ", toc - tic, "s")

    """ Result (on my machine)
    Method /w loops:    3.6782882 s
    Method /w vec-fns:  0.3709317 s

    Interpretation:
    Using numpy vector function are apparently faster then larger the vector size gets. 
    """


if __name__ == "__main__":
    main()