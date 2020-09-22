# _Minimum adjacent difference in a circular array


def minAdjDiff(arr, n):

    result = abs(arr[0] - arr[-1])

    l = 0
    r = n-1

    while l <= r:

        result = min(result, min(
            abs(arr[l] - arr[l+1]), abs(arr[r] - arr[r-1])))

        l += 1
        r -= 1

    return result
