from itertools import permutations

# a)
def has_duplicates(n): 
    """ Check if the given list has unique elements
        Uses the property of sets:
        If converted into a set it is guaranteed to have unique elements.
        -> Compare number of elements to determine if the list contains duplicates
    """
    if type(n) is not list:
        raise TypeError("Given input is not a list")

    if len(n) != len(set(n)):
        return True

    return False


# b)
def first_duplicate(n):
    """ Returns the first duplicate element in a list.
        Returns False if there are no duplicates.
        Iterates through the list and keeps track of all seen elements.
        If an element was already seen, it will return the first seen duplicate.
    """
    if has_duplicates(n):
        unique = set()
        for x in n:
            if x in unique:
                return x
            else:
                unique.add(x)

    return False

# c)
def remove_duplicates(n):
    """ Removes duplicates in a given list (referenced list)
        Returns a list of all duplicates.
    """

    seen = []
    duplicates = []

    # determine duplicates
    for x in n:
        if x in seen:
            duplicates.append(x)
        else:
            seen.append(x)

    # modify list in-place by assiining to its slice
    n[:] = seen; 

    # return duplicates
    return duplicates

# d)
def permutation(n):
    """ Prints out all permutations of a list.
        Uses itertools.permutations() which is an in-build function
    """
    for x in permutations(n):
        print(x)



if __name__ == "__main__":
    # a) Test duplicates
    print("Test a)")
    mylist1 = ["hello", 1, 2, "world"]
    mylist2 = ["hello", 1, 2, "world", "hello"]
    print(has_duplicates(mylist1)) # false
    print(has_duplicates(mylist2)) # true

    # b) Test duplicates
    print("Test b)")
    mylist3 = ["hello", 1, 2, "world", "world", 2]
    print(first_duplicate(mylist3)) # 2

    # c) Test remove duplicates
    print("Test c)")
    print(mylist3) # ['hello', 1, 2, 'world', 'world', 2]
    print(remove_duplicates(mylist3)) # ['world', 2]
    print(mylist3) # ['hello', 1, 2, 'world']

    # d) Test list permutation
    mylist4 = [1,2,3,4]
    permutation(mylist4)