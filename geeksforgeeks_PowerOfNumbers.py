# _Power Of Numbers


def power(N, R):
    mod = 1000000007

    if R <= 1:
        return N

    if R % 2 == 0:
        return (power(N, int(R/2)) ** 2) % mod
    else:
        return (N * (power(N, int(R/2)) ** 2)) % mod
