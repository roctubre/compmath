# a) & b)
def odd(n): 
    """ Counts the number of ODD digits in a given integer/float
    """
    try:
        if type(n) in [int, float]:
            return sum([True for d in str(n) if d.isdigit() and int(d) % 2 != 0])
        else:
            raise TypeError("Given input is not a supported type")
    except TypeError as e:
        print("Error:", str(e))


# a) & b)
def even(n): 
    """ Counts the number of EVEN digits in a given integer/float
    """
    try:
        if type(n) in [int, float]:
            return sum([True for d in str(n) if d.isdigit() and int(d) % 2 == 0])
        else:
            raise TypeError("Given input is not a supported type")
    except TypeError as e:
        print("Error:", str(e))


# c)
def primedigits(n):
    """ Counts the number of prime digits in a given integer
    """
    try:
        if type(n) is int:
            return sum([True for d in str(n) if int(d) in [2, 3, 5, 7]])
        else:
            raise TypeError("Given input is not a supported type")
    except TypeError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    # a) Test odd/even digits given an integer
    mynumber = 123456789
    print(odd(mynumber)) # 5
    print(even(mynumber)) # 4

    # b) Test odd/even digits given a float
    mynumber2 = 123456789.11112222
    print(odd(mynumber2)) # 9
    print(even(mynumber2)) # 8

    # c) Test prime digit counter in a given integer
    mynumber3 = 9876543210
    print(primedigits(mynumber3)) # 4
