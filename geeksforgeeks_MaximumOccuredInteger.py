# _Maximum occured integer


def maxOccured(L, R, N, maxx):

    prefix_sum_arr = [0] * 1000001

    for idx in range(N):
        prefix_sum_arr[L[idx]] += 1
        prefix_sum_arr[R[idx]+1] -= 1

    max_occ_val = prefix_sum_arr[0]
    max_occ_idx = 0

    for idx in range(1, max(R) + 1):
        prefix_sum_arr[idx] += prefix_sum_arr[idx-1]

        if prefix_sum_arr[idx] > max_occ_val:
            max_occ_val = prefix_sum_arr[idx]
            max_occ_idx = idx

    return max_occ_idx
