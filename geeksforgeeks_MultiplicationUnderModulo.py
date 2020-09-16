# _Multiplication Under Modulo


def multiplicationUnderModulo(a, b):
    M = 1000000007
    return int(((a % M) * (b % M)) % M)
