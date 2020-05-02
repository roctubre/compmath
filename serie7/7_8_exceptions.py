# a)
# Exceptions are errors which are detected during code execution.
# These errors can be caught in try-except blocks.
# There are many in-built exceptions (see https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
# Custom exceptions can be made by inheriting from the 'Exception' class

# b)
def division(x, y):
    if abs(y) < 1e-14:
        raise ZeroDivisionError("Divison by zero; undefined behaviour")
    return x / y


if __name__ == "__main__":
    try:
        division(2, 0.4)
        division(2, 0)
    except Exception as ex:
        print(str(ex))