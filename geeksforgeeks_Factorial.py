# _Factorial Of Number


def factorial(N):
    if N <= 1:
        return 1
    else:
        return (N * factorial(N-1))
