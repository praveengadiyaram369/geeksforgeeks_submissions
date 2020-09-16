# _Reverse array in groups


def arrayReversal(arr, left, K):

    for idx in range(0, int(K/2)):
        arr[left+idx], arr[left + K - idx -
                           1] = arr[left + K - idx-1], arr[left+idx]

# Complete this function


def reverseInGroups(A, N, K):

    for idx in range(0, N, K):
        if idx+K <= N:
            arrayReversal(A, idx, K)

    if N % K > 1:
        arrayReversal(A, N-(N % K), N % K)

    return A


print(reverseInGroups([1, 2, 3, 4, 5, 6, 7], 7, 5))
