# _Max Circular Subarray Sum


def getKadaneMax(arr, n):

    curr_sum = arr[0]
    max_sum = arr[0]

    idx = 1
    while idx < n:
        curr_sum += arr[idx]

        if arr[idx] > curr_sum:
            curr_sum = arr[idx]

        if curr_sum > max_sum:
            max_sum = curr_sum

        idx += 1

    return max_sum


def getKadaneMin(arr, n):

    curr_sum = arr[0]
    min_sum = arr[0]

    idx = 1
    while idx < n:
        curr_sum += arr[idx]

        if arr[idx] < curr_sum:
            curr_sum = arr[idx]

        if curr_sum < min_sum:
            min_sum = curr_sum

        idx += 1

    return min_sum

# Complete this function


def circularSubarraySum(arr, n):

    kadane_max = getKadaneMax(arr, n)
    kadane_min = sum(arr) - getKadaneMin(arr, n)

    if kadane_max < 0 and kadane_min == 0:
        return kadane_max
    return max(getKadaneMax(arr, n), sum(arr) - getKadaneMin(arr, n))
