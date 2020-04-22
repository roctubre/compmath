from math import floor

# a)
def intbreak(n): 
    """ Returns a list of digits of a given integer
        using list comprehension.
    """
    return [int(d) for d in str(n)]

# b)
def counter(n):
    """ Reverses the order of a given list in-place.
        It iterates through the first half of the list and 
        swaps each element with its mirroed index in the second half.
    """
    for i in range(1, floor(len(n)/2) + 1):
        n[i - 1], n[-i] = n[-i], n[i - 1]

if __name__ == "__main__":
    # break down integer into its digits
    mylist = intbreak(123456789)
    print(mylist)

    # reverse the list order
    counter(mylist)
    print(mylist)
