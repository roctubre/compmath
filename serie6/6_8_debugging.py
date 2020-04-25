# a) 
# What does the following code do?
# import pdb; pdb.set_trace()
# Answer:
# The typical usage to break into the debugger from a running program is 
# to insert this line at the location you want to break into the debugger. 
# You can then use debugger commands to show information around the breakpoint
# or control the execution steps.


# b)
from math import sin
import pdb;

print("This is a debugging test.")

def f(x):
    pdb.set_trace()
    a
    x = x + 1.0

    return sin(x)**2 + x

print("value of f(x)", f(1))

# Debugger: n, s, l, c commands
# n(ext) ... Continues execution until next line. Function-calls are stepped OVER.
# s(tep) ... Continues execution until next line. Function-calls are stepped INTO.
# l(ist) [first[, last]] ... Lists 11 lines of source code around the current breakpoint; o
#                            Optional range parameters for source code lines of current line
# c(ontinue) ... Continues execution and only stops until next breakpoint if any