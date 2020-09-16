# _Strongest Neighbour


def maximumAdjacent(sizeOfArray, arr):

    for idx in range(sizeOfArray-1):
        print(max(arr[idx], arr[idx+1]), end=' ')
