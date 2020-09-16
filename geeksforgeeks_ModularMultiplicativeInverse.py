# _Modular Multiplicative Inverse


def modInverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return -1
