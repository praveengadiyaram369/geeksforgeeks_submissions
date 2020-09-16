# _Addition Under Modulo


def sumUnderModulo(a, b):
    M = 1000000007
    return int(((a % M) + (b % M)) % M)
