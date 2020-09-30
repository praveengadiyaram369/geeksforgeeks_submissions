# _Kadane's Algorithm


def maxSubArraySum(a, size):

    max_sum = a[0]
    curr_sum = a[0]

    for idx in range(1, size):

        curr_sum += a[idx]
        curr_sum = max(a[idx], curr_sum)
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum
