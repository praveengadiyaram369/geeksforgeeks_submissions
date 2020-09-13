# _Power Using Recursion


def RecursivePower(n, p):
    if p == 0:
        return 1
    return n * RecursivePower(n, p-1)
