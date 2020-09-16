# _Sum of Digits of a Number


def sumOfDigits(n):
    if n > 0:
        return ((n % 10) + sumOfDigits(int(n/10)))
    else:
        return 0
