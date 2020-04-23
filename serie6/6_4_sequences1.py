# a)
def sequence(n, a0 = 1): 
    """ Generates a sequence
    """
    seq = [a0]
    for i in range(1, n):
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] / 2)
        else:
            seq.append(3*seq[-1] + 1)

    return seq


# b) Verify ending cycle 4->2->1->4
def verify_cycle():
    print("Verify ending cycle for from 1-100")
    for a0 in range(1,101):
        seq = sequence(1000, a0) # sequence should be length long enough -> 1000

        # remove last elements in seq until it is a 4 or empty
        while seq[-1] != 4 or len(seq) == 0:
            seq.pop(-1)

        # compare last for elements with cycle
        if seq[-4:] == [4, 2, 1, 4]:
            print("a0:", a0, "confirmed.")
        else:
            print("a0:", a0, "doesn't end in a cyle.")
            print(seq)


if __name__ == "__main__":
    # a) Test sequence generation
    print("Test Sequence Generation")
    print(sequence(20, 7))

    # b) Verify ending cycle 4->2->1->4 with arbitrary initial value
    verify_cycle()
        