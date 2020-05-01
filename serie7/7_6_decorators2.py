import math


def count(fun):
    """ Returns a decorator function, which when called returns 
        the call count and the evaluation 
    """
    counter = 0
    def deco(x):
        nonlocal counter
        counter += 1
        return counter, fun(x)

    return deco


if __name__ == "__main__":
    # Declare two decorators
    f = count(math.sin)
    f2 = count(math.cos)

    # Test first decorator
    print(f(0.1))
    print(f(0.2))

    # Second decorator; doesn't affect count of first decorator
    print(f2(0))
    print(f2(math.pi))

    # And first again
    print(f(0.3))