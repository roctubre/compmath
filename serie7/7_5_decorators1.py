import math

# a)
def dec(ev, fun):
    """ Returns a function that evaluates with given parameters when called """
    def wrapper():
        return fun(ev)
    return wrapper

# b)
def comp(l):
    """ Returns a function which is the composition of functions
        in a given list
    """
    def deco(x):
        val = x
        for f in reversed(l):
            val = f(val)
        return val

    return deco

if __name__ == "__main__":
    # a) Test decorator
    mydec1 = dec(math.pi/2, math.sin) # create decorator with sin()
    mydec2 = dec(1, math.exp) # create decorator with exp()
    print(mydec1) # address of function
    print(mydec2) # address of function
    print(mydec1()) # execute function; sin(pi/2) = 1
    print(mydec2()) # execute function; e**1 = e = 2.71

    # b) Test decorator - composition
    l1 = [math.fabs, math.cos, math.asin, math.sin, math.atan, math.tan]
    mycomp = comp(l1)
    print(mycomp) # address of function
    print(mycomp(math.pi)) # execute function -> 1
    print(mycomp(0)) # execute function -> 1
