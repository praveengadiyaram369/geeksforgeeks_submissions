# _11. Wave Array


def convertToWave(A, N):

    for idx in range(0, N-1, 2):
        A[idx], A[idx+1] = A[idx+1], A[idx]
