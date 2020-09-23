# _Frequencies of Limited Range Array Elements


def frequencycount(A, N):

    for idx in range(N):
        A[idx] -= 1

    for idx in range(N):
        A[A[idx] % N] = A[A[idx] % N] + N

    for idx in range(N):
        A[idx] = int(A[idx] / N)
