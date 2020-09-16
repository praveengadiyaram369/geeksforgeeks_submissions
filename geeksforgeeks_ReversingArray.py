# _Reversing an Array


def arrayReversal(arr, sizeOfArr):

    for idx in range(int(sizeOfArr/2)):
        arr[idx], arr[~idx] = arr[~idx], arr[idx]
