# _GP Term


def termOfGP(A, B, N):
    common_ratio = float(B) / float(A)
    return math.floor((A * math.pow(common_ratio, N-1)))
