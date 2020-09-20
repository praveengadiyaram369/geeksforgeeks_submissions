# _Rotate Array


def arrayReversal(arr, left, right):
    K = (right - left)
    for idx in range(0, int(K/2)):
        arr[left+idx], arr[left + K - idx -
                           1] = arr[left + K - idx-1], arr[left+idx]


def rotateArr(A, D, N):

    arrayReversal(A, 0, D)
    arrayReversal(A, D, N)
    arrayReversal(A, 0, N)
