# _Primality Test


def isPrime(N):
    if N == 1:
        return False
    else:
        for i in range(N):
            if i > 1 and (N % i) == 0:
                return False

        return True
