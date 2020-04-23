# a)
def tensor_prod(a, b): 
    """ Returns the tensor product using lists
    """

    product = []
    # loop through first tensor/vector
    for a_ in a:
        row = []
        # multiply with each element of second tensor and add to row list 
        for b_ in b:
            row.append(a_ * b_)

        # add row list to final product
        product.append(row)

    return product


# b)
def prod(A, B):
    """ Returns the matrix product of two matrices using lists
    """

    # Check if dimenstions are compatible
    if len(A[0]) != len(B):
        raise ValueError("Dimensions do not match.")

    product = []
    # iterate through rows of A
    for i in range(len(A)):
        # new row for final product
        new_row = []
        # iterate through columns of B
        for j in range(len(B[0])):
            new_row.append(0)
            # iterate through rows of B
            for k in range(len(B)):
                new_row[-1] += A[i][k] * B[k][j]
        # append row to final product
        product.append(new_row)

    return product


if __name__ == "__main__":
    # a) Test tensor product
    a = [1,2,3,4]
    b = [1,2,3]
    print(tensor_prod(a, b))


    # b) Test matrix product
    A = [[1,2,3], [4,5,6]]                  # 2x3 matrix
    B = [[1,1,2,2], [2,2,3,3], [3,3,4,4]]   # 3x4 matrix
    try:
        print(prod(A, B))                       # Result is a 2x4 matrix
    except Exception as e:
        print("Error: ", str(e))

        