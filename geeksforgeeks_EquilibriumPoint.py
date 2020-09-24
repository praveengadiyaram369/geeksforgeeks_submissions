# _Equilibrium Point


def equilibriumPoint(A, N):
    sum_arr = sum(A)
    prefix_sum_left = 0
    prefix_sum_right = sum_arr - A[0]

    if prefix_sum_left == prefix_sum_right:
        return 1

    for idx in range(1, N):
        prefix_sum_left += A[idx - 1]
        prefix_sum_right -= A[idx]

        if prefix_sum_left == prefix_sum_right:
            return idx+1

    return -1
