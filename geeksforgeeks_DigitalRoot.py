# _Digital Root


def digitalRoot(n):
    if len(str(n)) > 1:
        return digitalRoot((n % 10) + digitalRoot(int(n/10)))
    else:
        return n
