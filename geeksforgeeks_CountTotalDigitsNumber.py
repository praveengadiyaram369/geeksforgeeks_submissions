# _Count Total Digits in a Number


def countDigits(n):
    if n > 0:
        return (1 + countDigits(int(n/10)))
    else:
        return 0
