# _Leaders in an array


def arrayReversal(arr, sizeOfArr):

    for idx in range(int(sizeOfArr/2)):
        arr[idx], arr[~idx] = arr[~idx], arr[idx]

    return arr

# Complete this function


def leaders(A, N):
    max_right = A[-1]
    result = [max_right]

    right = N-2
    while right >= 0:
        if A[right] >= max_right:
            max_right = A[right]
            result.append(max_right)

        right -= 1

    return arrayReversal(result, len(result))
