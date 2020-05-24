import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np

def func1(x):
    """ 2nd degree polynomial """
    return x**2 #+ 3*x

def func2(x):
    """ 3nd degree polynomial """
    return x**3 #+ 2*x**2 + 5*x


def midpointrule(a, b, f, n):
    """
    Returns a vector of values defined by the composite midpoint rule 
    """
    def x(j, N):
        return a + (j*(b-a))/N
    
    int_ = []
    for i in range(n+1):
        N = 2**i
        int_.append(((b-a)/N) * np.sum([f((x(j-1, N) + x(j, N))/2) for j in range(1, N+1)]))

    return int_

def main():
    # set variables
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    a = -5
    b = 10
    n = 10
    
    # 2nd degree
    int_ = midpointrule(a, b, func1, n)
    lim_, err_ = integrate.quad(lambda x: func1(x), a, b) # calculate true limit
    print("vec(I_L):", int_)
    print("Actual limit:", lim_)

    # verify approximation using plots
    ax[0].set_title("2nd degree Integral")
    ax[0].set_xlabel('k')
    ax[0].axhline(y=lim_, color='r', linestyle='--')
    ax[0].plot(int_, marker="x")
    ax[0].legend(["limit", "vec($I_N$)"], loc='lower right')

    # 3rd degree
    int2_ = midpointrule(a, b, func2, n)
    lim2_, err2_ = integrate.quad(lambda x: func2(x), a, b) # calculate true limit
    print("\nvec(I_L):", int_)
    print("Actual limit:", lim_)

    # verify approximation using plots
    ax[1].set_title("3rd degree Integral")
    ax[1].set_xlabel('k')
    ax[1].axhline(y=lim2_, color='r', linestyle='--')
    ax[1].plot(int2_, marker="x")
    ax[1].legend(["limit", "vec($I_N$)"], loc='lower right')


    plt.show()


if __name__ == "__main__":
    main()