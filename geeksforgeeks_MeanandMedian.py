# _Mean And Median of Array


def median(A, N):

    A.sort()
    if N % 2 != 0:
        return A[math.floor(N/2)]
    else:
        return math.floor((A[int(N/2)] + A[int(N/2) - 1])/2)


def mean(A, N):
    mean_value = 0
    for i in range(N):
        mean_value += A[i]

    return math.floor(mean_value/N)
