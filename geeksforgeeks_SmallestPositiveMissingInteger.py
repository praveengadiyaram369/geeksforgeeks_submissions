

def missingNumber(arr, n):

    for idx in range(n):
        curr_idx = arr[idx] - 1
        while 0 <= curr_idx < n and arr[idx] != arr[curr_idx]:
            arr[curr_idx], arr[idx] = arr[idx], arr[curr_idx]
            curr_idx = arr[idx] - 1

    for idx in range(n):
        if idx+1 != arr[idx]:
            return idx+1

    return n+1
