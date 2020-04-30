
# a) Uses string.replace()
def find_replace(s_in, s_find, s_replace):
    return s_in.replace(s_find, s_replace)

# b) Uses string.upper(), string.split()
def f(s, capitalize = False):
    if capitalize:
        return s.upper().split()
    else:
        return s.split()


if __name__ == "__main__":
    # test a)
    print(find_replace("ded did dod, bla bli dod", "dod", "hunga"))

    # test b)
    print(f("Hello World! Mama is here"))
    print(f("Hello World! Daddy is here", True))
