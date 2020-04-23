# a)
def join_strings_reverse(s1, s2): 
    """ Joins two strings, reverses the order of letters and
        prints it out

        Explanation:
            1. Joins two strings using the + operator
            2. Reverses the order by slicing with stepsize -1
    """
    print(str(s1 + s2)[::-1])


# b)
def flip_reverse(text):
    """ Flips first and last word of the given text and 
        reverses all letters

        Explanation:
            1. Split text into words
            2. Swap first and last word (if only one word then first = last) 
            3. Join reversed words using list comprehensation
    """
    words = text.split()
    words[0], words[-1] = words[-1], words[0]
    text_new = ' '.join([w[::-1] for w in words])
    print(text_new)


# c)
def square_cubic(n = 10):
    """ Prints out the squares and cubes of the integers 1 to n
    """
    for i in range(1, n + 1):
        print(i, "\t", i*i, "\t", i*i*i)


if __name__ == "__main__":
    # a) Test function with some strings
    join_strings_reverse("Hello", "World")

    # b) Test function with a random text
    flip_reverse("The quick brown fox jumps over the lazy dog")

    # c) Test function
    square_cubic()




        